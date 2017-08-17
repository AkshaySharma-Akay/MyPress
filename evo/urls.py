from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.signin, name='signin'),
	url(r'^login/$',views.signin, name='signin'),
	url(r'^signup/$',views.signup, name='signup'),

	url(r'^tutor/dashboard/$', views.tutor_dashboard, name='tutor_dashboard'),

	#student urls
	url(r'^student/dashboard/$', views.student_dashboard, name='student_dashboard'),
	url(r'^student/welcome/$', views.student_welcome, name='student_welcome'),
	url(r'^admission/course/', views.admission_course ,name='admission_course'),
	url(r'^admission/add_course/(?P<course_id>[0-9]+)/', views.admission_add_course ,name='admission_add_course'),
	url(r'^admission/$', views.admission, name='admission'),
	url(r'^admission/basic/$', views.admission_basic, name='admission_basic'),
	url(r'^admission/address/$', views.admission_address, name='admission_address'),
	url(r'^admission/qualifications/$', views.admission_qualifications, name='admission_qualifications'),
	url(r'^admission/uploads/$', views.admission_uploads , name='admission_uploads'),
	url(r'^admission/terms/$', views.admission_terms , name='admission_terms'),
	url(r'^admission/finalsubmission/$', views.admission_final_submission , name='admission_final_submission'),

	#student conf
	url(r'^student/dashboard/confirmationpage/$', views.admission_confirm, name='admission_confirm'),
]