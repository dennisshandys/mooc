from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField
    )
from accounts.models import UserProfile
from communities.models import Hub

#To Get Detail List URL
hub_detail_url = HyperlinkedIdentityField(
        view_name='hub-api:detail',
        lookup_field='slug'
        )

# class CourseCreateUpdateSerializer(ModelSerializer):
#     class Meta:
#         model = Hub
#         fields = [
#             'title',
#             'slug',
#             'short_description',
#             'description',
#             'price',
#             'length_course',
#             'effort',
#             'video_transcript',
#             'level',
#             'speaking_language',
#             'transcript_language',
#             'subject',
#             'media',
#             'starting_date',
#             'ending_date',
#             'active',
#             'institution',
#             'certificate',
#             'created_at',
#             'updated_at',
#         ]



class HubListSerializer(ModelSerializer):
    #url = hub_detail_url

    class Meta:
        model = Hub
        fields = [
            #'url',
            'user_owner',
            'user_member',
            'image_profile',
            'created_at',
            'updated_at',
        ]


class HubFeaturedListSerializer(ModelSerializer):
    #url = hub_detail_url
    count_userprofile_set = SerializerMethodField()
    class Meta:
        model = Hub
        fields = [
            #'url',
            'title',
            'user_owner',
            'count_userprofile_set',
            'image_profile',
            'created_at',
            'updated_at',
        ]

    def get_count_userprofile_set(self, obj):
        return obj.userprofile_set.count()

class HubRecomendedListSerializer(ModelSerializer):
    #url = hub_detail_url
    
    class Meta:
        model = Hub
        fields = [
            #'url',
            'title',
            'user_owner',
            'image_profile',
            'created_at',
            'updated_at',
        ]

    

# class CourseDetailSerializer(ModelSerializer):
#     institution = SerializerMethodField()
#     certificate = SerializerMethodField()
#     # prerequisite = SerializerMethodField()
#     class Meta:
#         model = Course
#         fields = [
#             'title',
#             'slug',
#             'short_description',
#             'description',
#             'price',
#             'length_course',
#             'effort',
#             'video_transcript',
#             'level',
#             'speaking_language',
#             'transcript_language',
#             'subject',
#             'media',
#             'starting_date',
#             'ending_date',
#             'active',
#             'institution',
#             'certificate',
#             # 'prerequisite',
#             'created_at',
#             'updated_at',
#         ]

#     def get_institution(self, obj):
#         return obj.institution.name

#     def get_certificate(self, obj):
#         try:
#             certificate = obj.certificate.title
#         except:
#             certificate = None
#         return certificate

    # def get_prerequisite(self, obj):
    #     try:
    #         prerequisite = obj.prerequisite_set.all()
    #     except:
    #         prerequisite = None
    #     return prerequisite


