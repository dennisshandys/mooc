from django.conf.urls import url
from django.contrib import admin

from .views import (
    MyUserCreateAPIView,
    MyUserLoginAPIView
    )

urlpatterns = [
    url(r'^login/$', MyUserLoginAPIView.as_view(), name='login'),
    url(r'^register/$', MyUserCreateAPIView.as_view(), name='register'),
]
