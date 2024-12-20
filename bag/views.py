from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from products.models import Product


# Create your views here.
def view_bag(request):
    """ A view that displays the shopping bag. """

    return render(request, "bag/bag.html")


def add_to_bag(request, item_gtin):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, gtin=item_gtin)

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_gtin in list(bag.keys()):
        bag[item_gtin] += quantity
        messages.success(request, f'Added {product.name} to your shopping bag')
    else:
        bag[item_gtin] = quantity
        messages.success(request, f'Added {product.name} to your shopping bag')

    request.session['bag'] = bag

    return redirect(redirect_url)


def adjust_bag(request, item_gtin):
    """ Ajust a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_gtin] = quantity
    else:
        bag.pop(item_gtin)

    request.session['bag'] = bag

    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_gtin):
    """ Remove a quantity of the specified product from the shopping bag """

    try:
        product = get_object_or_404(Product, gtin=item_gtin)

        bag = request.session.get('bag', {})

        print(bag)
        print(item_gtin)

        bag.pop(item_gtin)

        request.session['bag'] = bag

        return HttpResponse(status=200)

    except Exception as e:
        error_message = f"Error removing item: {product} | {e}."
        messages.error(request, error_message)
        return HttpResponse(status=500)
