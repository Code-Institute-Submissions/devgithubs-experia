from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Experiences


class ExperienceView(TemplateView):
    # '''
    # Class view to display experiences page
    # '''
    # model = Experiences
    # context_object_name = 'experiences'
    # template_name = "experiences/experiences.html"

    def get(self, request, *args, **kwargs):
        experiences = Experiences.objects.all()
        context = {'experiences': experiences}
        return render(request, 'experiences/experiences.html', context)