from django.shortcuts import render, reverse, redirect, get_object_or_404, HttpResponse
from django.contrib import messages

from experiences.models import Experiences

from django.views.generic import TemplateView
from .forms import PostExperienceForm

from profiles.models import UserProfile




class PostExperienceView(TemplateView):
    '''
    Class view that handles form to create user experience
    '''

    template_name = 'host/host.html'

    def remove_experience(self, request, item_id):
        experience = get_object_or_404(Experiences, pk=item_id)
        experience.delete()
        messages.success(request, 'Removed from your experiences')
        return redirect(reverse('host'))

    def get(self, request):

        for key, value in request.session.items():
            print(f'key: {key}, value: {value}')
        user_experience = get_object_or_404(UserProfile, user=request.user)
        form = PostExperienceForm(instance=request.user)
        print(form)
        created_experience = user_experience.creator.all()
        context = {'experience_form': form, 'created_experience': created_experience}

        return render(request, self.template_name, context)

    def post(self, request):
        initial_name = request.user
        # experience = get_object_or_404(UserProfile, user=request.user)
        form = PostExperienceForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = initial_name
            post.save()

            messages.success(request, 'Successfully added Experience!')

            return redirect(reverse('host'))
        else:
            form = PostExperienceForm(initial={'created_by': initial_name})
            messages.error(request, 'Failed to add experience. Please ensure the form is valid.')

        context = {'experience_form': form}
        return render(request, self.template_name, context)