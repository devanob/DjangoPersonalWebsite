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
from django.urls import path
from django.conf.urls import include, url, re_path
from .views import redirectHome
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls
##HomePage 
from HomePage.urls import urlpatterns as HomeURL
from about.urls  import urlpatterns as aboutURL
from projects.urls import urlpatterns as projectsURL
from contact.urls import urlpatterns as contactsURL
from ProjectUser.urls import urlpatterns as ProjectUserURL




#Organizer Urls
urlpatterns = [
    path('personals-admin/', admin.site.urls),
    path(r'about/', include(aboutURL) ),
    path(r'projects/', include(projectsURL) ),
    path(r'contacts/', include(contactsURL) ),
    path(r'user/', include(ProjectUserURL)),
    re_path(r'^cms-admin/', include(wagtailadmin_urls)),
    re_path(r'^documents/', include(wagtaildocs_urls)),
    path(r'', include( HomeURL) ),
]
from django.conf import settings

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Personal Admin"
admin.site.site_title = "Personal's Admin Portal"
admin.site.index_title = "Welcome to Personal's Administration Control Page"
