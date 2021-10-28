# from django.views.generic import TemplateView
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Experiences


# class ExperienceView(TemplateView):
#     '''
#     Class view to display experiences page
#     '''
#     model = Experiences
#     context_object_name = 'experiences'
#     template_name = "experiences/experiences.html"
#     query_set = Experiences.objects.all()

#     def get_query_set(self):
#         return self.query_set

#     def get(self, request, *args, **kwargs):
#         # GET method
#         context = {'experiences': self.get_query_set()}
#         return render(request, self.template_name, context)


def all_experiences(request):
    """ A view to show all experiences, including sorting and search queries """

    experiences = Experiences.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('experiences'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            experiences = experiences.filter(queries)

    context = {
        'experiences': experiences,
        'search_term': query,
    }

    return render(request, 'experiences/experiences.html', context)


def experiences_detail(request, experience_id):
    """ A view to show individual experience details """
    
    experience = get_object_or_404(Experiences, pk=experience_id)

    context = {
        'experience': experience,
    }

    return render(request, 'experiences/experiences_detail.html', context)