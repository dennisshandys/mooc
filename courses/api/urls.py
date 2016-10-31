from django.conf.urls import url


from .views import (
    CourseCreateAPIView,
    CourseDeleteAPIView,
    CourseDetailAPIView,
    CourseEnrolledAPI,
    CourseListAPIView,
    CourseUpdateAPIView,

    )

urlpatterns = [
    url(r'^$', CourseListAPIView.as_view(), name='list'),
    url(r'^create/$', CourseCreateAPIView.as_view(), name='create'),
    url(r'^(?P<slug>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/info$', CourseDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<slug>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/enrolled/$', CourseEnrolledAPI.as_view(), name='enrolled'),
    url(r'^(?P<slug>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/edit/$', CourseUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<slug>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/delete/$', CourseDeleteAPIView.as_view(), name='delete'),
    
   
]
