from django.db import models

# Create your models here.
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import EmailField
from django.db.models import TextField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class Contact(models.Model):

    # Fields
    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField(max_length=70)
    contact_phone_number = models.CharField(blank=True,max_length=70)
    contact_message = models.CharField(max_length=200)
    contact_date = models.DateTimeField(auto_now_add=True, blank=True)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('Contact_contact_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('Contact_contact_update', args=(self.pk,))


