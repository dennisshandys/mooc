from rest_framework.serializers import (
	HyperlinkedIdentityField,
	ModelSerializer,
	SerializerMethodField,
	)
from rooms.models import CoachingCircle
from accounts.api.serializers import MyUserDetailSerializer, StudentListSerializer
from courses.models import Course

class CoachingCircleListSerializer(ModelSerializer):
	course = SerializerMethodField()
	user = StudentListSerializer(many=True)
	member_count = SerializerMethodField()
	
	class Meta:
		model = CoachingCircle
		fields = [
			'course',
			'user',
			'name',
			'room_number',
			'time_available',
			'day_available',
			'member_count',
			'created_at',
			'updated_at',
		]

	def get_course(self, obj):
		return obj.course.title

	def get_member_count(self, obj):
		return obj.user.all().count()
	

# class CoachingCircleDetailSerializer(ModelSerializer):
# 	class Meta:
