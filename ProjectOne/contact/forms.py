from django import forms
from .models import Contact

class ContactClientForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'contact_message': 
                forms.Textarea(attrs={'cols': 30, 'rows':1, 'class':"form-control"}),
            'contact_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'contact_contact' : forms.TextInput(attrs={'class': 'form-control'}),
            'contact_email' : forms.EmailInput(attrs={'class': 'form-control'}),
            'contact_phone_number' : forms.TextInput(attrs={'class': 'form-control'})
        }


