from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('about/', views.About.as_view(), name="about"),
]