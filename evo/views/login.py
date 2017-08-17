from django.shortcuts import render,redirect, HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from evo.forms import SigninForm, SignupForm
from evo.models import EvoUser, StatusStudent



@login_required(login_url = '/student/login/')
def signinredirect(request):
	user = request.user
	try:
		ac_type = user.evouser.account_type
		if ac_type == 's':
			return redirect('student_dashboard')
		elif ac_type == 't':
			return redirect('tutor_dashboard')
		else:
			return HttpResponse("Sorry Your Account Is Not")
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
				context['form'] = form
				context['state'] = "Sorry Your Account is Not Active Contact Administration Please!"
		else:
			context['state'] = "Invalid Username or Password!"

	return render(request, template_name,context)



def signup(request):
	template_name = "evo/forms/signup.html"
	form = SignupForm()
	ac_type = EvoUser()
	status = StatusStudent()
	context = {'form':form}

	#Time to process the form data
	if (request.method == 'POST'):
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			email = form.cleaned_data['email']
			user.set_password(password)
			user.save()

			#set the account type to student
			ac_type.user = user
			ac_type.account_type = 's'
			ac_type.save()

			#set status of student
			status.student = user
			status.admission = False
			status.profile = False
			status.save()

			#login in the user
			user = authenticate(username=username,password=password)
			if user is not None:
				login(request,user)
				return redirect('/evo/login/')
		else:
			context['form'] = form

	context['form'] = form

	return render(request, template_name,context)

