from django.db import models
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel,InlinePanel
from wagtail.search import index
from modelcluster.fields import ParentalKey
from wagtail.images.edit_handlers import ImageChooserPanel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your models here.Blog Models
import logging
log = logging.getLogger(__name__)
from django.conf import settings
#Represent A Blog Post
class BlogPage(Page):
    description = models.CharField(blank=True,max_length=255)
    date = models.DateField("Post date")
    body = RichTextField(blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='+')

    #Search Index 
    search_fields = Page.search_fields + [
        index.SearchField('description'),
        index.SearchField('body'),
    ]   
    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('author'),
        FieldPanel('description'),
        FieldPanel('body', classname="full"),
        InlinePanel('gallery_images', label="Gallery images"),

    ]

#Represent A Blog Image
class BlogImages(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images', blank=True)
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+')
    caption = models.CharField(blank=True, max_length=250)
    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]

#Represent A Blog category
class BlogCategory(Page):
    name =  models.CharField(max_length=255,verbose_name='name_category')
    description = models.CharField(max_length=255,verbose_name='description_category')
    colour = models.CharField(max_length=255,verbose_name='colour_category')
    catergory_image = models.ImageField(upload_to="img/blog/blog_category", 
                                    blank=True)
    children_max_page_size = 10
    content_panels = Page.content_panels + [
        FieldPanel('name', classname="full"),
        FieldPanel('description', classname="full"),
        FieldPanel('colour', classname="full"),
        FieldPanel('catergory_image', classname="full")
    ]
    search_fields = Page.search_fields + [
        index.SearchField('name'),
        index.SearchField('description'),
    ]
    def get_context(self, request):


        context = super(BlogCategory, self).get_context(request)

        # Get the full unpaginated listing of resource pages as a queryset -
        # replace this with your own query as appropriate
        blogpages = self.get_children().live().order_by('-first_published_at')
        paginator = Paginator(blogpages, self.children_max_page_size)

        page = request.GET.get('page',1)
        try:
            blogpages = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            blogpages = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            blogpages = paginator.page(paginator.num_pages)

        # make the variable 'resources' available on the template\
        
        context['blogpages'] = blogpages

        return context
    subpage_types = ["blog.BlogPage"]
    
    
#represents the BlogHome Page
class BlogHome(Page):
    ##pagination max page size 
    children_max_page_size = 10

    intro = RichTextField(blank=True)
    body = RichTextField(blank=True)
    blog_home_image = models.ImageField(upload_to="img/blog/blog_home", 
                                    blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        FieldPanel('intro', classname="full"),
        FieldPanel('blog_home_image', classname="full"),
    ]
    def get_context(self, request):
    # Update context to include only published categories, ordered by reverse-chron
        context = super().get_context(request)
        context['categories'] = self.get_children().live().type(BlogCategory)
        return context
  