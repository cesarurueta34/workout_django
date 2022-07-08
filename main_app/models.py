from django.db import models

# Create your models here.

class Workout(models.Model):

    workout_name = models.CharField(max_length=100)
    type = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']