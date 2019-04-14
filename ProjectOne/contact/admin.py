from django.contrib import admin
from django import forms
from .models import Contact

class ContactAdminForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'


class ContactAdmin(admin.ModelAdmin):
    form = ContactAdminForm
    list_display = ['contact_name', 
    'contact_email', 'contact_phone_number', 
    'contact_message','contact_date']


admin.site.register(Contact, ContactAdmin)