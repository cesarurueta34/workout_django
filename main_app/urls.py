from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('home/', views.Home.as_view(), name="home"),
    path('workout_list/', views.WorkoutList.as_view(), name="workout_list"),
    path('workout/new/', views.WorkoutCreate.as_view(), name="workout_create"), 
    path('workouts/<int:pk>/', views.WorkoutDetail.as_view(), name="workout_detail"), 
    path('workouts/<int:pk>/update',views.WorkoutUpdate.as_view(), name="workout_update"),
    path('workouts/<int:pk>/delete',views.WorkoutDelete.as_view(), name="workout_delete"),
    path('workouts/<int:pk>/exercises/new/', views.ExerciseCreate.as_view(), name="exercise_create")

]