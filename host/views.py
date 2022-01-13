from django.shortcuts import render, reverse, redirect, get_object_or_404, HttpResponse
from django.contrib import messages

from experiences.models import Experiences

from django.views.generic import TemplateView
from .forms import PostExperienceForm

from .models import ExperienceList, ExperienceListItem
from profiles.models import UserProfile


class PostExperienceView(TemplateView):

    template_name = 'host/host.html'

    def get(self, request):
        # experience = None
        form = PostExperienceForm
        # try:
        #     created_experience = Experiences.objects.filter(user=request.user)
        # except ExperienceList.DoesNotExist:
        #     pass
        exp = Experiences.objects.all()
        print(exp)
        experience = get_object_or_404(UserProfile, user=request.user)
        print(experience)
        created_experience = experience.creator.all()
        context = {'experience_form': form, 'created_experience': created_experience}

        return render(request, self.template_name, context)

    def post(self, request):
        experience = get_object_or_404(UserProfile, user=request.user)
        form = PostExperienceForm(request.POST, request.FILES, instance=experience) #initial={'created_by': created_by}
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            print(f'the post is: {post}')
            messages.success(request, 'Successfully added Experience!')

            return redirect(reverse('host'))
        else:
            form = PostExperienceForm()
            messages.error(request, 'Failed to add experience. Please ensure the form is valid.')

        context = {'experience_form': form}
        return render(request, self.template_name, context)


def remove_experience(request, item_id):
    experience = get_object_or_404(Experiences, pk=item_id)
    experience.delete()
    messages.success(request, 'Removed from your experiences')
    return redirect(reverse('host'))