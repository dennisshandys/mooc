import requests
from django.conf import settings
from django.db.models import Q
from django.contrib.auth import (get_user_model,
    authenticate, 
    login, logout)


from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView


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

from accounts.models import MyUser, UserProfile
from courses.api.permissions import IsOwnerOrReadOnly
from courses.api.pagination import CourseLimitOffsetPagination, CoursePageNumberPagination




from .serializers import (
    MyUserCreateSerializer,
    MyUserLoginSerializer,
    UserProfileListSerializer
    )

class UserProfileListAPIView(ListAPIView):
    serializer_class = UserProfileListSerializer
    queryset = UserProfile.objects.all()
    permission_classes = [AllowAny]

class MyUserCreateAPIView(CreateAPIView):
    serializer_class = MyUserCreateSerializer
    queryset = MyUser.objects.all()
    permission_classes = [AllowAny]



class MyUserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = MyUserLoginSerializer
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = MyUserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):

            new_data = serializer.data
            #SOME RANDOM TOKEN
            base_url = "http://192.168.1.97:8000/api/"

            login_url = base_url + "auth/token/"
            data_login = {
              "username": new_data['username'],
              "password": new_data['password']
            }
            login_r = requests.post(login_url, data=data_login)
            
            json_data = login_r.json()
            token = json_data["token"]
            new_data['token'] = token
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)





















