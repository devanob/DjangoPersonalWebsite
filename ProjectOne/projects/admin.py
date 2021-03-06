from django.contrib import admin
from django import forms
from .models import Project

class projectAdminForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = '__all__'


class projectAdmin(admin.ModelAdmin):
    form = projectAdminForm
    list_display = ['projectName','last_updated', 'projectHandlier', 'project_image']


from django.contrib.auth.models import Permission 

admin.site.register(Permission)
admin.site.register(Project, projectAdmin)