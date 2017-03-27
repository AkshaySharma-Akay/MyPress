from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from woark.models import Article, ArticleContent, Comment,Blog
from woark.forms import ArticleCommentForm
from woark.models import Site, SiteContact, SiteSocialProfile, Menu, MenuItem,ThemeInfo
from woark.models import ArticleTag


def blog(request):
	try:
		blogs = Blog.objects.all()
	except Blog.DoesNotExist:#test it whether it works when there is no data available
		return HttpResponse("Sorry There is no blog at the momment")

	template_name = 'woark/blog/blog.html'
	context = {
		'site': Site.objects.get(id='1'),
		'site_contact': SiteContact.objects.all(),
		'site_social_profile': SiteSocialProfile.objects.all(),
		'header_menu': MenuItem.objects.filter(menu__name = 'Header Menu'),
		'themeinfo':ThemeInfo.objects.get(title = 'Woark'),
		'blogs':blogs,
	}
	return render(request, template_name, context)


def get_article(request, blog_id, article_id):
	template_name = 'woark/blog/get_article.html'
	form = ArticleCommentForm()
	blog = Blog.objects.get(id=blog_id)
	article = blog.article_set.get(id=article_id)
	article = Article.objects.get(id=article_id)
	article_comment = article.comment.all().order_by('-pub_on')
	context = {
		'site': Site.objects.get(id='1'),
		'site_contact': SiteContact.objects.all(),
		'site_social_profile': SiteSocialProfile.objects.all(),
		'header_menu': MenuItem.objects.filter(menu__name = 'Header Menu'),
		'themeinfo':ThemeInfo.objects.get(title = 'Woark'),
		'article': article,
		'article_content': ArticleContent.objects.get(article = article_id),
		'c_form':form,
		'article_comment':article_comment,
	}
	formerror = ""
	if request.method == 'POST':
		if request.user.is_authenticated:
			if request.user.is_active:
				form = ArticleCommentForm(request.POST)
				if form.is_valid():
					comment = form.save(commit=False)
					comment.article = article
					comment.user = request.user
					comment.save()
				else:
					context['c_form']=form
			else:
				formerror = "Sorry Your Account Is Not Active"
		else:
			formerror = "Sorry Register First To Comment!"

		context['formerror'] = formerror

	return render(request, template_name, context)

#
# Note : woark/blog/index.html : Template is used for both the get_blog() and the get_blog_pack() views
#
def get_blog(request, blog_id):
	template_name = 'woark/blog/index.html'
	try:
		blog = Blog.objects.get(id=blog_id)
	except Blog.DoesNotExist:
		return HttpResponse("Sorry Blog Does Not Exists")

	return redirect('get_blog_pack',blog_id =blog_id, pack_count=1)


def get_blog_pack(request, blog_id, pack_count):
	#pack_count : the pack_count is the no. of the packet 
	#to be accessed 1st time, 2nd time or so on get it doc. is important
	template_name = "woark/blog/get_pack.html"
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


def get_tags(request, blog_id):
	"Show all the tags in a blog"
	blog = Blog.objects.get(id = blog_id)
	tags = blog.articletag_set.all()
	template_name = 'woark/blog/get_tags.html'
	context = {
		'site': Site.objects.get(id='1'),
		'site_contact': SiteContact.objects.all(),
		'site_social_profile': SiteSocialProfile.objects.all(),
		'header_menu': MenuItem.objects.filter(menu__name = 'Header Menu'),
		'themeinfo':ThemeInfo.objects.get(title = 'Woark'),
		'blog':blog,
		'tags':tags,
	}
	return render(request, template_name, context)
