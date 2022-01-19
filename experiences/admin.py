from django.contrib import admin
from .models import Experiences, ExperienceCategory, ExperienceReview


class ExperienceAdmin(admin.ModelAdmin):
    '''Register of Experiences model'''
    list_display = (
        'experience_category',
        'name',
        'description',
        'location',
        'price',
        'rating',
        'image',
    )
    ordering = ('experience_category',)


admin.site.register(Experiences, ExperienceAdmin)


class CategoryAdmin(admin.ModelAdmin):
    '''Register of Category model'''
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(ExperienceCategory, CategoryAdmin)


class ExperienceReviewAdmin(admin.ModelAdmin):
    '''Register of Review model'''
    list_display = (
        'user',
        'experience',
        'review_text',
        'review_rating',
    )


admin.site.register(ExperienceReview, ExperienceReviewAdmin)