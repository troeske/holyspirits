from django.shortcuts import render
from products.models import Product, ProductTasteCategory


# Create your views here.

def index(request):
    """ A view that displays the home page. """
      
    featured_product = Product.objects.filter(featured=True)
    if featured_product.count() > 0:
        featured_product = featured_product.first() 
        product_taste_categories = ProductTasteCategory.objects.filter(product=featured_product)

    context = {
       'featured_product': featured_product,
        'product_taste_categories': product_taste_categories,
    }

    return render(request, "home/index.html", context)
