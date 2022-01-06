from django.urls import path
from . import views
from profiles.views import PostExperienceView
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.profile, name='profile'),
    path('', PostExperienceView.as_view(), name='post_experience'),
    path('order_history/<order_number>/', views.order_history, name='order_history'),
]