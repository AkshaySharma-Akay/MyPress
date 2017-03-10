from django.conf.urls import url
from . import views

#urlpatterns 
urlpatterns = [
	url(r'^$',views.home, name='home'),
]