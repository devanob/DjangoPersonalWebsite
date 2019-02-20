from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import TextField
from django_extensions.db.fields import AutoSlugField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields
from organizer.models import Tag as ProjectTags

class Project(models.Model):

    # Fields
    project_name = models.CharField(max_length=255,primary_key=True)
    slug = extension_fields.AutoSlugField(populate_from='project_name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    img_link = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    project_link = models.CharField(max_length=100)
    tags = models.ManyToManyField(ProjectTags, related_name='project_tag')

    class Meta:
        ordering = ('-last_updated',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('projects', args=(self.slug,))
    

    def get_update_url(self):
        return reverse('projects', args=(self.slug,))

    def __str__(self):
        return " {} created on {} last updated {} ".format(
            self.project_name,
            self.created.strftime('%m-%d-%Y, %H:%M:%S'),
            self.last_updated.strftime('%m-%d-%Y, %H:%M:%S')
            )
    def get_img(self):
        return "img/projects/{}".format(self.img_link)