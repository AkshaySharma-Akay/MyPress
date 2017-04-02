from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator, MaxLengthValidator

#Choices List

ACCOUNT_TYPE=[
	['s','Student'],
	['t','Tutor'],
	['deo','Data Entry Operator'],
]

class EvoUser(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='account_type')
	account_type = models.CharField(max_length=3,choices=ACCOUNT_TYPE,default='s')

	def __str__(self):
		if(self.account_type == 't'):
			self.ac_type = "Tutor"
		elif(self.account_type == 'deo')
			self.ac_type = "Data Entry Operator"
		else:
			self.ac_type = "Student"
		return (self.user.username + " : " +self.ac_type)


