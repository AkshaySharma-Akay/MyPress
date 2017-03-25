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


def get_blog(request, blog_id):
	template_name = 'woark/blog/index.html'
	try:
		blog = Blog.objects.get(id=blog_id)
	except Blog.DoesNotExist:
		return HttpResponse("Sorry Blog Does Not Exists")

	article_pack = blog.article_set.all().order_by('-pub_date')[:3]
	context = {
		'site': Site.objects.get(id='1'),
		'site_contact': SiteContact.objects.all(),
		'site_social_profile': SiteSocialProfile.objects.all(),
		'header_menu': MenuItem.objects.filter(menu__name = 'Header Menu'),
		'themeinfo':ThemeInfo.objects.get(title = 'Woark'),
		'blog':blog,
		'article_pack':article_pack,
	}
	return render(request, template_name, context)

def get_blog_pack(request, blog_id, pack_count):

	template_name = "woark/blog/index.html"
	try:
		blog = Blog.objects.get(id=blog_id)
	except Blog.DoesNotExist:
		return HttpResponse("Sorry Blog Does Not Exists")


	article_count = 3 #no of articles per page
	pack_count = int(pack_count)	
	
	#negative pack_count change it to positive
	if(pack_count <= 0):
		pack_count = 1
	
	a = article_count * (pack_count - 1)
	b = a + article_count

	article_pack = blog.article_set.all().order_by('-pub_date')[a:b]
	context = {
		'site': Site.objects.get(id='1'),
		'site_contact': SiteContact.objects.all(),
		'site_social_profile': SiteSocialProfile.objects.all(),
		'header_menu': MenuItem.objects.filter(menu__name = 'Header Menu'),
		'themeinfo':ThemeInfo.objects.get(title = 'Woark'),
		'blog':blog,
		'article_pack':article_pack,
	}
	return render(request, template_name, context)
