from django.conf.urls import url
from . import views

#urlpatterns 
urlpatterns = [
	url(r'^$',views.home, name='home'),
	url(r'^blog/(?P<article_id>[0-9]+)/$',views.get_article, name='get_article'),
]