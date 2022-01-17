from django.urls import path
from . import views
from host.views import PostExperienceView


urlpatterns = [
    path('host', PostExperienceView.as_view(), name='host'),
    path('delete/<int:created_id>', views.remove_experience, name='remove_experience'),
    path('edit/<int:item_id>', views.update_experience, name='update_experience'),
]