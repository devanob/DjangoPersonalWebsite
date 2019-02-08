
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

# Create your views here.
class AboutPageView(TemplateView):
    template_name = "about/about.html"




