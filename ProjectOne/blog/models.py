from django.db import models
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel,InlinePanel
from wagtail.search import index
from modelcluster.fields import ParentalKey
from wagtail.images.edit_handlers import ImageChooserPanel
# Create your models here.Blog Models




#Represent A Blog Post
class BlogPage(Page):
    intro = RichTextField(blank=True)
    date = models.DateField("Post date")
    body = RichTextField(blank=True)

    #Search Index 
    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]   
    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
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

class BlogHome(Page):
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
    # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        context['categories'] = self.get_children().live().type(BlogCategory)
        return context
  