from django.contrib import admin
from django import forms
from .models import Project

class projectAdminForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = '__all__'


class projectAdmin(admin.ModelAdmin):
    form = projectAdminForm
    list_display = ['projectName', 'slug', 'created', 'last_updated','imglink', 'description','project_link',]
    readonly_fields =  ['created', 'last_updated',]

admin.site.register(Project, projectAdmin)