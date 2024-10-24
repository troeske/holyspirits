from decimal import Decimal
from django.shortcuts import get_object_or_404
from django.conf import settings
from products.models import Product

def bag_contents(request):
    
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    
    for item_gtin, quantity in bag.items():
        product = get_object_or_404(Product, gtin=item_gtin)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_gtin': item_gtin,
            'quantity': quantity,
            'product': product,
        })
    
    if total < settings.FREE_SHIPPING_THRESHOLD:
        shipping = total * Decimal(settings.STANDARD_SHIPPING_PERCENTAGE / 100)
        free_shipping_delta = settings.FREE_SHIPPING_THRESHOLD - total
    else:
        shipping = 0
        free_shipping_delta = 0
    
    grand_total = shipping + total
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'shipping': shipping,
        'free_shipping_delta': free_shipping_delta,
        'grand_total': grand_total,
        'free_shipping_threshold': settings.FREE_SHIPPING_THRESHOLD,
    }
    
    print(context)
    
    return context
    