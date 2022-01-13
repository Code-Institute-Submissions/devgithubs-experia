from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from profiles.models import UserProfile
from experiences.models import Experiences

from django.contrib import messages
from .models import Wishlist


@login_required
def wishlist(request):
    """
    A view to render the user's wishlist
    """
    wishlist = None
    try:
        wishlist = Wishlist.objects.get(user=request.user)
    except Wishlist.DoesNotExist:
        pass

    context = {
        'wishlist': wishlist,
    }

    return render(request, 'wishlist/wishlist.html', context)

    def __len__(self):
        """ count all the items in the favourites"""
        return sum(item['quantity'] for item in self.wishlist.values())

@login_required
def add_to_wishlist(request, item_id):
    """
    Add a product from the store to the
    wishlist for the logged in user
    """
    experience = get_object_or_404(Experiences, pk=item_id)
    redirect_url = request.POST.get('redirect_url')

    wish, _ = Wishlist.objects.get_or_create(user=request.user)

    wish.experiences.add(experience)
    messages.info(request, f'{experience.name} was added to your wishlist')

    return redirect(redirect_url)
    
@login_required
def remove_from_wishlist(request, item_id):
    """
    Add a product from the store to the
    wishlist for logged in user
    """
    wish = Wishlist.objects.get(user=request.user)
    experience = get_object_or_404(Experiences, pk=item_id)

    # Remove wish from the wishlist
    wish.experiences.remove(experience)
    messages.info(request, f'{experience.name} was removed from your wishlist')

    return redirect(reverse('wishlist'))