"""mooc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include('smuggler.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/auth/token/$', 'rest_framework_jwt.views.obtain_jwt_token', name='auth_login_api'),
    url(r'^api/auth/token/refresh/$', 'rest_framework_jwt.views.refresh_jwt_token', name='refresh_token_api'),
    url(r'^api/courses/', include("courses.api.urls", namespace='courses-api')),
    url(r'^api/communities/', include("communities.api.urls", namespace='communities-api')),
    url(r'^api/enrollments/', include("enrollments.api.urls", namespace='enrollments-api')),
    url(r'^api/reviews/', include("reviews.api.urls", namespace='reviews-api')),
    url(r'^api/rooms/', include("rooms.api.urls", namespace='rooms-api')),
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/users/', include("accounts.api.urls", namespace='users-api')),
    url(r'^courses/', include("courses.urls", namespace='courses')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.PROTECTED_ROOT) 
