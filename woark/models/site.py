from django.db import models

class Site(models.Model):
	title = models.CharField(max_length=30)
	link = models.URLField(max_length=200, default='http://localhost')

	def __str__(self):
		return (self.title + " : " + self.link)

class SiteContact(models.Model):
	title = models.CharField(max_length=30)
	info = models.CharField(max_length=30)
	icon = models.CharField(max_length=15)
	link = models.URLField(max_length=200,blank=True)

	def __str__(self):
		return self.title

class SiteSocialProfile(models.Model):
	name = models.CharField(max_length=30)
	icon = models.CharField(max_length=15)
	link = models.URLField(max_length=200)

	def __str__(self):
		return (self.name + " : " + self.link)

class Menu(models.Model):
	name = models.CharField(max_length=40)

	def __str__(self):
		return self.name

class MenuItem(models.Model):
	menu = models.ManyToManyField(Menu)
	title = models.CharField(max_length=30)
	link = models.URLField(max_length=200)
	index = models.IntegerField(default=1)

	def __str__(self):
		return (str(self.index) + ". " +self.title)

	class Meta:
		ordering = ['index']

class ThemeInfo(models.Model):
	title = models.CharField(max_length=20)
	link = models.URLField(max_length = 200)
	dev = models.CharField(max_length=100)
	dev_link = models.URLField(max_length=200)

	def __str__(self):
		return (self.title + " By " + self.dev)