from django.db import models

from courses.models import Course

# Create your models here.
class Testimony(models.Model):
	#user
	course = models.ForeignKey(Course)
	rating = models.IntegerField(null=True, blank=True)
	review_text = models.TextField()
	date = models.DateTimeField()
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

	def __str__(self):
		return "%s" %(self.rating)