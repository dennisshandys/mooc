from django.contrib import admin

from .models import( 
Course, Institution,
 Certificate, Prerequisite,

 )
# Register your models here.

admin.site.register(Course)
admin.site.register(Institution)
admin.site.register(Certificate)
admin.site.register(Prerequisite)