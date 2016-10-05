from django.db import models
from django.conf import settings
from courses.models import Course
# Create your models here.
class Enrollment(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	course = models.ForeignKey(Course)
	agreement_marketing_mail = models.BooleanField(default=True)
	enrollment_start = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
	enrollment_end = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

	def __str__(self):
		return self.course.title