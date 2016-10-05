from django.conf.urls import url


from .views import (
    # EnrollmentCreateAPIView,
    # EnrollmentDeleteAPIView,
    EnrollmentDetailAPIView,
    EnrollmentListAPIView,
    # EnrollmentUpdateAPIView,
    )

urlpatterns = [
    url(r'^$', EnrollmentListAPIView.as_view(), name='list'),
    # url(r'^create/$', CourseCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>[\w-]+)/$', EnrollmentDetailAPIView.as_view(), name='detail'),
    # url(r'^(?P<slug>[\w-]+)/edit/$', CourseUpdateAPIView.as_view(), name='update'),
    # url(r'^(?P<slug>[\w-]+)/delete/$', CourseDeleteAPIView.as_view(), name='delete'),
]
