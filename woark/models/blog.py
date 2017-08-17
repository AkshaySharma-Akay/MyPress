from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
	"Model for creating / updating Blog"
	title = models.CharField(max_length=30)
	description = models.TextField(max_length = 150)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	created_by = models.ForeignKey(User, on_delete = models.CASCADE)

	def __str__(self):
		return (str(self.title) + " : " + str(self.description))

class ArticleTag(models.Model):
	title = models.CharField(max_length=50)
	blog = models.ManyToManyField(Blog)
	def __str__(self):
		return ("Tag : " + self.title)

class Article(models.Model):
	blog = models.ForeignKey(Blog, on_delete = models.CASCADE)
	author = models.ForeignKey(User, on_delete= models.CASCADE)
#main part
	title = models.CharField(max_length=100)
	article_image = models.ImageField(upload_to='article/' + str(id) + '/',default='')
#tag
	tag = models.ManyToManyField(ArticleTag)#on_delete what to do with article check that
#dates
	created_on = models.DateTimeField(auto_now_add = True)
	pub_date = models.DateTimeField(auto_now = True)

	def __str__(self):
		return ("Article : " + str(self.title) + " | Blog : " + str(self.blog.title))


class ArticleContent(models.Model):
	article = models.OneToOneField(Article, on_delete=models.CASCADE)
	plain_content = models.TextField(max_length = 5000)
	markup_content = models.TextField(max_length = 7000)

	def __str__(self):
		return("Article : " + self.article.title)


class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete = models.CASCADE, related_name='comment')
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	pub_on = models.DateTimeField(auto_now=True)
	added_on = models.DateTimeField(auto_now_add = True)
	content = models.TextField(max_length=700)

	def __str__(self):
		return("Comment: " + self.user.username + self.article.title)





