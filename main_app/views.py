from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
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
class About(TemplateView):
    template_name = "about.html"

@method_decorator(login_required, name='dispatch')
class WorkoutList(TemplateView):
    template_name = "workout_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name=self.request.GET.get("name")
        if name != None:
            context["workouts"] = Workout.objects.filter(
                name__icontains=name, user=self.request.user)
            context["header"] = f"Searching for {name}"
        else:
            context["workouts"] = Workout.objects.filter(user=self.request.user)
            context["header"] = "My Workouts"
        return context

@method_decorator(login_required, name='dispatch')
class WorkoutCreate(CreateView):
    model = Workout
    fields = ['workout_name', 'type']
    template_name = "workout_create.html"
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(WorkoutCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('workout_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')    
class WorkoutUpdate(UpdateView):
    model = Workout
    fields = ['workout_name', 'type']
    template_name = "workout_update.html"
    success_url = "/workout_list/"

    def get_success_url(self):
        return reverse('workout_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class WorkoutDetail(DetailView):
    model = Workout
    template_name = "workout_detail.html"

@method_decorator(login_required, name='dispatch')
class WorkoutDelete(DeleteView):
    model = Workout
    template_name = "workout_delete_confirmation.html"
    success_url = "/workout_list/"

@method_decorator(login_required, name='dispatch')
class ExerciseCreate(View):
     def post(self, request, pk):
         name = request.POST.get("name")
         reps = request.POST.get("reps")
         sets = request.POST.get("sets")
         weight = request.POST.get("weight")
         workout = Workout.objects.get(pk=pk)
         Exercise.objects.create(name=name, reps=reps, sets=sets, weight=weight, workout=workout)
         return redirect('workout_detail', pk=pk)

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

@method_decorator(login_required, name='dispatch')
class ExerciseUpdate(UpdateView):
    model = Exercise
    fields = ['name', 'reps', 'sets', 'weight']
    template_name = "exercise_update.html"
    success_url = "/workout_list/"
 

@method_decorator(login_required, name='dispatch')
class ExerciseDelete(DeleteView):
    model = Exercise
    template_name = "exercise_delete_confirmation.html"
    success_url = "/workout_list/"

