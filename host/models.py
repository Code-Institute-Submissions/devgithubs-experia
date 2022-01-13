from django.db import models
from django.contrib.auth.models import User
from experiences.models import Experiences


class PostExperienceView(Experiences, models.Model):
    pass


class ExperienceList(models.Model):
    """
    Model to show all product items within the users created Experiences
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experiences = models.ManyToManyField(Experiences, through="ExperienceListItem")

    def __str__(self):
        return ExperienceList, f'({self.user})'


class ExperienceListItem(models.Model):
    """
    A 'through' model, allowing users to add
    unique experiences to their profile.
    """

    experience = models.ForeignKey(Experiences,
                                null=False,
                                blank=False,
                                on_delete=models.CASCADE)
    posted_experience = models.ForeignKey(ExperienceList,
                                  null=False,
                                  blank=False,
                                  on_delete=models.CASCADE)

    def __str__(self):
        return self.posted_experience.name