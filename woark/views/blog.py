from django.shortcuts import render
from woark.models import Article, ArticleContent

def blog(request):
	pass
	
def blog_article(request):
	pass

def get_article(request, article_id):
	template_name = 'woark/blog/get_article.html'
	context = {
		'article': Article.objects.get(id=article_id),
		'article_content': ArticleContent.objects.get(article = article_id),
		
	}

	return render(request, template_name, context)