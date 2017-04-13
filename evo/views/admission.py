from django.shortcuts import render, redirect
from django.http import HttpResponse
from evo.models import Course, StatusStudent, StudentBasic, StudentAddress, StudentCourse
from evo.models import AdmissionStatus
from evo.forms import StudentBasicForm, StudentAddressForm
from django.contrib.auth.decorators import login_required


""" 
	CTRL + C and CTRL + V

if request.user.account_type
"""

def is_student(request):
	user = request.user
	if user.evouser.account_type == 's':
		return True
	else:
		return False

@login_required(login_url='evo/login/')
def admission(request):
	"Show the status of the student admission"
	if not(is_student(request)):
		return HttpResponse("Sorry You Can't Access This Page")

	#check if student's admission is already complete or not
	status = StatusStudent.objects.get(student=request.user)
	if status.admission == True:
		return redirect('student_dashboard')

	#if student selected the course show status else redirect to admission_course view
	try:
		course = request.user.studentcourse
		template_name = 'evo/admission/index.html'
		context = {
			'user':request.user,
			'course':course,
		}
		return render(request, template_name, context)

	except StudentCourse.DoesNotExist:
		return redirect('admission_course')



@login_required(login_url = 'evo/login/')
def admission_course(request):
	if not(is_student(request)):
		return HttpResponse("Sorry You Can't Access This Page")

	try:
		course = request.user.studentcourse
		return redirect('admission')

	except StudentCourse.DoesNotExist:
		template_name = 'evo/admission/course.html'
		context = {
			'user':request.user,
			'courses':Course.objects.all(),
		}
		return render(request, template_name, context)
	
	return render(request, template_name, context)

@login_required(login_url = 'evo/login')
def admission_add_course(request, course_id):
	if not(is_student(request)):
		return HttpResponse("Sorry You Can't Access This Page")

	#if student is already enrolled in any course show error
	try:
		course = request.user.studentcourse
		return HttpResponse('Sorry You Are Already Enrolled For A Course Contact Admin To Change It.')
	#else check whether course_id is valid
	except StudentCourse.DoesNotExist:
		try:
			selected_course = Course.objects.get(id = course_id)
			if (selected_course.admission_status):
				studentcourse = StudentCourse()
				studentcourse.student = request.user
				studentcourse.course = selected_course
				studentcourse.save()

				
				#saving the details in admission_status module for first time
				admission_status = AdmissionStatus()
				admission_status.student = request.user
				admission_status.save()
				return redirect('admission')
			else:
				return HttpResponse('Sorry Admission For This Course Is Not Available!')
		except Course.DoesNotExist:
			return HttpResponse('Sorry You Have Selected An Invalid Course')




@login_required(login_url = 'evo/login/')
def admission_basic(request):
	if not(is_student(request)):
		return HttpResponse("Sorry You Can't Access This Page")
	template_name = 'evo/admission/basic.html'
	try:
		student = request.user.student_basic
		submit = 'Update'
		form = StudentBasicForm(instance=student)
	except StudentBasic.DoesNotExist:
		student = StudentBasic(student=request.user)
		submit= 'Save'
		form = StudentBasicForm()
	context={
		'form':form,
		'submit':submit,
		'course':request.user.studentcourse.course.title,
	}
	if request.method == 'POST':
		form = StudentBasicForm(request.POST, instance=student)
		if form.is_valid():
			form.save()
			request.user.first_name = form.cleaned_data['first_name']
			request.user.last_name = form.cleaned_data['last_name']
			request.user.save()

			if (submit == 'Save'):
				#set the basic details to True as the student saves the basic details for first time
				admission_status = request.user.admissionstatus
				admission_status.basic = True
				admission_status.save()

			return redirect('admission_address')
		else:
			context['form']= form
	return render(request, template_name,context)
	

@login_required(login_url = 'evo/login/')
def admission_address(request):
	template_name = 'evo/admission/address.html'
	try:
		p_student = request.user.student_address.get(address_type = 'p')
		p_submit = 'Update'
		p_form = StudentAddressForm(instance=p_student,prefix='p')

	except StudentAddress.DoesNotExist:
		p_student = StudentAddress(student=request.user)
		p_submit = 'Save'
		p_form = StudentAddressForm(prefix='p')

	try:
		c_student = request.user.student_address.get(address_type = 'c')
		c_submit = 'Update'
		c_form = StudentAddressForm(instance=c_student,prefix='c')

	except StudentAddress.DoesNotExist:
		c_student = StudentAddress(student=request.user)
		c_submit = 'Save'
		c_form = StudentAddressForm(prefix='c')


	if(p_submit == c_submit):
		submit = p_submit
	else:
		submit = 'Save'

	context = {
		'p_form':p_form,
		'c_form':c_form,
		'submit':submit,
		'course':request.user.studentcourse.course.title,
	}

	if request.method == 'POST':
		p_form = StudentAddressForm(request.POST, instance=p_student,prefix='p')
		c_form = StudentAddressForm(request.POST, instance=c_student,prefix='c')
		

		if((p_form.is_valid()) and (c_form.is_valid())):
			p = p_form.save(commit=False)
			p.address_type = 'p'
			p.save()
			c = c_form.save(commit=False)
			c.address_type = 'c'
			c.save()

			if (submit == 'Save'):
				#set the basic details to True as the student saves the basic details for first time
				admission_status = request.user.admissionstatus
				admission_status.basic = True
				admission_status.save()

			return redirect('/admission/courses/')

		else:
			context['p_form'] = p_form
			context['c_form'] = c_form

	return render(request, template_name,context)