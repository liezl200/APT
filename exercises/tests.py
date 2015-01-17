from django.test import TestCase
from exercises.models import Movement

# Create your tests here.

class MovementTests(TestCase):
	"""Movement model tests."""

	def test_str(self):

		pose1 = Movement(name = "Grasp", pose = "Grasp", 
			orientation = (1, 2, 3))

		self.assertEquals(
			str(pose1),
			"Grasp")
