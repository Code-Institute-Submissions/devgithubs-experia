from django.contrib import admin
from .models import Experiences, ExperienceCategory


class ExperienceAdmin(admin.ModelAdmin):
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


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Experiences, ExperienceAdmin)
admin.site.register(ExperienceCategory, CategoryAdmin)
