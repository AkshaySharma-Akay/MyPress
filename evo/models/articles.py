from django.db import models
from django.contrib.auth.models import User


#Note: These Models Are Different From That in woark app
#To Be Used for official articles only
class EvoArticleTag(models.Model):
	title = models.CharField(max_length=50)
	def __str__(self):
		return ("Tag : " + self.title)

class EvoArticle(models.Model):
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	title = models.CharField(max_length=150)
	created_on = models.DateTimeField(auto_now_add = True)
	pub_date = models.DateTimeField(auto_now = True)
	content = models.TextField(max_length = 7000)
	tag = models.ManyToManyField(EvoArticleTag )

	def __str__(self):
		return ("Article : " + str(self.title))

