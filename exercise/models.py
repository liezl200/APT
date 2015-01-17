from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User, Group
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible

# Movement consist of the exercises a physical therapist
# creates for a patient
# they are stored by pose and orientation and are named by name
class Movement(models.Model):
	name = models.CharField(max_length = 250)
	pose = models.CharField(max_length = 250)
	orientation = models.CommaSeparatedIntegerField(max_length = 200)

	# method for accessing name of exercies
	def __unicode__(self):
		return self.name






