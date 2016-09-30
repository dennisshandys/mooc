from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models


def download_media_location(instance, filename):
	return "%s/%s" %(instance.slug, filename)


class Organization(models.Model):
	name = models.CharField(max_length=50)
	country = models.CharField(max_length=20)
	address = models.TextField()
	email = models.EmailField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

	def __str__(self):
		return self.name

class Certificate(models.Model):
	title = models.CharField(max_length=120)
	date = models.DateField()
	line_no = models.IntegerField(max_length=120)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

	def __str__(self):
		return self.title
# Create your models here.
class Course(models.Model):
	organization = models.ForeignKey(Organization, null=True)
	certificate = models.OneToOneField(Certificate, blank=True, null=True)
	title = models.CharField(max_length=120)
	slug = models.SlugField(null=True, blank=True)
	short_description = models.TextField()
	description = models.TextField()
	level = models.CharField(max_length=50)
	speaking_language = models.CharField(max_length=50)
	transcript_language =models.CharField(max_length=50)
	media = models.ImageField(blank=True, 
			null=True, 
			upload_to=download_media_location,
			storage=FileSystemStorage(location=settings.PROTECTED_ROOT))
	starting_date = models.DateField()
	ending_date = models.DateField(null=True, blank=True)
	active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)


	def __str__(self):
		return self.title




class TaggedItem(models.Model):
	course = models.ForeignKey(Course)
	tag = models.CharField(max_length=20)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)
	

	def __str__(self):
		return self.tag


class Prerequisite(models.Model):
	course = models.ManyToManyField(Course)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)


class Syllabus(models.Model):
	course = models.ForeignKey(Course)
	title = models.CharField(max_length=120)
	short_description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

	def __str__(self):
		return self.title

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


class Lecturer(models.Model):
	course = models.ManyToManyField(Course)
	name = models.CharField(max_length=120)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

	def __str__(self):
		return self.name





class Enrollment(models.Model):
	#user
	course = models.ForeignKey(Course)
	enrollment_start = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
	enrollment_end = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

	def __str__(self):
		return self.title


class Review(models.Model):
	#user
	course = models.ForeignKey(Course)
	rating = models.IntegerField(null=True, blank=True)
	testimony = models.TextField()
	date = models.DateTimeField()
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

	def __str__(self):
		return "%s" %(self.rating)


def thumbnail_location(instance, filename):
	return "%s/%s" %(instance.product.slug, filename)

THUMB_CHOICES = (
	("hd", "HD"),
	("sd", "SD"),
	("micro", "Micro"),
)

class Thumbnail(models.Model):
	course = models.ForeignKey(Course) #instance.product.title
	type = models.CharField(max_length=20, choices=THUMB_CHOICES, default='hd')
	height = models.CharField(max_length=20, null=True, blank=True)
	width = models.CharField(max_length=20, null=True, blank=True) 
	media = models.ImageField(
		width_field = "width",
		height_field = "height",
		blank=True, 
		null=True, 
		upload_to=thumbnail_location)

	def __unicode__(self): # __str__(self):
		return str(self.media.path)


import os
import shutil
from PIL import Image
import random

from django.core.files import File


def create_new_thumb(media_path, instance, owner_slug, max_length, max_width):
		filename = os.path.basename(media_path)
		thumb = Image.open(media_path)
		size = (max_length, max_width)
		thumb.thumbnail(size, Image.ANTIALIAS)
		temp_loc = "%s/%s/tmp" %(settings.MEDIA_ROOT, owner_slug)
		if not os.path.exists(temp_loc):
			os.makedirs(temp_loc)
		temp_file_path = os.path.join(temp_loc, filename)
		if os.path.exists(temp_file_path):
			temp_path = os.path.join(temp_loc, "%s" %(random.random()))
			os.makedirs(temp_path)
			temp_file_path = os.path.join(temp_path, filename)

		temp_image = open(temp_file_path, "w")
		thumb.save(temp_image)
		thumb_data = open(temp_file_path, "r")

		thumb_file = File(thumb_data)
		instance.media.save(filename, thumb_file)
		shutil.rmtree(temp_loc, ignore_errors=True)
		return True







