from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('home/', views.Home.as_view(), name="home"),
    path('workout_list/', views.WorkoutList.as_view(), name="workout_list"),
     path('workout/new/', views.WorkoutCreate.as_view(), name="workout_create")

]