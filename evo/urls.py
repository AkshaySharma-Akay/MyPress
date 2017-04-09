from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^login/$',views.signin, name='signin'),
	url(r'^signup/$',views.signup, name='signup'),
	url(r'^tutor/dashboard/$', views.tutor_dashboard, name='tutor_dashboard'),
	url(r'^student/dashboard/$', views.student_dashboard, name='student_dashboard'),
	url(r'^deo/dashboard/$', views.deo_dashboard, name='deo_dashboard'),
]