from django.conf.urls import url


from communities.api.views import (
    # CourseCreateAPIView,
    # CourseDeleteAPIView,
    # CourseDetailAPIView,
    HubListAPIView,
    HubFeaturedListAPIView,
    # CourseUpdateAPIView,
    )

urlpatterns = [
    url(r'^$', HubListAPIView.as_view(), name='list'),
    url(r'^featured/$', HubFeaturedListAPIView.as_view(), name='list-featured'),
    # url(r'^create/$', CourseCreateAPIView.as_view(), name='create'),
    # url(r'^(?P<slug>[\w-]+)/$', CourseDetailAPIView.as_view(), name='detail'),
    # url(r'^(?P<slug>[\w-]+)/edit/$', CourseUpdateAPIView.as_view(), name='update'),
    # url(r'^(?P<slug>[\w-]+)/delete/$', CourseDeleteAPIView.as_view(), name='delete'),
]
