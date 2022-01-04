from django.db import models
from django.contrib.auth.models import User
from experiences.models import Experiences


class Wishlist(models.Model):
    """
    Model to show all product items within the users wishlist
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experiences = models.ManyToManyField(Experiences, through="WishlistItem")

    def __str__(self):
        return Wishlist, f'({self.user})'


class WishlistItem(models.Model):
    """
    A 'through' model, allowing users to add
    individual products to their favourites.
    """

    experience = models.ForeignKey(Experiences,
                                null=False,
                                blank=False,
                                on_delete=models.CASCADE)
    wish = models.ForeignKey(Wishlist,
                                  null=False,
                                  blank=False,
                                  on_delete=models.CASCADE)

    def __str__(self):
        return self.wish.name