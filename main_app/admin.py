from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Workout, Exercise # import the Artist model from models.py
# Register your models here.

admin.site.register(Workout) # this line will add the model to the admin panel
admin.site.register(Exercise) # this line will add the model to the admin panel