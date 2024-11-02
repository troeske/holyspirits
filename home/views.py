from django.shortcuts import render
from products.models import Product


# Create your views here.

def index(request):
    """ A view that displays the home page. """
      
    featured_product = Product.objects.filter(featured=True)
    if featured_product.count() > 0:
        featured_product = featured_product.first()
    
    context = {
        'featured_product': featured_product,
    }

    return render(request, "home/index.html", context)