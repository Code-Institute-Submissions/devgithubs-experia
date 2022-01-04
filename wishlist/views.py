from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from profiles.models import UserProfile
from experiences.models import Experiences

from django.contrib import messages
from .models import Wishlist



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