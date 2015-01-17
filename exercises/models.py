from django.db import models

# Create your models here.
# Movement consist of the exercises a physical therapist
# creates for a patient
# they are stored by pose and orientation and are named by name
'''
class Movement(models.Model):
	name = models.CharField(max_length = 250)
	pose = models.CharField(max_length = 250)
	orientation = models.CommaSeparatedIntegerField(max_length = 200)

	# method for accessing name of exercises
	def __unicode__(self):
		return self.name
'''
class Movement(models.Model):
	patientExerciseData = models.CharField(max_length = 250)

	def __unicode__(self):
		return self.name