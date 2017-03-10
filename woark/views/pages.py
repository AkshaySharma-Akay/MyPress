from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return HttpResponse("Welcome To Woark, A Mini Content Management System for managing small websites")