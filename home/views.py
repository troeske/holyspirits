from django.shortcuts import render
from products.models import Product, ProductTasteCategory


# Create your views here.

def index(request):
    """ A view that displays the home page. """
    
    context = {
     }

    return render(request, "home/index.html", context)
