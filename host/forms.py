from django import forms
from experiences.models import ExperienceCategory, Experiences


class PostExperienceForm(forms.ModelForm):
    '''class to handle experience form'''
    class Meta:
        '''define class metadata'''
        model = Experiences
        exclude = ['created_by', 'rating']
        fields = ('name', 'description', 'experience_category',
                  'location', 'price', 'duration', 'age_restricted',
                  'language_default', 'image', 'hosted_by')

    def __init__(self, *args, **kwargs):
        """
        Use friendly name on experience form for categories
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Experience name',
            'description': 'Description',
            'experience_category': 'Category',
            'location': 'Location',
            'price': 'Price',
            'duration': 'Duation (mins)',
            'age_restricted': 'Suitable for ages under 18?',
            'language_default': 'English?',
            'image': 'Image',
            'hosted_by': 'Host name',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder

        categories = ExperienceCategory.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        self.fields['experience_category'].choices = friendly_names