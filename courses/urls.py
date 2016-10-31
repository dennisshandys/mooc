from django.conf.urls import url


from courses.api.views import (
   
    CourseDetailAPIView,
    )

urlpatterns = [
    
    url(r'^(?P<slug>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/info$', CourseDetailAPIView.as_view(), name='detail'),
    
]
