from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag")
        return redirect(reverse('experiences'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JZXQlEU0gY4PkcvtOqUF9L2OE0AD6wf4eGAVumskou44wQUvNC8uLEOLZnD6X0bRR4oj9NxYc7efi2xSxg5CfsS00RGPGkzqR',
        'client_secret': 'test client secret',
    }
    return render(request, template, context)