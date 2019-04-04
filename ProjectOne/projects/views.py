from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render
from projects.models import Project
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
# Create your views here.
class ProjectView(View):
    template_name = "projects/projectsList.html"
    num_pages = 3 # number of items per pagination page 
    default_page =  1 ## page to do if error such as out of bound paging 
    #get function no slug
    def get(self,request, pageNum):
        allProjects = Project.objects.all()
        pagination_Pages = Paginator(allProjects, self.num_pages)
        ##check if user gave number 
        try:# try to get the page if ther num is valid
            page = pagination_Pages.page(pageNum)
        except PageNotAnInteger:
            page = pagination_Pages.page(1)
        except EmptyPage:
            page = pagination_Pages.page(pagination_Pages.num_pages)
        pagination_context = {'current_page' : page}
        if pageNum == 1 :
            pagination_context['addHeader'] = True
        return render(request, self.template_name, pagination_context)
       
