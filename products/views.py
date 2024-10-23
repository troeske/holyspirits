from django.shortcuts import render
from .models import *

# Create your views here.
def all_products(request):
    """ A view that displays all products including sorting and search queries. """
    
    products = Product.objects.all()
    
    context = {
        'products': products,
    }
    
    return render(request, "products/products.html", context)