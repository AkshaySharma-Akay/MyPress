from django import forms
from django.contrib.auth.models import User
from django.forms import formset_factory
from evo.models import StudentBasic,StudentAddress, StudentQualification,StudentUploads


#SigninForm for signin for everyone
class SigninForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['username','password']
		widgets = {
			'username':forms.TextInput(attrs={'placeholder':'Username'}), #,'class':'form-control'}),
			'password':forms.PasswordInput(attrs={'placeholder':'Password'}), #,'class':'form-control'}),
		}

# StudentForm for the Signup Form for Students
class SignupForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['username','email','password']
		widgets = {
			'username':forms.TextInput(attrs={'placeholder':'Username'}),
			'password':forms.PasswordInput(attrs={'placeholder':'Password'}),
			'email':forms.EmailInput(attrs={'placeholder':'E-Mail'}),
		}

class StudentBasicForm(forms.ModelForm):
	class Meta:
		model = StudentBasic
		fields = '__all__'
		exclude = ['student']

class StudentAddressForm(forms.ModelForm):
	class Meta:
		model = StudentAddress
		fields = '__all__'
		exclude = ['student','address_type']

class StudentQualificationForm(forms.ModelForm):
	class Meta:
		model = StudentQualification
		fields = '__all__'
		exclude = ['student','course']

class StudentUploadsForm(forms.ModelForm):
	class Meta:
		model = StudentUploads
		fields ='__all__'
		exclude = ['student']

		#def clean_stu_image(self):
		#	stu_image = self.cleaned_data['stu_image']

TERMS_CHOICE = [
	['a','Accept'],
	['d','Decline']
]

class StudentTermsForm(forms.Form):
	terms = forms.ChoiceField(choices=TERMS_CHOICE, widget=forms.RadioSelect())

class StudentFinalSubmissionForm(forms.Form):
	finalsubmission = forms.ChoiceField(choices=TERMS_CHOICE, widget=forms.RadioSelect())