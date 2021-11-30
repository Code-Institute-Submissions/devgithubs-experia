# from django.views.generic import TemplateView
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Experiences, ExperienceCategory


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
    """
    A view to show all experiences,
    including sorting and search queries.
    """
    experiences = Experiences.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                experiences = experiences.annotate(lower_name=Lower('name'))
            if sortkey == 'experience_category':
                sortkey = 'experience_category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            experiences = experiences.order_by(sortkey)

        if 'experience_category' in request.GET:
            categories = request.GET['experience_category'].split(',')
            experiences = experiences.filter(experience_category__name__in=categories)
            categories = ExperienceCategory.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('experiences'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            experiences = experiences.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'experiences': experiences,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'experiences/experiences.html', context)


def experiences_detail(request, experience_id):
    """ A view to show individual experience details """
    
    experience = get_object_or_404(Experiences, pk=experience_id)

    context = {
        'experience': experience,
    }

    return render(request, 'experiences/experiences_detail.html', context)