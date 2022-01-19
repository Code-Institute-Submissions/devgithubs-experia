from django.db import models
from django.contrib.auth.models import User
from profiles.models import UserProfile


class ExperienceCategory(models.Model):
    '''Model that handles the experience categories '''
    class Meta:
        '''Define characteristics of model'''
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        '''returns a string of the category name'''
        return str(self.name)

    def get_friendly_name(self):
        '''returns a more readable version of the category name'''
        return self.friendly_name


class Experiences(models.Model):
    '''Model that handles the experiences'''
    class Meta:
        '''Define meta characteristics of model'''
        verbose_name_plural = 'Experiences'

    created_by = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                   null=True, blank=True,
                                   related_name='creator')
    experience_category = models.ForeignKey(
        'ExperienceCategory', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    location = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.CharField(max_length=20)
    age_restricted = models.BooleanField(default=False)
    language_default = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    hosted_by = models.CharField(max_length=254)

    def __str__(self):
        '''returns a string of the experience name'''
        return str(self.name)

    def creator(self):
        '''returns the creator of an experience'''
        return self.created_by


RATING = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)


class ExperienceReview(models.Model):
    '''Model that handles the review model'''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    experience = models.ForeignKey(Experiences, related_name='reviews',
                                   on_delete=models.CASCADE)
    review_text = models.CharField(max_length=200)
    review_rating = models.CharField(max_length=100, choices=RATING)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        '''Define meta characteristics of review model'''
        ordering = ('created_on',)