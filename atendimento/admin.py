from django.contrib import admin
from django.db.models.base import ModelBase
from .models import Projects

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

admin.site.register(Projects, ProjectAdmin)