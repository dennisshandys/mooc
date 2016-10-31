from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
    )

#from accounts.api.serializers import UserDetailSerializer
from courses.models import Course
from reviews.models import Testimony

User = get_user_model()



def create_comment_serializer(user=None, slug=None):
    class CommentCreateSerializer(ModelSerializer):
        class Meta:
            model = Testimony
            fields = [
                'id',
                'rating',
                'review_text',
                'created_at',
            ]
        

        def create(self, validated_data):
        	if slug:
        		get_course = Course.objects.get(slug=slug)
        	else:
        		get_course = None
        	rating = validated_data.get("rating")
        	review_text = validated_data.get("review_text")
        	if user:
        		main_user = user
        	else:
        		main_user = User.objects.all().first()
        	testimony = Testimony(review_text=review_text,
            	rating=rating, course=get_course)
        	testimony.save()
        	return validated_data
    return CommentCreateSerializer

class CommentListSerializer(ModelSerializer):
    class Meta:
        model = Testimony
        fields = [
             'id',
             'user',
             'rating',
             'review_text',
             'created_at',
        ]
        