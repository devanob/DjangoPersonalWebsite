from django.contrib import admin
from django import forms
from .models import Project

class projectAdminForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = '__all__'


class projectAdmin(admin.ModelAdmin):
    form = projectAdminForm
    list_display = ['project_name', 'slug', 'created', 'last_updated','img_link', 'description','project_link',]
    readonly_fields =  ['created', 'last_updated',]

admin.site.register(Project, projectAdmin)