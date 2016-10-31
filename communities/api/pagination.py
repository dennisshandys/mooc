from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    )



class HubFeaturedLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 10

#Maximal data yang ditampilan dalam 1 page
class HubFeaturedPageNumberPagination(PageNumberPagination):
    page_size = 4
    