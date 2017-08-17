from django.shortcuts import redirect, render
from django.http import HttpResponse 
from evo.models import EvoUser, StatusStudent
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url = '/evo/login/')
def is_student(request):
	user = request.user
	if user.evouser.account_type =='s':
		return True
	else:
		return False

#redirect student a/c to his status
@login_required(login_url = '/evo/login/')
def student_dashboard(request):
	if is_student(request):		
		try:
			status  = StatusStudent.objects.get(student = request.user)
			if status.admission == False:
				return redirect('student_welcome')
			else:
				template_name = 'evo/dashboard/student_dashboard.html'
				context= {
					'user':request.user,
				}
				return render(request, template_name, context)


		except StatusStudent.DoesNotExist:
			return HttpResponse("Sorry Something Went Wrong Contact Administration")

	else:
		return HttpResponse("Sorry You Can't Access This Page")


@login_required(login_url = '/evo/login/')
def student_welcome(request):
	if is_student(request):
		template_name ='evo/admission/welcome.html'
		context = {
			'user':request.user,
		}
		return render(request, template_name, context)
	else:
		return HttpResponse("Sorry You Can't Access This Page")


#Same For All Views
"""
@login_required(login_url = '/evo/login/')
def student_welcome(request):
	if is_student(request):
		return HttpResponse('Welcome USer')
	else:
		return HttpResponse("Sorry You Can't Access This Page")
"""