from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse

def redirectHome(request):
    home_url = reverse("home")
    return HttpResponseRedirect(home_url)

