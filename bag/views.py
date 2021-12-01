from django.shortcuts import render, redirect


def view_bag(request):
    '''
    View to render the users bag
    '''
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    '''
    Function to add x number of 
    experiences to the checkout bag
    '''
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)