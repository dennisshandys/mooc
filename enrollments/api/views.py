from django.db.models import Q

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


from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

    )

from courses.models import Course
from enrollments.models import Enrollment

#Override Pagination class
from .pagination import EnrollmentLimitOffsetPagination, EnrollmentPageNumberPagination

#Override Hak Akses Permisiion to my API
#from .permissions import IsOwnerOrReadOnly

from .serializers import (
    
    EnrollmentListSerializer,
    EnrollmentDetailSerializer
    
    )

class EnrollmentListAPIView(ListAPIView):
    #Call Serializers
    serializer_class = EnrollmentListSerializer

    #Filter Option in List API
    filter_backends= [SearchFilter, OrderingFilter]
    permission_classes = [AllowAny]

    #Field yang ingin di filter
    search_fields = ['enrollment_end', 'enrollment_start', 'course']

    #To setting up paging pagination
    pagination_class = EnrollmentPageNumberPagination #PageNumberPagination

    #Override queryset
    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = Enrollment.objects.all() #filter(user=self.request.user)
        #Because it is CBV so u need keyword self
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(enrollment_end=query)|
                    Q(enrollment_start=query)|
                    Q(course__title__icontains=query)
                    ).distinct()
        return queryset_list

class EnrollmentDetailAPIView(RetrieveAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentListSerializer
    #Use Slug rather than PK in URL
    lookup_field = 'pk'

    #Tipe Permission yang diberikan
    permission_classes = [AllowAny]