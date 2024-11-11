from decimal import Decimal
from django.shortcuts import get_object_or_404
from django.conf import settings
from products.models import Product


def bag_contents(request):
    """
    Calculate the contents of the shopping bag, including total cost, shipping,
    and other related information.
    Args:
        request (HttpRequest): The HTTP request object containing session data.
    Returns:
        dict: A dictionary containing the following keys:
            - bag_items (list): A list of dictionaries, each containing:
                - item_gtin (str): The GTIN of the product.
                - quantity (int): The quantity of the product.
                - product (Product): The product object.
            - total (Decimal): The total cost of the items in the bag.
            - product_count (int): The total number of items in the bag.
            - shipping (Decimal): The shipping cost.
            - free_shipping_delta (Decimal): The amount needed to reach free shipping.
            - grand_total (Decimal): The total cost including shipping.
            - free_shipping_threshold (Decimal): The threshold for free shipping.
            - currency (str): The currency used for pricing.
    """

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
        'currency': settings.CURRENCY,
    }

    return context
