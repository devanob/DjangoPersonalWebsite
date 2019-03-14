from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser,PermissionsMixin
from django_celery_beat.models import PeriodicTask
class ProjectUser(AbstractUser):
    gitUser = models.CharField(verbose_name='Git User Name',max_length=255)
    #tasksPeriodic= models.ForeignKey(Person, on_delete=models.CASCADE)