import datetime
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField
    )
from rest_framework.reverse import reverse

from communities.models import Hub
from courses.models import (Course, Prerequisite,
    Syllabus, Certificate, Lecturer,)
from enrollments.models import Enrollment
from reviews.models import Testimony

#To Get Detail List URL
course_detail_url = HyperlinkedIdentityField(
        view_name='courses-api:detail',
        lookup_field='slug'
        )
course_edx_url = HyperlinkedIdentityField(
        view_name='courses:detail',
        lookup_field='slug'
        )

class EnrollUrlHyperlinkedIdentityField(HyperlinkedIdentityField):
    def get_url(self, obj, view_name, request, format):
        kwargs = {
            'slug': obj.slug,
        }
        return reverse(view_name, kwargs=kwargs, request=request, format=format)

class SyllabusSerializer(ModelSerializer):
    class Meta:
        model = Syllabus
        fields = [
            
            "title",
            "short_description",
        ]

class CertificateSerializer(ModelSerializer):
    class Meta:
        model = Certificate
        fields = [
            
            "title",
            "description",
        ]

class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Testimony
        fields = [
            
            "rating",
            "review_text",
            "created_at",
        ]

class LecturerSerializer(ModelSerializer):
    class Meta:
        model = Lecturer
        fields = [
            
            "name",
            "media",
            "org",
            "occupation",
            "created_at",
        ]
class CourseCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'title',
            'embed_code',
            'slug',
            'short_description',
            'description',
            'price',
            'length_course',
            'effort',
            'video_transcript',
            'level',
            'speaking_language',
            'transcript_language',
            'subject',
            'media',
            'starting_date',
            'ending_date',
            'active',
            'institution',
            'certificate',
            'created_at',
            'updated_at',
        ]



class CourseListSerializer(ModelSerializer):
    institution = SerializerMethodField()
    certificate = SerializerMethodField()
    hub_count_set = SerializerMethodField()
    #media = SerializerMethodField()
    
    url = course_detail_url
    edx_url = course_edx_url
    enroll_url = EnrollUrlHyperlinkedIdentityField("courses-api:enrolled")
    class Meta:
        model = Course
        fields = [
            'url',
            'edx_url',
            'enroll_url',
            'embed_code',
            'media',
            'title',
            'course_id',
            'starting_date',
            'slug',
            'short_description',
            'price',
            'institution',
            'certificate',
            'hub_count_set',
            'enrollment_start',
            'enrollment_end',
            'created_at',
            'updated_at',
        ]


    def get_hub_count_set(self, obj):
        return Hub.objects.filter(related_course=obj.id).count()

    def get_institution(self, obj):
        if obj.institution:
            return obj.institution.name
        else:
            return None

    def get_media(self, obj):
        try:
            media = obj.media.url
        except:
            media = None
        return media

    def get_certificate(self, obj):
        try:
            certificate = obj.certificate.title
        except:
            certificate = None
        return certificate


class CourseDetailSerializer(ModelSerializer):
    institution = SerializerMethodField()
    certificate = CertificateSerializer(read_only=True)
    syllabus_set = SyllabusSerializer(many=True, read_only=True)
    testimony_set = ReviewSerializer(many=True, read_only=True)
    lecturer_set = LecturerSerializer(many=True, read_only=True)
    enroll_url = EnrollUrlHyperlinkedIdentityField("courses-api:enrolled")
    #media = SerializerMethodField()
    # prerequisite = SerializerMethodField()
    class Meta:
        model = Course
        fields = [
            'enroll_url',
            'title',
            'embed_code',
            'slug',
            'short_description',
            'description',
            'price',
            'length_course',
            'effort',
            'video_transcript',
            'level',
            'speaking_language',
            'transcript_language',
            'subject',
            'media',
            'starting_date',
            'ending_date',
            'active',
            'institution',
            'certificate',
            'syllabus_set',
            'testimony_set',
            'lecturer_set',
            # 'prerequisite',
            'enrollment_start',
            'enrollment_end',
            'created_at',
            'updated_at',
        ]
    

    def get_institution(self, obj):
        if obj.institution:
            return obj.institution.name
        else:
            return None

    def get_lecturer(self, obj):
        if obj.lecturer:
            return obj.lecturer.name
        else:
            return None
    def get_media(self, obj):
        try:
            media = obj.media.url
        except:
            media = None
        return media

    def get_certificate(self, obj):
        try:
            certificate = obj.certificate.title
        except:
            certificate = None
        return certificate

    def create(self, validated_data):
        title = validated_data["title"]
        Product.objects.get(title=title)
        product = Product.objects.create(**validated_data)
        return product

    # def get_prerequisite(self, obj):
    #     try:
    #         prerequisite = obj.prerequisite_set.all()
    #     except:
    #         prerequisite = None
    #     return prerequisite


