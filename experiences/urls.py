from django.urls import path
from . import views
# from .views import ExperienceView


urlpatterns = [
    path('', views.all_experiences, name='experiences'),
    path('<experience_id>', views.experiences_detail, name='experiences_detail'),
]