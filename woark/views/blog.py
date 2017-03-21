from django.shortcuts import render
from django.contrib.auth.models import User
from woark.models import Article, ArticleContent, Comment
from woark.forms import ArticleCommentForm

def blog(request):
	pass
	
def blog_article(request):
	pass

def get_article(request, article_id):
	template_name = 'woark/blog/get_article.html'
	form = ArticleCommentForm()
	article = Article.objects.get(id=article_id)
	article_comment = article.comment.all()
	context = {
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


