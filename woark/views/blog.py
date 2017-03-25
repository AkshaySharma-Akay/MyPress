from django.shortcuts import render
from django.contrib.auth.models import User
from woark.models import Article, ArticleContent, Comment,Blog
from woark.forms import ArticleCommentForm
from woark.models import Site, SiteContact, SiteSocialProfile, Menu, MenuItem,ThemeInfo

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
