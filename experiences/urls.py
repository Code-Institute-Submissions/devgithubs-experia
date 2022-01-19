from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_experiences, name='experiences'),
    path('', views.all_reviews, name='all_reviews'),
    path('<experience_id>', views.experiences_detail,
         name='experiences_detail'),
    path('add/<int:experience_id>', views.add_review, name='add_review'),
    path('edit/<int:review_id>', views.edit_review, name='edit_review'),
    path('delete/<int:review_id>', views.delete_review, name='delete_review'),
]