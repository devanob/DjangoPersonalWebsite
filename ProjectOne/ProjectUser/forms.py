from django.contrib.auth.forms import AuthenticationForm
from django import forms
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'})
    )
    password = forms.CharField(label=("Password"), widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-lg'})
    )


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
class SignupForm(UserCreationForm):

    username = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'})
    )

    email = forms.EmailField(max_length=200, help_text='Required', widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'})
    )
    password1 = forms.CharField(label=("Password"), widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-lg'})
    )

    password2 = forms.CharField(
        label=("Password confirmation"),
        # help_text=_("Enter the same password as above, for verification."), 
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
        
    )
   

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = False
        if commit:
            user.save()
        return user