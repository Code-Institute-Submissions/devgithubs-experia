from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from experiences.models import Experiences


@login_required
def view_bag(request):
    '''
    View to render the users bag
    '''
    return render(request, 'bag/bag.html')


@login_required
def add_to_bag(request, item_id):
    '''
    Function to add x number of
    experiences to the checkout bag
    '''
    experience = get_object_or_404(Experiences, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Updated {experience.name} n\
                         quantity to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {experience.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


@login_required
def adjust_bag(request, item_id):
    '''
    Function to adjust number of
    experiences in the checkout bag
    '''
    experience = get_object_or_404(Experiences, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Updated {experience.name} n\
                         quantity to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {experience.name} from your bag')
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


@login_required
def remove_from_bag(request, item_id):
    '''
    Function to remove number of
    experiences in the checkout bag
    '''
    try:
        experience = get_object_or_404(Experiences, pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(request, f'Removed {experience.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)