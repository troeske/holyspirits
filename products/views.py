from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import *
from django.db.models.functions import Lower
from .forms import ProductForm


# Create your views here.
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
            query = Q(name__icontains=query) | Q(description__icontains=query)    
            products = products.filter(query)
        
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
        'serch_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }
    
    return render(request, "products/products.html", context)

def product_details(request, gtin):
    """ A view that displays a single product's details. """
    
    product = get_object_or_404(Product, pk=gtin)

    context = {
        'product': product,
    }
    
    return render(request, "products/product_details.html", context)


def add_product(request):
    """ Add a product to the store """
    
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

def edit_product(request, gtin):
    """ Edit a product in the store """
    
    product = get_object_or_404(Product, pk=gtin)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_details', args=[product.gtin]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')
    
    template = 'products/edit_product.html'
    
    context = {
        'form': form,
        'product': product,
        'on_edit_product_page': True
    }
    
    return render(request, template, context)

def delete_product(request, gtin):
    """ Edit a product in the store """
    
    product = get_object_or_404(Product, pk=gtin)
    product.delete()
    messages.info(request, f'The product {product.name} has been deleted!')
    
    return redirect(reverse('products'))

