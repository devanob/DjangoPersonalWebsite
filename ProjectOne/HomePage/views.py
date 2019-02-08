from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

# Create your views here.
class HomePage(TemplateView):
    template_name = "HomePage/homepage.html"