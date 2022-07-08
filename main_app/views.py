from unicodedata import name
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.

class Home(View): 
    def get(self, request): 
        return HttpResponse("Workout Main Page")

class Home(TemplateView):
    template_name = "home.html"


