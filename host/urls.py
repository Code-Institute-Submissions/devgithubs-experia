from django.urls import path
from . import views
from .views import PostExperienceView

urlpatterns = [
    path('host', PostExperienceView.as_view(), name='host'),
    path('remove_experience/<int:item_id>', views.remove_experience, name='remove_experience'),
]