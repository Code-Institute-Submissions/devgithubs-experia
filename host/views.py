from django.shortcuts import render, reverse, redirect, get_object_or_404, HttpResponse
from django.contrib import messages

from experiences.models import Experiences

from django.views.generic import TemplateView
from .forms import PostExperienceForm

from profiles.models import UserProfile


def update_experience(request, item_id):
    experience = get_object_or_404(Experiences, pk=item_id)
    if request.method == 'POST':
        form = PostExperienceForm(request.POST, request.FILES, instance=experience)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated experience!')
            return redirect(reverse('experiences_detail', args=[experience.id]))
        else:
            messages.error(request, 'Failed to update experience. Please ensure the form is valid.')
    else:
        form = PostExperienceForm(instance=experience)
        messages.info(request, f'You are editing {experience.name}')

    template = 'host/update_experience.html'
    context = {
        'form': form,
        'experience': experience,
    }

    return render(request, template, context)


def remove_experience(request, created_id):
    experience = get_object_or_404(Experiences, pk=created_id)
    experience.delete()
    messages.success(request, 'Removed from your experiences')
    return redirect(reverse('experiences'))


class PostExperienceView(TemplateView):
    '''
    Class view that handles form to create user experience
    '''
    queryset = Experiences.objects.all()
    template_name = 'host/host.html'

    def get(self, request):

        user_experience = get_object_or_404(UserProfile, user=request.user)
        form = PostExperienceForm()

        created_experience = user_experience.creator.all()
        context = {'experience_form': form, 'created_experience': created_experience}

        return render(request, self.template_name, context)

    def post(self, request):

        form = PostExperienceForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            user = get_object_or_404(UserProfile, user=request.user)
            post.created_by = user
            post.save()

            messages.success(request, 'Successfully added Experience!')

            return redirect(reverse('host'))
        else:
            form = PostExperienceForm()
            messages.error(request, 'Failed to add experience. Please ensure the form is valid.')

        context = {'experience_form': form}
        return render(request, self.template_name, context)