from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
def redirectHome(request):
    return HttpResponseRedirect('/home/')

class HomePage(TemplateView):
    template_name = "index.html"
