from django.views.generic import TemplateView


class HomeView(TemplateView):
    '''
    Generic class view to display home page
    '''
    template_name = "home/index.html"