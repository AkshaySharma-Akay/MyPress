from django.conf.urls import url
from . import views

#urlpatterns 
urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^blog/$', views.blog , name='blog'),

	#blogs
	url(r'^blog/(?P<blog_id>[0-9]+)/$', views.get_blog, name='get_blog'),
	url(r'^blog/(?P<blog_id>[0-9]+)/pack/(?P<pack_count>[0-9]+)/$', views.get_blog_pack, name='get_blog_pack'),

	#articles
	url(r'^blog/(?P<blog_id>[0-9]+)/(?P<article_id>[0-9]+)/$',views.get_article, name='get_article'),

	#tags
	url(r'^blog/(?P<blog_id>[0-9]+)/tags/$', views.get_tags, name = 'get_tags'),

	url(r'^blog/(?P<blog_id>[0-9]+)/tag/(?P<tag_id>[0-9]+)/(?P<pack_count>[0-9]+)/$', views.get_tag_pack, name = 'get_tag_pack'),
]