from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^evo/$',views.evo_index, name='evo_index'),
	url(r'^evo/login/$',views.signin, name='signin'),
]