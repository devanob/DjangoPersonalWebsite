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
from django.contrib.staticfiles.templatetags.staticfiles import static
from ProjectUser.models import ProjectUser as ProjectUserHandlier
from ProjectOne.settings import STATICFILES_DIRS
def project_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_STATIC_URL<id>/<filename>
    return '{}/img/project_img/{}'.format(STATICFILES_DIRS[0],filename)
class Project(models.Model):

    # Fields
    projectName = models.CharField(max_length=255,verbose_name='name',primary_key=True)
    slug = extension_fields.AutoSlugField(populate_from='projectName', blank=True)
    created = models.DateTimeField(verbose_name='Date Created')
    last_updated = models.DateTimeField(verbose_name='Date Updated')
    imglink = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    project_link = models.CharField(max_length=100)
    tags = models.ManyToManyField(ProjectTags, blank=True, null=True, related_name='project_tag')
    projectHandlier = models.ForeignKey(ProjectUserHandlier,on_delete=models.CASCADE, related_name="projectUserHandlier",)
    project_image = models.ImageField(upload_to="img/project_img/", 
                                    blank=True)

    class Meta:
        ordering = ('-last_updated',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('projects', args=(self.slug,))
    

    def get_update_url(self):
        return reverse('projects', args=(self.slug,))

    def __str__(self):
        return "{} created on {} last updated {} ".format(
            self.projectName,
            self.created.strftime('%m-%d-%Y, %H:%M:%S'),
            self.last_updated.strftime('%m-%d-%Y, %H:%M:%S'),
            )
    def get_img(self):
        return static("img/projects/{}".format(self.imglink))