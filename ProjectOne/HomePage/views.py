from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.views.generic import View
from projects.models import Project
# Create your views here.
class HomePage(TemplateView):
    template_name = "HomePage/homepage.html"

class HomePageView(View):
    template_name = "HomePage/homepage.html"
    
    #get function no slug
    def get(self,request):
        # get the latest three updated projects
        projectQuery = Project.objects.all()[:3]
        template_context ={'Projects'  : projectQuery , 
        "latest_project" : Project.objects.all()[:3][0]
        }
        return  render(request, self.template_name, 
             template_context)
    

