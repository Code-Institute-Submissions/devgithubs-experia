from django.urls import path
from . import views

urlpatterns = [
    path('', views.help, name='help'),
    path('help/contact-us/', views.contact_us, name='contact-us'),
]