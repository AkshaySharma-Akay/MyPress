from django import forms
from django.contrib.auth.models import User


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