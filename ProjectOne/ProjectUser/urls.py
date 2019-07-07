"""ProjectOne URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from .views import CustomLogInView, CustomLogOutView , CustomSignUpView, ActivateAccount
##
urlpatterns = [
    path(r'login/', CustomLogInView.as_view(), name = "login"),
    path(r'logout/', CustomLogOutView.as_view(), name = "logout"),
    path(r'signup/', CustomSignUpView.as_view(), name = "signup"),
    path('activate/<str:uidb64>/<str:token>', ActivateAccount.as_view(), name='activate'),
]