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

from accounts.models import MyUser


class MyUserDetailSerializer(ModelSerializer):
    class Meta:
        model = MyUser
        fields = [
            'username',
            'email',
        ]




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



class MyUserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    email = EmailField(label='Email Address')
    password = CharField(label='Password', 
        style={'input_type': 'password'})
    class Meta:
        model = MyUser
        fields = [
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
        if not email and not password:
            raise ValidationError("An Email and Password is required to login.")
        user = MyUser.objects.filter(email=email).distinct()
        user = user.exclude(email__isnull=True).exclude(email__iexact='')
        if user.exists() and user.count()==1:
            user_obj = user.first()
        else:
            raise ValidationError("This email is not valid")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect credentials, please try again")
        data["token"] = "SOME RANDOM TOKEN"
        return data


