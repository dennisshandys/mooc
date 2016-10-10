from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField
    )

from courses.models import Course, Prerequisite


#To Get Detail List URL
course_detail_url = HyperlinkedIdentityField(
        view_name='courses-api:detail',
        lookup_field='slug'
        )


class CourseCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'title',
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
    url = course_detail_url

    class Meta:
        model = Course
        fields = [
            'url',
            'title',
            'course_id',
            'starting_date',
            'slug',
            'short_description',
            'price',
            'institution',
            'certificate',
            'created_at',
            'updated_at',
        ]

    def get_institution(self, obj):
        return obj.institution.name

    def get_certificate(self, obj):
        try:
            certificate = obj.certificate.title
        except:
            certificate = None
        return certificate


class CourseDetailSerializer(ModelSerializer):
    institution = SerializerMethodField()
    certificate = SerializerMethodField()
    # prerequisite = SerializerMethodField()
    class Meta:
        model = Course
        fields = [
            'title',
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
            # 'prerequisite',
            'created_at',
            'updated_at',
        ]

    def get_institution(self, obj):
        return obj.institution.name

    def get_certificate(self, obj):
        try:
            certificate = obj.certificate.title
        except:
            certificate = None
        return certificate

    # def get_prerequisite(self, obj):
    #     try:
    #         prerequisite = obj.prerequisite_set.all()
    #     except:
    #         prerequisite = None
    #     return prerequisite


