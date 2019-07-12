from django.contrib import admin
from .models import ProjectUser
from django.contrib.auth.admin import UserAdmin as UseBaseAdmin
from projects.tasks import generateProjects
from django.contrib.auth.forms import UserCreationForm
import logging
log = logging.getLogger('ProjectOne')


class UserCreateForm(UserCreationForm):

    class Meta:
        model = ProjectUser
        fields = ('username', 'first_name' , 'last_name', )


def UpdateProjects(modeladmin, request, queryset):
    for user in queryset:
        try:
            log.info("Projects OF User Update: {}".format(user.username ))
            generateProjects.delay(user.username)
        except:
            log.error("Error Finding User")
            log.error(queryset)
    


UpdateProjects.short_description = "Update Selected User Project"
class UserAdmin(UseBaseAdmin):
    add_form = UserCreateForm
    # The forms to add and change user instances
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    actions = [UpdateProjects]
    list_display = ('email', 'is_staff', 'is_active','gitUser', "uuid")
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    search_fields = ('email',)
    fieldsets = UseBaseAdmin.fieldsets +(
        
        (
            ('GitInfo'), 
            {'fields': 
                ('gitUser',)
                }
        ),
        
    )
    
    ordering = ('email',)
    filter_horizontal = ()
admin.site.register(ProjectUser,UserAdmin)