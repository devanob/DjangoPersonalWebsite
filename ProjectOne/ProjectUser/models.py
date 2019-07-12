from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser,PermissionsMixin
from django_celery_beat.models import PeriodicTask
import uuid
from django.db import models

class ProjectUser(AbstractUser): 
    email = models.EmailField(unique=True)
    gitUser = models.CharField(verbose_name='Git User Name',max_length=255)
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)