from django.conf.urls import url
from . import views

#urlpatterns 
urlpatterns = [
	url(r'^$',views.home, name='home'),
	url(r'^blog/(?P<blog_id>[0-9]+)/$', views.get_blog, name='get_blog'),
	url(r'^blog/(?P<blog_id>[0-9]+)/pack/(?P<pack_count>[0-9]+)/$', views.get_blog_pack, name='get_blog_pack'),
	url(r'^blog/(?P<blog_id>[0-9]+)/(?P<article_id>[0-9]+)/$',views.get_article, name='get_article'),

	#pages link 
	#url(r'^aboutus/$',views.aboutus, name='aboutus'),
	#url(r'^contactus/$', views.contactus, name='contactus'),
	
]