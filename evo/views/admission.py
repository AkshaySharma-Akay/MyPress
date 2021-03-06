from django.shortcuts import render, redirect
from django.http import HttpResponse
from evo.models import Course, StatusStudent, StudentBasic, StudentAddress, StudentCourse
from evo.models import AdmissionStatus, StudentQualification, StudentUploads, EvoArticle, StatusStudent
from evo.forms import StudentBasicForm, StudentAddressForm, StudentQualificationForm, StudentUploadsForm
from evo.forms import StudentTermsForm, StudentFinalSubmissionForm
from django.contrib.auth.decorators import login_required

""" 
	admission.py
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
		template_name = 'evo/admission/index.html'
		context = {
			'user':request.user,
			'course':request.user.studentcourse.course.title,
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
	if not(is_student(request)):
		return HttpResponse("Sorry You Can't Access This Page")

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

			#Update the admission_status, completed this phase, this code is executed only once
			if (submit == 'Save'):
				admission_status = request.user.admissionstatus
				admission_status.address = True
				admission_status.save()

			#everthing done successfully redirect user to the next phase
			return redirect('admission_qualifications')

		else:
			context['p_form'] = p_form
			context['c_form'] = c_form

	return render(request, template_name,context)


@login_required(login_url='evo/login/')
def admission_qualifications(request):
	if not(is_student(request)):
		return HttpResponse("Sorry You Can't Access This Page")

	template_name = 'evo/admission/qualifications.html'
	try:
		p_student = request.user.studentqualification.get(course = 'pt')
		p_submit = 'Update'
		p_form = StudentQualificationForm(instance=p_student,prefix='p')

	except StudentQualification.DoesNotExist:
		p_student = StudentQualification(student=request.user)
		p_submit = 'Save'
		p_form = StudentQualificationForm(prefix='p')

	try:
		t_student = request.user.studentqualification.get(course = 't')
		t_submit = 'Update'
		t_form = StudentQualificationForm(instance=t_student, prefix='t')

	except StudentQualification.DoesNotExist:
		t_student = StudentQualification(student=request.user)
		t_submit = 'Save'
		t_form = StudentQualificationForm(prefix='t')


	if(p_submit == t_submit):
		submit = p_submit
	else:
		submit = 'Save'

	context = {
		'course':request.user.studentcourse.course.title,
		't_form': t_form,
		'p_form': p_form,
		'submit': submit,
	}

	if request.method == 'POST':
		t_form = StudentQualificationForm(request.POST, instance = t_student, prefix = 't')
		p_form = StudentQualificationForm(request.POST, instance = p_student , prefix = 'p')

		#validation of the forms
		if ( (t_form.is_valid()) and (p_form.is_valid()) ):
			t = t_form.save(commit = False)
			t.course = 't'
			t.save()
			p = p_form.save(commit = False)
			p.course = 'pt'
			p.save()
			
			#Update the admission_status, completed this phase, this code is executed only once
			if (submit == 'Save'):
				admission_status = request.user.admissionstatus
				admission_status.qualifications = True
				admission_status.save()

			#everthing done successfully redirect user to the next phase
			return redirect('admission_uploads')

		else:
			context['p_form'] = p_form
			context['t_form'] = t_form

	return render(request, template_name,context)

@login_required(login_url='evo/login/')
def admission_uploads(request):
	if not(is_student(request)):
		return HttpResponse("Sorry You Can't Access This Page")

	template_name = 'evo/admission/uploads.html'
	
	try:
		student = request.user.student_uploads
		submit = 'Update'
		form = StudentUploadsForm(instance=student)

	except StudentUploads.DoesNotExist:
		student = StudentUploads(student=request.user)
		submit= 'Save'
		form = StudentUploadsForm()

	context={
		'form':form,
		'submit':submit,
		'course':request.user.studentcourse.course.title,
	}

	if request.method == 'POST':
		form = StudentUploadsForm(request.POST, request.FILES , instance=student)
		if form.is_valid():
			form.save()

			if (submit == 'Save'):
				#set the basic details to True as the student saves the basic details for first time
				admission_status = request.user.admissionstatus
				admission_status.uploads = True
				admission_status.save()

			return redirect('admission_terms')
		else:
			context['form']= form
	return render(request, template_name,context)



@login_required(login_url='evo/login/')
def admission_terms(request):
	"View For Terms and Condition Page"
	if not(is_student(request)):
		return HttpResponse("Sorry You Can't Access This Page")

	terms = request.user.admissionstatus.terms
	submit = 'Next'

	terms_article = EvoArticle.objects.get(title = "Terms And Conditions")
	if request.user.admissionstatus.terms:
		form = False
		msg = "Already Accepted, Please Move To Next"
	else:	
		form = StudentTermsForm()
		msg = ''

	template_name = "evo/admission/terms.html"

	context={
		'submit':submit,
		'article' : terms_article,
		'course': request.user.studentcourse.course.title,
		'form':form,
		'msg':msg,
	}
	if request.method == 'POST':
		form = StudentTermsForm(request.POST)
		if form.is_valid():
			value = form.cleaned_data['terms']
			if value == 'a':
				ad_status = request.user.admissionstatus
				ad_status.terms = True
				ad_status.save()
			else:
				context['msg'] = "Sorry You Can't Move To Next, Without Accepting the Terms and Conditions.."
		else:
			context['form'] = form
	return render(request, template_name, context)


@login_required(login_url='evo/login/')
def admission_final_submission(request):
	"View For Terms and Condition Page"
	if not(is_student(request)):
		return HttpResponse("Sorry You Can't Access This Page")


	
	status = request.user.admissionstatus
	status_list = [status.basic, status.address, status.qualifications, status.uploads, status.terms]
	
	if False in status_list:
		return HttpResponse("Sorry You Can't Access This Page Until You Have Completed Other Admission Processes")

	template_name = "evo/admission/final_submission.html"

	final_submission = request.user.admissionstatus.finalsubmission
	print(final_submission)
	submit = 'Submit'

	if request.user.admissionstatus.finalsubmission:
		form = False
		msg = "Already Accepted, Please Download your Confirmation Page"
	else:	
		form = StudentFinalSubmissionForm()
		msg = ''

	context = {
		'submit':submit,
		'form':form,
		'msg':msg,
		'user':request.user,
		'basic_details': request.user.student_basic,
		'p_address': request.user.student_address.get(address_type='p'),
		'c_address': request.user.student_address.get(address_type='c'),
		'course': request.user.studentcourse.course,
		'qualifications_t': request.user.studentqualification.get(course = 't'),
		'qualifications_pt': request.user.studentqualification.get(course= 'pt'),
		'uploads':request.user.student_uploads,
	}

	if request.method == 'POST':
		form = StudentFinalSubmissionForm(request.POST)
		if form.is_valid():
			value = form.cleaned_data['finalsubmission']
			if value == 'a':
				ad_status = request.user.admissionstatus
				ad_status.finalsubmission = True
				ad_status.save()
				student_status = request.user.statusstudent
				student_status.admission = True
				student_status.save()
				return redirect(admission)
			else:
				context['msg'] = "Sorry you have to complete this step first"
		else:
			context['form'] = form
	
	return render(request, template_name,context)

	
@login_required(login_url='evo/login/')
def confirmation_page(request):
	"View For Terms and Condition Page"
	if not(is_student(request)):
		return HttpResponse("Sorry You Can't Access This Page")

	
	template_name = "evo/admission/final_submission.html"
	context ={
		'user':request.user,
		'basic_details': request.user.student_basic,
		'p_address': request.user.student_address.get(address_type='p'),
		'c_address': request.user.student_address.get(address_type='c'),
		'course': request.user.studentcourse.course,
		'qualifications_t': request.user.studentqualification.get(course = 't'),
		'qualifications_pt': request.user.studentqualification.get(course= 'pt'),
		'uploads':request.user.student_uploads,
	}
	return render(request, template_name,context)


@login_required(login_url='evo/login/')
def admission_confirm(request):
	"View For Terms and Condition Page"
	if not(is_student(request)):
		return HttpResponse("Sorry You Can't Access This Page")

	status  = StatusStudent.objects.get(student = request.user)
	if status.admission == False:
		return HttpResponse("Please, First Complete Your Admission Process")

	
	template_name = "evo/dashboard/confirmationpage.html"
	context ={
		'user':request.user,
		'basic_details': request.user.student_basic,
		'p_address': request.user.student_address.get(address_type='p'),
		'c_address': request.user.student_address.get(address_type='c'),
		'course': request.user.studentcourse.course,
		'qualifications_t': request.user.studentqualification.get(course = 't'),
		'qualifications_pt': request.user.studentqualification.get(course= 'pt'),
		'uploads':request.user.student_uploads,
	}
	return render(request, template_name,context)