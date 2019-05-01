from django.contrib.auth.forms import AuthenticationForm
from django import forms
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'})
    )
    password = forms.CharField(label=("Password"), widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-lg'})
    )
