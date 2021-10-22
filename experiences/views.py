from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Experiences


class ExperienceView(TemplateView):
    '''
    Class view to display experiences page
    '''
    model = Experiences
    context_object_name = 'experiences'
    template_name = "experiences/experiences.html"
    query_set = Experiences.objects.all()

    def get_query_set(self):
        return self.query_set

    def get(self, request, *args, **kwargs):
        # GET method
        context = {'experiences': self.get_query_set()}
        return render(request, self.template_name, context)