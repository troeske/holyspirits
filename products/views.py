from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import *

# Create your views here.
def all_products(request):
    """ A view that displays all products including sorting and search queries. """
    
    products = Product.objects.all()
    
    query = None
    
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            # normally filter uses AND; with Q we can use OR!!!
            query = Q(name__icontains=query) | Q(description__icontains=query)    
            products = products.filter(query)
            
            
    context = {
        'products': products,
        'serch_term': query,
    }
    
    return render(request, "products/products.html", context)

def product_details(request, gtin):
    """ A view that displays a single product's details. """
    
    
    product = get_object_or_404(Product, pk=gtin)
    print("GTIN: ", gtin)
    print("Product: ", product)
    
    context = {
        'product': product,
    }
    
    return render(request, "products/product_details.html", context)
