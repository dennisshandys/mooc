import requests
import datetime
from django.http import Http404, HttpResponseRedirect
from django.contrib import admin
from django.utils import formats


from .models import( 
Course, Institution,
 Certificate, Prerequisite,
 Syllabus,Thumbnail,DumpJSON,
 Lecturer,

 )
# Register your models here.

admin.site.register(Course)
admin.site.register(Institution)
admin.site.register(Certificate)
admin.site.register(Prerequisite)
#admin.site.register(Lecturer)

admin.site.register(Syllabus)
admin.site.register(Thumbnail)
admin.site.register(Lecturer)

class DumpJSONAdmin(admin.ModelAdmin):
	list_display = ('endpoint_api',)
	

	
	def response_add(self, request, obj, post_url_continue=None):
		#api_endpoint = "http://192.168.1.242/api"
		api_secret_key = "0b19492a5f9271b5094b3a3c39c61acd1d377989"
		#end_point = "/enrollment/v1/enrollment"
		user = api_secret_key
		final_end_point = obj.endpoint_api
		headers = {'Authorization': 'Bearer 	0b19492a5f9271b5094b3a3c39c61acd1d377989'}
		params = {

		}
		r = requests.get(final_end_point)
		objects = r.json()["results"]
		
		for item in objects:
			get_course = Course.objects.filter(slug=item['course_id'],
				title=item['name']).count()
			if get_course >=1:
				pass
			elif get_course==0:
				new_course = Course()
				new_course.effort = item['effort']
				new_course.enrollment_start = item['enrollment_start']
				new_course.enrollment_end = item['enrollment_end']
				new_course.course_id = item['id']
				new_course.media = item['media']['image']['small']
				new_course.embed_code = item['media']['course_video']['uri']
				new_course.title = item['name']
				new_course.number = item['number']
				#new_course.institution = "MIT"
				new_course.short_description = item['short_description']
				new_course.starting_date = item['start']
				if item['start_display']:
					new_course.start_display = datetime.datetime.strptime(str(item['start_display']), '%b. %d, %Y').strftime('%Y-%m-%d')

				else:
					new_course.start_display = None
				new_course.start_type = item ['start_type']
				new_course.pacing = item ['pacing']
				
				new_course.slug = item['course_id']
				new_course.save()

			# if item['start_display']:
			# 	date = datetime.datetime.strptime(str(item['start_display']), '%b. %d, %Y').strftime('%Y-%m-%d')
				#date = item['start_display']
				#a = str(date).strftime("%Y-%m-%d")
				# print (item['start_display'])
				# print (date)
		return HttpResponseRedirect('http://localhost:8000/api/courses/')		

admin.site.register(DumpJSON,DumpJSONAdmin)