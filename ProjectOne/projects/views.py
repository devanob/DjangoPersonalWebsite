from django.shortcuts import render
from django.views.generic import View
from django.views.generic.base import RedirectView
from django.shortcuts import render
from projects.models import Project
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from django.urls import reverse_lazy
from projects.forms import SearchProjectForm
from django.http import HttpResponse
from django.views.generic import ListView
# Create your views here.
class ProjectView(View):
    template_name = "projects/projectsList.html"
    num_pages = 6 # number of items per pagination page 
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
        pagination_context['formSearch'] = SearchProjectForm()
        return render(request, self.template_name, pagination_context)



class BaseRedirect(RedirectView):
    permanent = False
    query_string = True
    url = reverse_lazy('allProjects', kwargs={'pageNum':1})
    

class SearchProjects(ListView):
    context_object_name = 'current_page'
    template_name = "projects/projectsSearchList.html"
    form = SearchProjectForm
    num_pages = 10
    #Set Query Set 
    def get_queryset(self):
        #get the from search from the form
        self.formSearch = self.form(self.request.GET)
        if self.formSearch.is_valid():
            search = self.formSearch.generateSearchQuery()
            if not search.exists():
                return None
            pagination_Pages = Paginator(search, self.num_pages)
            try:# try to get the page if ther num is valid
                page = pagination_Pages.page(self.kwargs['pageNum'])
                print(page)
                print(self.kwargs['pageNum'])
            except PageNotAnInteger:
                page = pagination_Pages.page(1)
            except EmptyPage:
                page = pagination_Pages.page(pagination_Pages.num_pages)
            return  page
        else:
            return None
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['formSearch'] = self.formSearch
        return context

from django.shortcuts import get_object_or_404
from .serializers import ProjectSerializer
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 5
##API REST PROJECTS

class ProjectsViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving projects.
    """
    def list(self, request):
        queryset = Project.objects.all()
        serializer = ProjectSerializer(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data)

class ProjectsViewSetPaginated(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    A simple ViewSet for listing or retrieving projects.
    """
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        if ('page_count' in self.kwargs):
            page_size = int(self.kwargs['page_count'])
            self.pagination_class = None
            return Project.objects.all()[:page_size]
        return Project.objects.all()

    serializer_class = ProjectSerializer

