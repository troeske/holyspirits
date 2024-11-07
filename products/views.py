from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.db.models import Q
from .models import *
from django.db.models.functions import Lower
from django.forms import inlineformset_factory
from .forms import * 



# Create your views here.
@login_required
def add_related_model(request, model_type):
    """View to add related models via AJAX."""
    if not request.user.is_superuser:
        return JsonResponse({'success': False, 'error': 'Unauthorized access.'}, status=403)

    # Replace request.is_ajax() with direct header check
    if request.method == 'GET' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if model_type == "brand":
            form = ProductBrandForm()
        elif model_type == "bottler":
            form = BottlerForm()
        else:
            return JsonResponse({'success': False, 'error': 'Invalid model type'}, status=400)

        action_url = reverse('add_related_model', args=[model_type])

        logo_url = 'https://res.cloudinary.com/dqd3t6mmb/image/upload/v1730352034/noimage_ytgewe.png'

        logo_placeholder = True

        context = {'form': form,
                   'action_url': action_url,
                   'logo_url': logo_url,
                   'logo_placeholder': logo_placeholder
                   }

        form_html = render_to_string('products/includes/related_model_form.html', context, request=request)

        return JsonResponse({'success': True, 'form_html': form_html})

    elif request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if model_type == "brand":
            form = ProductBrandForm(request.POST, request.FILES)
        elif model_type == "bottler":
            form = BottlerForm(request.POST, request.FILES)
        else:
            return JsonResponse({'success': False, 'error': 'Invalid model type'}, status=400)

        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            action_url = reverse('add_related_model', args=[model_type])
            context = {'form': form, 'action_url': action_url}
            form_html = render_to_string('products/includes/related_model_form.html', context, request=request)
            return JsonResponse({'success': False, 'form_html': form_html})

    else:
        return JsonResponse({'success': False, 'error': 'Method not allowed'}, status=405)
    

@login_required
def edit_related_model(request, model_type, pk):
    """View to edit related models via AJAX."""
    if not request.user.is_superuser:
        return JsonResponse({'success': False, 'error': 'Unauthorized access.'}, status=403)

    if model_type == "brand":
        instance = get_object_or_404(ProductBrand, pk=pk)
        form_class = ProductBrandForm
    elif model_type == "bottler":
        instance = get_object_or_404(Bottler, pk=pk)
        form_class = BottlerForm
    else:
        return JsonResponse({'success': False, 'error': 'Invalid model type'}, status=400)

    if request.method == 'GET' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = form_class(instance=instance)
        action_url = reverse('edit_related_model', args=[model_type, pk])
        
        if instance.logo.url == 'http://res.cloudinary.com/dqd3t6mmb/image/upload/placeholder':
            logo_url = 'https://res.cloudinary.com/dqd3t6mmb/image/upload/v1730352034/noimage_ytgewe.png'
            logo_placeholder = True
        else:
            logo_url = instance.logo.url
            logo_placeholder = False
        
        context = {'form': form,
                   'action_url': action_url,
                   'logo_url': logo_url,
                   'logo_placeholder': logo_placeholder
                   }

        form_html = render_to_string('products/includes/related_model_form.html', context, request=request)

        return JsonResponse({'success': True, 'form_html': form_html})

    elif request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = form_class(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            if form.cleaned_data.get('remove_logo'):
                instance.logo = 'placeholder'  # Set to default value
            form.save()
            return JsonResponse({'success': True})
        else:
            action_url = reverse('edit_related_model', args=[model_type, pk])
            context = {'form': form, 'action_url': action_url}
            form_html = render_to_string('products/includes/related_model_form.html', context, request=request)
            return JsonResponse({'success': False, 'form_html': form_html})
    else:
        return JsonResponse({'success': False, 'error': 'Method not allowed'}, status=405)

def all_products(request):
    """ A view that displays all products including sorting and search queries. """
    
    products = Product.objects.all()
    
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            # normally filter uses AND; with Q we can use OR!!!
            search_conditions = (
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(producttastecategory__taste_category__name__icontains=query) |
                Q(producttastecategory__taste_category__description__icontains=query)
            )
            
            products = products.filter(search_conditions).distinct()
        
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            # filter using fk product_category pointing to ProductCategory
            # and __name to get the name field of the ProductCategory
            products = products.filter(product_category__name__in=categories)
            categories = ProductCategory.objects.filter(name__in=categories)
        
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            
            if sortkey == 'productcategory':
                sortkey = 'product_category__name'    
            
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            
            products = products.order_by(sortkey)
    
    current_sorting = f'{sort}_{direction}'
    
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }
    
    return render(request, "products/products.html", context)

def product_details(request, gtin):
    """ A view that displays a single product's details. """
    
    product = get_object_or_404(Product, pk=gtin)
    product_taste_categories = ProductTasteCategory.objects.filter(product=product)

    context = {
        'product': product,
        'product_taste_categories': product_taste_categories,
    }
    
    return render(request, "products/product_details.html", context)


@login_required
def add_product(request):
    """ Add a product to the store """
    
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
                                
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_details', args=[product.gtin]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')

    else:
        form = ProductForm()
    
    template = 'products/add_product.html'
    
    context = {
        'form': form,
        'on_add_product_page': True
    }
    
    return render(request, template, context)


@login_required
def edit_product(request, gtin):
    """Edit a product in the store"""
    
    print('Edit product view: ' + str(gtin), request.method)
    
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    product = get_object_or_404(Product, pk=gtin)
    
    # Determine if the product has a placeholder image
    placeholder_url = 'http://res.cloudinary.com/dqd3t6mmb/image/upload/placeholder'
    if product.list_image and product.list_image.url != placeholder_url:
        img_url = product.list_image.url
        img_placeholder = False
    else:
        img_url = 'https://res.cloudinary.com/dqd3t6mmb/image/upload/v1730352034/noimage_ytgewe.png'
        img_placeholder = True
    
    # Create an inline formset for ProductImage, suggested by ChatGPT
    ProductImageFormSet = inlineformset_factory(
        Product,
        ProductImage,
        form=ProductImageForm,
        extra=1,  # Provide an extra form to add new images
        can_delete=True
    )
    
    # using the same logic as for product images for the new Taste Category formset
    ProductTasteCategoryFormSet = inlineformset_factory(
        Product,
        ProductTasteCategory,
        form=ProductTasteCategoryForm,
        extra=0,
        can_delete=True
    )
            
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        formset = ProductImageFormSet(request.POST, request.FILES, instance=product)
        taste_formset = ProductTasteCategoryFormSet(request.POST or None, instance=product, prefix='tastecategory_set')
   
        print(form.is_valid())
        print(formset.is_valid())
        print(taste_formset.is_valid())
        print(taste_formset.errors)

        if form.is_valid() and formset.is_valid() and taste_formset.is_valid():
            if form.cleaned_data.get('remove_image'):
                product.list_image = None
            
            form.save()          
            formset.save()
            taste_formset.save()
            
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_details', args=[product.gtin]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        formset = ProductImageFormSet(instance=product)
        taste_formset = ProductTasteCategoryFormSet(instance=product, prefix='tastecategory_set')
    
    # For adding new Taste Categories
    taste_category_form = TasteCategorySelectionForm()
    
    template = 'products/edit_product.html'
    
    context = {
        'form': form,
        'formset': formset,
        'taste_formset': taste_formset,
        'taste_category_form': taste_category_form,
        'product': product,
        'on_edit_product_page': True,
        'img_url': img_url,
        'img_placeholder': img_placeholder
    }
    
    return render(request, template, context)


@login_required
def add_taste_categories(request, gtin):
    """ 
    Add one or more taste categories to a product via AJAX
    Suggested by ChatGPT
    
    """
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        product = get_object_or_404(Product, pk=gtin)
        form = TasteCategorySelectionForm(request.POST)

        if form.is_valid():
            taste_categories = form.cleaned_data['taste_categories']
            new_categories = []
            for category in taste_categories:
                # Check if the association already exists
                association, created = ProductTasteCategory.objects.get_or_create(
                    product=product,
                    taste_category=category
                )
                if created:
                    new_categories.append({
                        'id': association.id,
                        'name': category.name,
                        'fa_icon': category.fa_icon,
                        'form_index': ProductTasteCategory.objects.filter(product=product).count() - 1
                    })
            data = {
                'success': True,
                'new_taste_categories': new_categories
            }
            return JsonResponse(data)
        else:
            return JsonResponse({'success': False, 'error': 'Invalid form data'}, status=400)
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)


@login_required
def delete_product(request, gtin):
    """ Delete a product in the store """
    
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    product = get_object_or_404(Product, pk=gtin)
    product.delete()
    messages.info(request, f'The product {product.name} has been deleted!')
    
    return redirect(reverse('products'))

