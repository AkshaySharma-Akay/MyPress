from django.shortcuts import render,redirect, HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from evo.forms import SigninForm
from evo.models import EvoUser

@login_required(login_url = '/student/login/')
def signinredirect(request):
	user = request.user
	try:
		ac_type = user.evouser.account_type
		if ac_type == 's':
			return redirect('/student/')
		elif ac_type == 't':
			return redirect('/tutor/')
		elif ac_type == 'deo' :
			return redirect('/deo/')
		else:
			return("Sorry Your Account Is Not")
	except EvoUser.DoesNotExist:
		return HttpResponse("Sorry Your Account Type is not Defined, Please Contact Administration")
	return HttpResponse('Error')
		

#signin view
def signin(request):
	signinform = SigninForm()
	template_name='evo/forms/signin.html'
	logout(request)
	state=''
	context = {
		'form':signinform,
	}

	if (request.method == 'POST'):
		form = SigninForm(request.POST)
		username = request.POST.get('username','')
		email = request.POST.get('email','')
		password = request.POST.get('password','')
		user = auth.authenticate(username=username, password=password)

		if user is not None and user.is_active:
			if user.is_active:
				auth.login(request,user)
				return signinredirect(request)
			else:
				context['state'] = form.errors

		else:
			context['state'] = form.errors

	return render(request, template_name,context)





def evo_index(request):
	pass