from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Workout(models.Model):

    type = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)    
    
    def __str__(self):
        return self.workout_name

    class Meta:
        ordering = ['-created_at']


class Exercise(models.Model):

    name = models.CharField(max_length=150)
    reps = models.IntegerField(default=0)
    sets = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name="exercises")

    def __str__(self):
        return self.name
