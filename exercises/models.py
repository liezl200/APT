from django.db import models

# Movement consist of the exercises a physical therapist
# creates for a patient
# they are stored by pose and orientation and are named by name
class Movement(models.Model):
	patientExerciseData = models.CharField(max_length = 250)

	def __unicode__(self):
		return self.patientExerciseData