from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from experiences.models import Experiences


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
    experience = Experiences.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {experience.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    '''
    Function to adjust number of 
    experiences in the checkout bag
    '''
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    '''
    Function to remove number of 
    experiences in the checkout bag
    '''
    try:
        bag = request.session.get('bag', {})
        bag.pop[item_id]

        request.session['bag'] = bag
        return HttpResponse(status=200)
        
    except Exception as e:
        return HttpResponse(status=500)