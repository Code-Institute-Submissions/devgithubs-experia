from django.contrib import admin
from .models import ExperienceList, ExperienceListItem, PostExperienceView

# Register your models here.
admin.site.register(ExperienceList)
admin.site.register(ExperienceListItem)
admin.site.register(PostExperienceView)