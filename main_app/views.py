from unicodedata import name
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Workout
from django.views.generic.edit import CreateView
# Create your views here.

class Home(View): 
    def get(self, request): 
        return HttpResponse("Workout Main Page")

class Home(TemplateView):
    template_name = "home.html"

class WorkoutList(TemplateView):
    template_name = "workout_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["workouts"] = Workout.objects.all() # Here we are using the model to query the database for us.
        return context

class WorkoutCreate(CreateView):
    model = Workout
    fields = ['workout_name', 'type']
    template_name = "workout_create.html"
    success_url = "/workout_list/"