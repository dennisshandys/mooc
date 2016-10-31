from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models
from courses.models import Course



def download_media_location(instance, filename):
	return "%s/%s" %(instance.slug, filename)

# Create your models here.
class Hub(models.Model):
	user_owner = models.OneToOneField(settings.AUTH_USER_MODEL, null=True)
	title= models.CharField(null=True, max_length=120)
	slug = models.SlugField(null=True, blank=True)
	image_profile = models.ImageField(blank=True, 
			null=True, 
			upload_to=download_media_location,
			storage=FileSystemStorage(location=settings.PROTECTED_ROOT))
	dob = models.DateField()
	preferred_language = models.CharField(max_length=120, blank=True, null=True)
	address = models.TextField()
	city = models.CharField(max_length=120)
	country = models.CharField(max_length=120)
	zip_code = models.IntegerField( blank=True, null=True)
	interest = models.TextField( blank=True, null=True)
	title = models.CharField( max_length=100, blank=True, null=True)
	organization = models.TextField( blank=True, null=True)
	email = models.EmailField()
	phone = models.IntegerField()
	website = models.URLField( blank=True, null=True)
	about_me = models.TextField( blank=True, null=True)
	related_course = models.ForeignKey(Course,null=True, blank=True)
	is_featured = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)


	facebook_link = models.CharField(max_length=320, 
		null=True, 
		blank=True, 
		verbose_name='Facebook profile url')
	twitter_handle = models.CharField(max_length=320, 
		null=True, 
		blank=True, 
		verbose_name='Twitter handle')		


	def __str__(self):
		return self.title
