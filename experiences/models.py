from django.db import models


class ExperienceCategory(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name():
        return self.friendly_name


class Experiences(models.Model):

    class Meta:
        verbose_name_plural = 'Experiences'

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
    rating = models.DecimalField(max_digits=6, decimal_places=2)
    hosted_by = models.CharField(max_length=254)
    
    def __str__(self):
        return self.name