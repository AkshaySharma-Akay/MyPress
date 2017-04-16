from django.shortcuts import render, redirect
from django.http import HttpResponse
from checkviews import *

@login_required(login_url = '/evo/login/')
def is_tutor(request):
	user = request.user
	if user.evouser.account_type == 't':
		return True
	else:
		return False

@login_required(login_url = '/evo/login/')
def tutor_dashboard(request):
	if is_tutor(request):
		return HttpResponse("Welcome Tutor")
	else:
		return HttpResponse("Sorry You Can't Access This Page.")