from django.db.models import Q
from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
    )

from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView, 
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
    )
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

    )
from django.shortcuts import render
from .serializers import (
    CommentListSerializer,
    create_comment_serializer
    )
from courses.api.pagination import CoursePageNumberPagination
from reviews.models import Testimony


# Create your views here.
class CommentCreateAPIView(CreateAPIView):
    queryset = Testimony.objects.all()
    #serializer_class = PostCreateUpdateSerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        slug = self.request.GET.get("slug")
        return create_comment_serializer(
                user=self.request.user,
                slug = slug

                )
class CommentListAPIView(ListAPIView):
    serializer_class = CommentListSerializer
    permission_classes = [AllowAny]
    filter_backends= [SearchFilter, OrderingFilter]
    search_fields = ['review_text', 'user__first_name']
    pagination_class = CoursePageNumberPagination #PageNumberPagination

    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = Testimony.objects.filter(id__gte=0) #filter(user=self.request.user)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(review_text=query)|
                    Q(user__first_name__icontains=query) |
                    Q(user__last_name__icontains=query)
                    ).distinct()
        return queryset_list