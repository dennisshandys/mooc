from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    )



class CourseLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 10

#Maximal data yang ditampilan dalam 1 page
class CoursePageNumberPagination(PageNumberPagination):
    page_size = 20
    