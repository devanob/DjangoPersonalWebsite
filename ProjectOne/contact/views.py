from django.shortcuts import render
from django.views.generic import View
from projects.models import Project
from django.http import HttpResponse, JsonResponse
from .forms import  ContactClientForm
import json


class ContactForm(View):
    
    def post(self, request):
        formDataRaw = request.body
        dictData = json.loads(formDataRaw)
        contactForm = ContactClientForm(dictData)
        if contactForm.is_valid():
            contactForm.save()
            return JsonResponse({'status': 1})
        else:
            return JsonResponse(contactForm.errors, status=341)