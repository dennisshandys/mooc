import datetime
import requests
from django.conf import settings
from django.contrib.contenttypes.models import ContentType



from rest_framework.serializers import (
    CharField,
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
    )

from accounts.models import (MyUser, UserProfile,
    )
from rooms.models import CoachingCircle


class MyUserDetailSerializer(ModelSerializer):
    class Meta:
        model = MyUser
        fields = [
            'username',
            'email',
        ]
class StudentListSerializer(ModelSerializer):
    username = SerializerMethodField()
    #member_count = SerializerMethodField()
    class Meta:
        model = UserProfile
        fields = [
            'image_profile',
            'username',
            'country',
            'city',
            #'member_count',
        ]

    def get_username(self, obj):
        return obj.user.username

    # def get_member_count(self, obj):
    #     members = CoachingCircle.objects.filter(user=obj.user).count()
    #     return members

class UserProfileListSerializer(ModelSerializer):
    user = MyUserDetailSerializer(read_only=True)
    current_time = SerializerMethodField()
    class Meta:
        model = UserProfile
        fields = [
            'user',
            'country',
            'current_time',
            'preferred_language',
        ]

    def get_current_time(self, obj):
        return datetime.datetime.now()

class MyUserCreateSerializer(ModelSerializer):
    password = CharField(label='Password', 
        style={'input_type': 'password'})
    password2 = CharField(label='Confirm password',
        style={'input_type': 'password'})
    class Meta:
        model = MyUser
        fields = [
            'username',
            'email',
            'password',
            'password2',
            
        ]
        extra_kwargs = {"password":
                            {"write_only": True},
                        "password2":
                            {"write_only": True},
                            }
    def validate(self, data):
        email = data['email']
        user_qs = MyUser.objects.filter(email=email)
        if user_qs.exists():
            raise ValidationError("This user has already registered.")
        return data


    def validate_password(self, value):
        data = self.get_initial()
        password = data.get("password")
        password2 = value
        if password != password2:
            raise ValidationError("Passwords must match.")
        
        # user_qs = User.objects.filter(email=email2)
        # if user_qs.exists():
        #     raise ValidationError("This user has already registered.")

        return value

    def validate_password2(self, value):
        data = self.get_initial()
        password = data.get("password")
        password2 = value
        if password != password2:
            raise ValidationError("Passwords must match.")
        return value



    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = MyUser(
                username = username,
                email = email
            )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data



#products_url = base_url + "products/"

class MyUserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    email = EmailField(label='Email Address')
    password = CharField(label='Password', 
        style={'input_type': 'password'})
    username = CharField(label="Username", allow_blank=True, read_only=True)
    class Meta:
        model = MyUser
        fields = [
            'username',
            'email',
            'password',
            'token',
            
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                            }
    def validate(self, data):
        user_obj = None
        email = data.get("email")
        password = data.get("password")
        token = data.get("token")
        if not email and not password:
            raise ValidationError("An Email and Password is required to login.")
        user = MyUser.objects.filter(email=email).distinct()
        username = user.first().username
        user = user.exclude(email__isnull=True).exclude(email__iexact='')
        if user.exists() and user.count()==1:
            user_obj = user.first()
            
        else:
            raise ValidationError("This email is not valid")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect credentials, please try again")
        data["username"] = username
        return data


