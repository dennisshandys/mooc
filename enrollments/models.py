from django.db import models

from courses.models import Course
# Create your models here.
class Enrollment(models.Model):
	#user
	course = models.ForeignKey(Course)
	enrollment_start = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
	enrollment_end = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

	def __str__(self):
		return self.title