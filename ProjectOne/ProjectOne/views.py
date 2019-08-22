from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse

def redirectHome(request):
    home_url = reverse("home")
    return HttpResponseRedirect(home_url)

def handler404(request, exception, template_name="404.html"):
    response = render_to_response("404.html")
    response.status_code = 404
    return response

def handler404(request, exception, template_name="500.html"):
    response = render_to_response("500.html")
    response.status_code = 500
    return response