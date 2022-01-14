from django.urls import path
from host.views import PostExperienceView


urlpatterns = [
    path('host', PostExperienceView.as_view(), name='host'),
    path('remove_experience/<int:item_id>', PostExperienceView.remove_experience, name='remove_experience'),
]