from django.db import models
from django_extensions.db import fields as extension_fields

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=31, unique=True)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
   # projects = models.ManyToManyField(Project, related_name='project_tag')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
