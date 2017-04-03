from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
	title = models.CharField(max_length=500)
	description = models.TextField(max_length = 2000)
	started_on = models.DateTimeField(auto_now_add = True)
	updated_on = models.DateTimeField(auto_now = True)
	years = models.DurationField()
	semesters = models.PositiveSmallIntegerField()

	def __str__(self):
		return ("Course : ", str(title))

class Subject(models.Model):
	courses = models.ManyToManyField(Course)
	title = models.CharField(max_length=500)
	description = models.TextField(max_length = 5000)
	introduced_on = models.DateTimeField(auto_now_add = True)
	updated_on = models.DateTimeField(auto_now = True)
	creditpoints = models.PositiveSmallIntegerField()

	def __str__(self):
		return ("Subject: " + self.subject_id + " ." + self.title + " : " + str(creditpoints))

class Semester(models.Model):
	course = models.OneToOneField(Course)
	semester_count = models.PositiveSmallIntegerField()
	course = models.OneToOneField(Course)
	subjects = models.ManyToManyField(Subject)

class Student(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	course = models.OneToOneField(Course)
	current_semester = models.PositiveSmallIntegerField(blank=True, default=1)
	enrolled_on = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return (str(self.user.username) + " : "+ str(self.course.title) + " : "+ str(self.current_semester))

class Tutor(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	subjects = models.ManyToManyField(Subject)



