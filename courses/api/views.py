import datetime
from django.db.models import Q

#Override Pagination class
from .pagination import CourseLimitOffsetPagination, CoursePageNumberPagination

#Override Hak Akses Permisiion to my API
from .permissions import IsOwnerOrReadOnly

from .serializers import (
    CourseCreateUpdateSerializer,
    CourseDetailSerializer,
    CourseListSerializer,
    
    )

from courses.models import Course
from enrollments.models import Enrollment


#This is for filter in RestFramework
from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
    )
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView, 
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
    )
#Hak Akses Permisiion to my API
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

    )
from rest_framework.response import Response

from rest_framework.views import APIView


class MultipleFieldLookupMixin(object):
    """
    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.
    """
    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs[field]: # Ignore empty fields.
                filter[field] = self.kwargs[field]
        return get_object_or_404(queryset, **filter)  # Lookup the object

class CourseCreateAPIView(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseCreateUpdateSerializer
    #permission_classes = [IsAuthenticated]

    #Add user field not from Field Post, (Additionalsimilar like 'def perform_update)
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

class CourseUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseCreateUpdateSerializer
    lookup_field = 'slug'

    #Tipe Permission yang diberikan
    #permission_classes = [IsOwnerOrReadOnly]
    #lookup_url_kwarg = "abc"

    #Update user field not from Field Post, (Additional, similar like 'def perform_create')
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        #email send_email

class CourseDeleteAPIView(DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    lookup_field = 'slug'
    #permission_classes = [IsOwnerOrReadOnly]
    #lookup_url_kwarg = "abc"

class CourseDetailAPIView(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    #Use Slug rather than PK in URL
    lookup_field = 'slug'

    #Tipe Permission yang diberikan
    permission_classes = [AllowAny]

class CourseListAPIView(ListAPIView):
    #Call Serializers
    serializer_class = CourseListSerializer

    #Filter Option in List API
    filter_backends= [SearchFilter, OrderingFilter]
    permission_classes = [AllowAny]

    #Field yang ingin di filter
    search_fields = ['title', 'description',]

    #To setting up paging pagination
    pagination_class = CoursePageNumberPagination #PageNumberPagination

    #Override queryset
    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = Course.objects.all() #filter(user=self.request.user)
        #Because it is CBV so u need keyword self
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(title__iexact=query)|
                    Q(description__iexact=query)
                    ).distinct()

        return queryset_list

class CourseEnrolledAPI(APIView):
    permission_classes = [IsAuthenticated]
    # def get(self, request, format=None):
    #     data = self.get_checkout_data(user=request.user)
    #     return Response(data)

    def post(self, request, format=None, *args, **kwargs):
        data = {}
        
        slug = self.kwargs.get("slug")
        get_course = Course.objects.get(slug=slug)
        get_enrollment = Enrollment.objects.filter(course=get_course, user=request.user).count()

        
        if request.user.is_authenticated():
            if get_enrollment >= 1:
                data["enrollment_success"]= "Course has been enrolled"
            elif get_enrollment == 0: 
                new_enrollment = Enrollment()
                new_enrollment.user = request.user
                new_enrollment.course = get_course
                new_enrollment.agreement_marketing_mail = True
                new_enrollment.enrollment_start = datetime.datetime.now()
                new_enrollment.save()
                data["enrollment_success"]= True
        else:
            data["enrollment_success"]= False
        return Response(data)
