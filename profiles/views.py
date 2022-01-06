from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from experiences.models import Experiences
from .forms import UserProfileForm

from checkout.models import Order

from django.views.generic import TemplateView
from profiles.forms import PostExperienceForm


def profile(request):
    '''
    Render the user's profile page
    '''
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is correct')
    else: 
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.success(request, (
        f'This is a past confirmation for order number {order_number}.'
        'A confirmation email was sent on the order date'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True
    }
    return render(request, template, context)


# def wishlist(request):
#     '''
#     Render the wishlist page
#     '''
    
#     return render(request, 'profiles/wishlist.html')


# def add_to_wishlist(request, item_id):
#     '''
#     Add an experience to the user's wishlist
#     '''
#     experience = get_object_or_404(Experiences, pk=item_id)
#     redirect_url = request.POST.get('redirect_url')
#     wishes = request.session.get('wishes', {})
    
    
#     messages.success(request, f'Added {experience.name} to your wishlist')

#     request.session['wishes'] = wishes
#     print(f'{wishes} added')
#     return redirect(redirect_url)


class PostExperienceView(TemplateView):

    template_name = 'profiles/post-experience.html'

    def get(self, request):
        form = PostExperienceForm
        created = Experiences.objects.filter(description=request.user)
        
        print(created)
        context = {'experience_form': form, 'created_experience': created}

        return render(request, self.template_name, context)

    def post(self, request):
        form = PostExperienceForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, f'Successfully added Experience!')

            # text = form.cleaned_data['post']
            form = PostExperienceForm()
            return redirect(reverse('post_experience'))
        else:
            messages.error(request, f'Failed to add experience. Please ensure the form is valid.')

        context = {'experience_form': form}
        
        return render(request, self.template_name, context)