from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify






def download_media_location(instance, filename):
	return "%s/%s" %(instance.slug, filename)

def download_media_profile_location(instance, filename):
	return "%s/%s" %(instance.name, filename)


class Institution(models.Model):
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
	line_no = models.IntegerField()
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

	def __str__(self):
		return self.title


		
class Course(models.Model):
	user = models.ManyToManyField(settings.AUTH_USER_MODEL)
	institution = models.ForeignKey(Institution, null=True, blank=True)
	certificate = models.OneToOneField(Certificate, blank=True, null=True)
	course_id = models.CharField(max_length=50, null=True, blank=True)
	embed_code = models.CharField(max_length=500, null=True, blank=True)
	title = models.CharField(max_length=120, null=True, blank=True)
	slug = models.CharField(null=True, blank=True, max_length=120,)
	short_description = models.TextField(null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	price = models.IntegerField( null=True, blank=True)
	length_course = models.IntegerField(null=True, blank=True)
	effort = models.CharField(max_length=120, null=True, blank=True)
	video_transcript = models.CharField(max_length=120, null=True, blank=True)
	level = models.CharField(max_length=50,  null=True, blank=True)
	speaking_language = models.CharField(max_length=50, null=True, blank=True)
	transcript_language =models.CharField(max_length=50, null=True, blank=True)
	subject = models.CharField(max_length=50, null=True, blank=True)
	media = models.ImageField(blank=True, 
			null=True, 
			upload_to=download_media_location,
			storage=FileSystemStorage(location=settings.PROTECTED_ROOT))
	starting_date = models.DateTimeField(null=True, blank=True)
	ending_date = models.DateField(null=True, blank=True)
	active = models.BooleanField(default=True)
	enrollment_start = models.DateTimeField(blank=True, null=True)
	enrollment_end = models.DateTimeField(blank=True, null=True)
	number = models.CharField(max_length=20, blank=True, null=True)
	start_display = models.DateField( blank=True, null=True)
	start_type = models.CharField(max_length=20, blank=True, null=True)
	pacing = models.CharField(max_length=50, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)


	def __str__(self):
		return self.title





class Lecturer(models.Model):
	
	course = models.ManyToManyField(Course)
	name = models.CharField(max_length=120)
	media = models.ImageField(blank=True, 
			null=True, 
			upload_to=download_media_profile_location,
			storage=FileSystemStorage(location=settings.PROTECTED_ROOT))
	occupation = models.CharField(max_length=120, null=True)
	title_degree = models.CharField(max_length=10, null=True)
	org = models.CharField(max_length=10, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

	def __str__(self):
		return self.name

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



class ObjectiveCourse(models.Model):
	course = models.ForeignKey(Course)
	what_you_learn = models.CharField(max_length=120)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)


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

	def __str__(self): # __str__(self):
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


# def course_post_save_receiver(sender, instance, created, *args, **kwargs):
# 	if instance.media:
# 		hd, hd_created = Thumbnail.objects.get_or_create(course=instance, type='hd')
# 		sd, sd_created = Thumbnail.objects.get_or_create(course=instance, type='sd')
# 		micro, micro_created = Thumbnail.objects.get_or_create(course=instance, type='micro')

# 		hd_max = (500, 500)
# 		sd_max = (350, 350)
# 		micro_max = (150, 150)

# 		media_path = instance.media.path
# 		owner_slug = instance.slug
# 		if hd_created:
# 			create_new_thumb(media_path, hd, owner_slug, hd_max[0], hd_max[1])
# 			# filename = os.path.basename(instance.media.path)
# 			# thumb = Image.open(instance.media.path)
# 			# thumb.thumbnail(hd_max, Image.ANTIALIAS)
# 			# temp_loc = "%s/%s/tmp" %(settings.MEDIA_ROOT, instance.slug)
# 			# if not os.path.exists(temp_loc):
# 			# 	os.makedirs(temp_loc)
# 			# temp_file_path = os.path.join(temp_loc, filename)
# 			# if os.path.exists(temp_file_path):
# 			# 	temp_path = os.path.join(temp_loc, "%s" %(random.random()))
# 			# 	os.makedirs(temp_path)
# 			# 	temp_file_path = os.path.join(temp_path, filename)

# 			# temp_image = open(temp_file_path, "w")
# 			# thumb.save(temp_image)
# 			# thumb_data = open(temp_file_path, "r")

# 			# thumb_file = File(thumb_data)
# 			# hd.media.save(filename, thumb_file)
		
# 		if sd_created:
# 			create_new_thumb(media_path, sd, owner_slug, sd_max[0], sd_max[1])

# 		if micro_created:
# 			create_new_thumb(media_path, micro, owner_slug, micro_max[0], micro_max[1])
# 	post_save.connect(course_post_save_receiver, sender=Course)


# def create_slug(instance, new_slug=None):
# 	slug = slugify(instance.title)
# 	if new_slug is not None:
# 		slug = new_slug
# 	qs = Course.objects.filter(slug=slug)
# 	exists = qs.exists()
# 	if exists:
# 		new_slug = "%s-%s" %(slug, qs.first().id)
# 		return create_slug(instance, new_slug=new_slug)
# 	return slug


# def course_pre_save_receiver(sender, instance, *args, **kwargs):
# 	if not instance.slug:
# 		instance.slug = create_slug(instance)
		
# pre_save.connect(course_pre_save_receiver, sender=Course)

class DumpJSON(models.Model):
	
	endpoint_api = models.CharField(max_length=500, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

	def __str__(self):
		return self.endpoint_api