from django.conf.urls import url


from .views import (
    CourseCreateAPIView,
    CourseDeleteAPIView,
    CourseDetailAPIView,
    CourseListAPIView,
    CourseUpdateAPIView,
    )

urlpatterns = [
    url(r'^$', CourseListAPIView.as_view(), name='list'),
    url(r'^create/$', CourseCreateAPIView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', CourseDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', CourseUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', CourseDeleteAPIView.as_view(), name='delete'),
]
