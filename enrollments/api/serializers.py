from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField
    )
from courses.api.serializers import CourseDetailSerializer
from enrollments.models import Enrollment


#To Get Detail List URL
enroll_detail_url = HyperlinkedIdentityField(
        view_name='enrollments-api:detail',
        lookup_field='pk',
        )


# class EnrollmentCreateUpdateSerializer(ModelSerializer):
#     course = SerializerMethodField()
#     class Meta:
#         model = Enrollment
#         fields = [
           
#         ]



class EnrollmentListSerializer(ModelSerializer):
    course = SerializerMethodField()
    url = enroll_detail_url

    class Meta:
        model = Enrollment
        fields = [
        'url',
        'course',
        'agreement_marketing_mail',
        'enrollment_start',
        'enrollment_end',
        ]

    def get_course(self, obj):
        return obj.course.title


class EnrollmentDetailSerializer(ModelSerializer):
    course = CourseDetailSerializer(read_only=True)
    

    class Meta:
        model = Enrollment
        fields = [
        'course',
        'agreement_marketing_mail',
        'enrollment_start',
        'enrollment_end',
        ]




# class CourseEnrollmentSerializer(ModelSerializer):
#     course = CharField(read_only=True)
#     user = EmailField(read_only=True)
#     enrollment_start = CharField(read_only=True)
#     enrollment_end = CharField(allow_blank=True, read_only=True)
#     class Meta:
#         model = Enrollment
#         fields = [
#             'course',
#             'user',
#             'enrollment_start',
#             'enrollment_end',
            
#         ]
        
#     def validate(self, data):
#         user_obj = None
#         email = data.get("email")
#         password = data.get("password")
#         if not email and not password:
#             raise ValidationError("An Email and Password is required to login.")
#         user = MyUser.objects.filter(email=email).distinct()
#         username = user.first().username
#         user = user.exclude(email__isnull=True).exclude(email__iexact='')
#         if user.exists() and user.count()==1:
#             user_obj = user.first()
            

#         else:
#             raise ValidationError("This email is not valid")

#         if user_obj:
#             if not user_obj.check_password(password):
#                 raise ValidationError("Incorrect credentials, please try again")
#         data["token"] = "SOME RANDOM TOKEN"
#         data["username"] = username
#         return data



