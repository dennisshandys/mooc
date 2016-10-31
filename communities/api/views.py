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

from communities.models import Hub

#Override Pagination class
from communities.api.pagination import HubFeaturedLimitOffsetPagination, HubFeaturedPageNumberPagination
from courses.api.pagination import CoursePageNumberPagination
#Override Hak Akses Permisiion to my API
from .permissions import IsOwnerOrReadOnly

from .serializers import (
    # CourseCreateUpdateSerializer,
    # CourseDetailSerializer,
    HubListSerializer,
    HubFeaturedListSerializer
    
    )


# class CourseCreateAPIView(CreateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseCreateUpdateSerializer
#     #permission_classes = [IsAuthenticated]

#     #Add user field not from Field Post, (Additionalsimilar like 'def perform_update)
#     # def perform_create(self, serializer):
#     #     serializer.save(user=self.request.user)

# class CourseUpdateAPIView(RetrieveUpdateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseCreateUpdateSerializer
#     lookup_field = 'slug'

#     #Tipe Permission yang diberikan
#     #permission_classes = [IsOwnerOrReadOnly]
#     #lookup_url_kwarg = "abc"

#     #Update user field not from Field Post, (Additional, similar like 'def perform_create')
#     def perform_update(self, serializer):
#         serializer.save(user=self.request.user)
#         #email send_email

# class CourseDeleteAPIView(DestroyAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseDetailSerializer
#     lookup_field = 'slug'
#     #permission_classes = [IsOwnerOrReadOnly]
#     #lookup_url_kwarg = "abc"

# class CourseDetailAPIView(RetrieveAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseDetailSerializer
#     #Use Slug rather than PK in URL
#     lookup_field = 'slug'

#     #Tipe Permission yang diberikan
#     permission_classes = [AllowAny]


class HubListAPIView(ListAPIView):
    #Call Serializers
    serializer_class = HubListSerializer

    #Filter Option in List API
    filter_backends= [SearchFilter, OrderingFilter]
    permission_classes = [AllowAny]

    #Field yang ingin di filter
    search_fields = ['title', ]

    #To setting up paging pagination
    pagination_class = CoursePageNumberPagination #PageNumberPagination

    #Override queryset
    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = Hub.objects.all() #filter(user=self.request.user)
        #Because it is CBV so u need keyword self
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(title__icontains=query)|
                    Q(user_member__username__icontains=query)
                    ).distinct()

        return queryset_list


class HubFeaturedListAPIView(ListAPIView):
    #Call Serializers
    serializer_class = HubFeaturedListSerializer

    #Filter Option in List API
    filter_backends= [SearchFilter, OrderingFilter]
    permission_classes = [AllowAny]

    #Field yang ingin di filter
    search_fields = ['title', ]

    #To setting up paging pagination
    pagination_class = HubFeaturedPageNumberPagination #PageNumberPagination

    #Override queryset
    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = Hub.objects.filter(is_featured=True).order_by('-created_at')[:4] #filter(user=self.request.user)

        return queryset_list


# class HubRecommendedListAPIView(ListAPIView):
#     #Call Serializers
#     serializer_class = HubRecommendedListSerializer

#     #Filter Option in List API
#     filter_backends= [SearchFilter, OrderingFilter]
#     permission_classes = [AllowAny]

#     #Field yang ingin di filter
#     search_fields = ['title', ]

#     #To setting up paging pagination
#     pagination_class = CoursePageNumberPagination #PageNumberPagination

#     #Override queryset
#     def get_queryset(self, *args, **kwargs):
#         #queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
#         queryset_list = Hub.objects.filter(is_featured=True).order_by('-created_at')[:4] #filter(user=self.request.user)

#         return queryset_list