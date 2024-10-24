from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def all_products(request):
    """ A view that displays all products including sorting and search queries. """
    
    products = Product.objects.all()
    
    context = {
        'products': products,
    }
    
    return render(request, "products/products.html", context)

def product_details(request, gtin):
    """ A view that displays a single product's details. """
    
    product = get_object_or_404(Product, pk=gtin)
    
    context = {
        'product': product,
    }
    
    return render(request, "products/product_details.html", context)
