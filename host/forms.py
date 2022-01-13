from django import forms
from .models import Experiences
from experiences.models import ExperienceCategory, Experiences


class PostExperienceForm(forms.ModelForm):
    '''class to handle experience form'''
    class Meta:
        '''define class metadata'''
        model = Experiences
        fields = '__all__'
        # exclude = ('created_by',)

    def __init__(self, *args, **kwargs):
        """
        Use friendly name on experience form for categories
        """
        super(PostExperienceForm, self).__init__(*args, **kwargs)

        categories = ExperienceCategory.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['experience_category'].choices = friendly_names
        self.fields['created_by'].widget.attrs['readonly'] = True