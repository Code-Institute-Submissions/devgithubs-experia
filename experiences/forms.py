from django import forms
from .models import ExperienceReview


class ReviewAdd(forms.ModelForm):
    '''Class to handle Adding review form'''
    class Meta:
        '''define meta characteristics of form'''
        model = ExperienceReview
        fields = ('review_text', 'review_rating')