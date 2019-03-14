from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.views.generic import View
from projects.models import Project
from django.http import HttpResponse
# Create your views here.
class HomePage(TemplateView):
    template_name = "HomePage/homepage.html"

class HomePageView(View):
    template_name = "HomePage/homepage.html"
    
    #get function no slug
    def get(self,request):
        # get the latest three updated projects
        try:
            projectQuery = Project.objects.all()[:3]
            template_context ={'Projects'  : projectQuery , 
            "latest_project" : Project.objects.all()[:3][0]
        }
        except:
            return  render(request, self.template_name)

        return  render(request, self.template_name, 
             template_context)
    def post(self, request):
        print(request.COOKIES)
        return HttpResponse("Ohh No! This Feature isnt done yet")

# Define Which Section Is Jumped To From Externel Page Transistion 
class HomePageViewExternel(View):
    template_name = "HomePage/homepage.html"
    
    def post(self, request):
        print(request.COOKIES)
        return HttpResponse("Ohh No! This Feature isnt done yet")
    # Define Which Section Is Jumped To From Externel Page Transistion 
    def get(self, request, section):
        return HttpResponse(section)
       


