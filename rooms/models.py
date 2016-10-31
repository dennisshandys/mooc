from django.db import models
from django.conf import settings
from accounts.models import MyUser, UserProfile
from courses.models import Course
# Create your models here.

TIME_CHOICES = (
	("08:00-09:30 AM", "08:00-09:30 AM"),
	("09:30-11:00 AM", "09:30-11:00 AM"),
	("11:00-12:30 PM", "11:00-12:30 PM"),
	("12:30-02:00 PM", "12:30-02:00 PM"),
	("02:00-03:30 PM", "02:00-03:30 PM"),
	("03:30-05:00 PM", "03:30-05:00 PM"),
	("05:00-06:30 PM", "05:00-06:30 PM"),
	("06:30-08:00 PM", "06:30-08:00 PM"),
	("08:00-09:30 PM", "08:00-09:30 PM"),
	("09:30-11:00 PM", "09:30-11:00 PM"),
)

DAY_CHOICES = (
	("Sunday", "Sunday"),
	("Monday", "Monday"),
	("Tuesday", "Tuesday"),
	("Wednesday", "Wednesday"),
	("Thursday", "Thursday"),
	("Friday", "Friday"),
	("Saturday", "Saturday"),
)
class CoachingCircle(models.Model):
	
	course = models.ForeignKey(Course)
	user = models.ManyToManyField(UserProfile)
	name = models.CharField(max_length=50, blank=True, null=True)
	room_number = models.IntegerField()
	time_available = models.CharField(choices=TIME_CHOICES, max_length=50, blank=True, null=True)
	day_available = models.CharField(choices=DAY_CHOICES, max_length=50, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

	def __str__(self):
		return self.name