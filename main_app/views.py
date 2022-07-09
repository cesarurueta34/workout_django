from django.urls import reverse
from unicodedata import name
from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Workout, Exercise
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

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
    
    
    def get_success_url(self):
        return reverse('workout_detail', kwargs={'pk': self.object.pk})

class WorkoutUpdate(UpdateView):
    model = Workout
    fields = ['workout_name', 'type']
    template_name = "workout_update.html"
    success_url = "/workout_list/"

    def get_success_url(self):
        return reverse('workout_detail', kwargs={'pk': self.object.pk})

class WorkoutDetail(DetailView):
    model = Workout
    template_name = "workout_detail.html"

class WorkoutDelete(DeleteView):
    model = Workout
    template_name = "workout_delete_confirmation.html"
    success_url = "/workout_list/"

class ExerciseCreate(View):
     def post(self, request, pk):
         name = request.POST.get("name")
         reps = request.POST.get("reps")
         sets = request.POST.get("sets")
         weight = request.POST.get("weight")
         workout = Workout.objects.get(pk=pk)
         Exercise.objects.create(name=name, reps=reps, sets=sets, weight=weight, workout=workout)
         return redirect('workout_detail', pk=pk)
