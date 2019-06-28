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

def get_celery_logger(name):
    logger = get_task_logger(name)
    logger.level = logging.INFO
    return logger

log = get_celery_logger(__name__)
@shared_task
def sendEmail(ContactData):
    log.info("Emailing Client...")
    subjectEmail = "Hello From Devano, {}".format(ContactData["contact_name"])
    messageEmail = render_to_string('contact/contactEmail.html', {'contact_name':ContactData["contact_name"]})
    status = send_mail(subjectEmail , messageEmail, 'DevanoBrownTech@devanobrown.tech', 
                      [ContactData["contact_email"]],
                      html_message=messageEmail,
                      fail_silently=False)
    if status:
        log.info("Sending Email Success")
    else :
        log.info("Sending Email Fail")
    send_mail("New Contact Message", "You Have A Message On your Website", 'DevanoBrownTech@devanobrown.tech', 
                      ["devanobrown@gmail.com"],
                      fail_silently=False)


