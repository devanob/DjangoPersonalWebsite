from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .forms import CustomAuthenticationForm
# Create your views here.

class CustomLogInView(LoginView):
    authentication_form = CustomAuthenticationForm
    form_class = CustomAuthenticationForm
    template_name = 'ProjectUser/login.html'
    success_url = "home"
    redirect_authenticated_user = "home"

class CustomLogOutView(LogoutView):
    template_name = "ProjectUser/login.html"
    next_page = "home"

