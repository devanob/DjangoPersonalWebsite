
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
from django.urls import path, re_path
from django.conf.urls import include, url
from projects.views import ProjectView, BaseRedirect,SearchProjects
from .views import ProjectsViewSet, ProjectsViewSetPaginated
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'projects-count/page-count=(?P<page_count>\d+)', ProjectsViewSetPaginated, basename='projects-count')
router.register(r'allprojects', ProjectsViewSet, basename='projects')
router.register(r'paginated-projects', ProjectsViewSetPaginated, basename='projects-pagination')


urlpatterns = [
    path(r'all-projects/page=<int:pageNum>/', ProjectView.as_view(), name = "allProjects"),
    path(r'search/page=<int:pageNum>/',SearchProjects.as_view(), name = "searchProject"),
    path(r'api-projects/', include(router.urls)),
]