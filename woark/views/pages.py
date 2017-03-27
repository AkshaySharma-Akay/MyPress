from django.shortcuts import render, redirect
from django.http import HttpResponse
from woark.models import Site, SiteContact, SiteSocialProfile, Menu, MenuItem,ThemeInfo
from woark.models import Blog

def home(request):
	template_name = 'woark/pages/home.html'
	context = {
		'site': Site.objects.get(id='1'),
		'site_contact': SiteContact.objects.all(),
		'site_social_profile': SiteSocialProfile.objects.all(),
		'header_menu': MenuItem.objects.filter(menu__name = 'Header Menu'),
		'themeinfo':ThemeInfo.objects.get(title = 'Woark'),
		}
	return render(request, template_name, context)

