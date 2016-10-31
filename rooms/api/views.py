from django.conf import settings
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from courses.models import Course
from rooms.models import CoachingCircle

#Override Hak Akses Permissions to my API
from .serializers import (
		CoachingCircleListSerializer,
	)

#This is for filter in RestFramework
from rest_framework.generics import (
		ListAPIView,
	)

from rest_framework.filters import (
		SearchFilter,
		OrderingFilter,
	)

from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,

    )

#Override Hak Akses Permissions to my API
from .serializers import (
		CoachingCircleListSerializer,
	)

class CoachingCircleListAPIView(ListAPIView):
	#Call Serializers
	serializer_class = CoachingCircleListSerializer

	#Filter Option in List API
	filter_backends = [SearchFilter, OrderingFilter]
	permission_classes = [IsAuthenticated]

	#Field yang ingin di filter
	search_fields = ['user__user__username', 'time_available', 'day_available', 'course__title']
	#filter_backends = (DjangoFilterBackend,)
	filter_backends = (DjangoFilterBackend,)
	filter_fields = ('day_available', 'time_available')
	#Override queryset
	def get_queryset(self, *args, **kwargs):
		# queryset_list = super(PostListAPIView,self).get_queryset(*args, **kwargs)
		if self.request.user.is_authenticated():
			queryset_list = CoachingCircle.objects.filter(user__user=self.request.user)
		else:
			queryset_list = CoachingCircle.objects.all()
		query = self.request.GET.get("q")
		if query:
			queryset_list = queryset_list.filter(
				Q(user__user__username__icontains=query)|
				Q(course__title__icontains=query)|
				Q(time_available__iexact=query)|
				Q(day_available__iexact=query)
				).distinct()

		return queryset_list