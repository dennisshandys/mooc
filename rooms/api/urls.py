from django.conf.urls import url

from .views import (

	CoachingCircleListAPIView,
	)

urlpatterns = [
	url(r'^$', CoachingCircleListAPIView.as_view(), name='list'),
]