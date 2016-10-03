from django.db import models

from courses.models import Course, Syllabus 


# Create your models here.
class Video(models.Model):
	syllabus = models.ForeignKey(Syllabus)
	title = models.CharField(max_length=120)
	embed_code = models.CharField(max_length=500, null=True, blank=True)
	slug = models.SlugField(max_length=120)
	description = models.TextField()
	video_duration = models.DurationField(null=True, blank=True)
	featured = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

	def __str__(self):
		return self.title