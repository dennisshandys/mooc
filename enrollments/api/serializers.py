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



