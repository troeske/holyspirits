from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q
from .models import *
from django.db.models.functions import Lower
from .forms import ProductForm, ProductBrandForm, CaskTypeForm, BottlerForm, ProductSizeForm



# Create your views here.

def add_related_model(request, model_type):
    """ recommended by ChatGPT to allow adding related models in a modal via AJAX """
    
    print("im view add: ", model_type)
    
    if request.method == 'POST':
        
        if model_type == "brand":
            form = ProductBrandForm(request.POST, request.FILES)
        if model_type == "bottler":
            form = BottlerForm(request.POST, request.FILES)
            
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
    else:
        form = ProductBrandForm()

    return JsonResponse({'success': False, 'errors': form.errors})


def edit_related_model(request, model_type, pk):
    """View to add/edit related models in a modal via AJAX."""
    
    print(model_type)
    
    if model_type == "brand":
        instance = get_object_or_404(ProductBrand, pk=pk)
    
    elif model_type =="bottler":
        instance = get_object_or_404(Bottler, pk=pk)

    
    if request.method == 'POST':
        
        if model_type == "brand":
            form = ProductBrandForm(request.POST, request.FILES, instance=instance)
        elif model_type == "bottler":
            form = BottlerForm(request.POST, request.FILES, instance=instance)
            
        if form.is_valid():
            # If "Remove Logo" is checked, delete the logo
            if form.cleaned_data['remove_logo']:
                instance.logo = 'placeholder'  # Set to default value
                
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})

    elif request.method == 'GET':
        data = {field.name: getattr(instance, field.name) for field in instance._meta.fields}
        
        # Add the URL for the logo if it exists
        if instance.logo:
            data['logo'] = instance.logo.url
        
        return JsonResponse({'success': True, 'instance': data})
    
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
    """ Edit a product in the store """
    
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    product = get_object_or_404(Product, pk=gtin)
    brand = get_object_or_404(ProductBrand, pk=product.brand.id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            if form.cleaned_data['remove_image']:
                product.list_image = 'placeholder'  # Set to default value
                
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_details', args=[product.gtin]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        brand_form = ProductBrandForm(instance=brand)  
        bottler_form = BottlerForm(instance=product.bottler) 
        size_form = ProductSizeForm(instance=product.size)
        cask_type_form = CaskTypeForm(instance=product.cask_type)
    
    template = 'products/edit_product.html'
    
    context = {
        'form': form,
        'brand_form': brand_form,  
        'bottler_form': bottler_form,
        'size_form': size_form,
        'cask_type_form': cask_type_form,
        'product': product,
        'on_edit_product_page': True
    }
    
    return render(request, template, context)


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

