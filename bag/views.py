from django.shortcuts import render, redirect

# Create your views here.
def view_bag(request):
    """ A view that displays the shopping bag. """
    
    return render(request, "bag/bag.html")


def add_to_bag(request, item_gtin):
    """ Add a quantity of the specified product to the shopping bag """
    
    print("gtin: ", item_gtin)
    print("quantity: ", request.POST.get('quantity'))
    
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    
    print("quantity: ", quantity)   
    print("redirect_url: ", redirect_url)
    print("bag: ", bag)
    
    if item_gtin in list(bag.keys()):
        bag[item_gtin] += quantity
    else:
        bag[item_gtin] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    
    return redirect(redirect_url)

