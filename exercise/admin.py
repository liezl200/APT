from django.contrib import admin
from exercise.models import Movement

# Register your models here.

#ExerciseTrack tracks whether a task was completed or not/ect



admin.site.unregister(Movement)
admin.site.register(Movement)
#admin.site.register(DateTime)
