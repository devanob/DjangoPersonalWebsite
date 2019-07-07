import os
from celery.utils.log import get_task_logger
from datetime import datetime
import urllib.request
from urllib.request import Request, urlopen
from celery import shared_task
import json
from ProjectUser.models import ProjectUser
from django.conf import settings
from django.utils.timezone import make_aware
import logging
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from .tokens import account_activation_token

def get_celery_logger(name):
    logger = get_task_logger(name)
    logger.level = logging.INFO
    return logger

log = get_celery_logger(__name__)
@shared_task
def sendActivationEmail(sign_up_data):
    user = ProjectUser.objects.get(username = sign_up_data["username"])
    log.info(user)
    log.info(sign_up_data)
    log.info("pk")
    log.info(urlsafe_base64_encode(force_bytes(user.pk)))
    message = render_to_string('ProjectUser/email_comfirm.html', {
                'user': user,
                'domain': sign_up_data["domain"],
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
    subjectEmail= "Account Activation-DevanoBrown.tech"

    status = send_mail(subjectEmail , message , 'DevanoBrownTech@devanobrown.tech', 
                      [sign_up_data["email"]],
                      html_message=message,
                      fail_silently=False)
    if status:
        log.info("Activation Email Send For {}".format(sign_up_data['username']))
    else:
        log.info("Activation Email Not Send For {}".format(sign_up_data['username']))
