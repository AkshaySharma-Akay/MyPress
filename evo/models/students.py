from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator, MaxLengthValidator
from evo.models.courses import Course



STUDENT_COURSE_OPTIONS = [
	['1','10Th'],
	['10+2','10+2'],	
]

GENDER_CHOICES = [
	['m','Male'],
	['f','Female']
]

CATEGORY_CHOICES = [
	['gen','General'],
	['sc','Scheduled Caste'],
	['st','Scheduled Tribe'],
	['irdp','Integrated Rural Development Programme'],
]
ADDRESS_CHOICES = [
	['p','Permanent'],
	['c','Correspondence']
]

#Magic of Thinking Big

#Check Status of Student, admission and profile
class StatusStudent(models.Model):
	student = models.OneToOneField(User, on_delete=models.CASCADE)
	admission = models.BooleanField(default=False)
	profile = models.BooleanField(default=False)

	def __str__(self):
		return(self.student.username)

#Models To Store The Basic Details of The Student
class StudentBasic(models.Model):
	"Models to store the basic details of the student"
	student = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student_basic')
	aadhaar_number = models.CharField("Addhar Number",max_length=12)
	first_name = models.CharField("First Name",max_length=150)
	last_name = models.CharField("Last Name" ,max_length=150, blank=True)
	fathers_name = models.CharField("Father's Name",max_length=150)
	mothers_name = models.CharField("Mother's Name",max_length=150)
	dob = models.DateField("Date Of Birth")
	gender = models.CharField("Gender",max_length=1,choices=GENDER_CHOICES,default='m')
	category = models.CharField("Category",max_length=4,choices=CATEGORY_CHOICES,default='gen')

	def __str__(self):
		return (self.student.username + self.first_name + self.last_name)

#Model To Store The Addresses Of The Student
class StudentAddress(models.Model):
	"Model To Store The Addresses of the students"
	student = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='student_address')
	address_type= models.CharField("Address Type", max_length=1, choices=ADDRESS_CHOICES,default='p')
	village =  models.CharField("Village/City/Town",max_length=70)
	postoffice = models.CharField("Post Office",max_length=70)
	tehsil = models.CharField("Tehsil",max_length=70)
	district = models.CharField("District",max_length=50)
	state = models.CharField("State",max_length=50)
	pincode = models.CharField("Pin Code",max_length=6,validators=[MinLengthValidator(6)])
	mobile = models.CharField("Phone/Mobile",max_length=20)

	def __str__(self):
		if str(self.address_type) == 'p':
			return (self.student.username + "'s " + " Permanent Address")
		else:
			return (self.student.username + "'s " + " Correspondence Address" )

class StudentQualification(models.Model):
	"Model To Store The Student's Qualification Details"
	student = models.ForeignKey(User, on_delete = models.CASCADE)
	course = models.CharField(max_length = 3, choices = STUDENT_COURSE_OPTIONS)
	year = models.IntegerField(validators=[MinValueValidator(1970), MaxValueValidator(2015)])
	board = models.CharField(max_length = 150)
	institute = models.CharField(max_length = 150)
	percentage = models.IntegerField(validators=[MinValueValidator(33), MaxValueValidator(100)])

	def __str__(self):
		return (self.student.username + self.course)

class StudentCourse(models.Model):
	"Model To store the students course status i.e. in which course he is enrolled"
	student = models.OneToOneField(User, on_delete= models.CASCADE)
	course = models.ForeignKey(Course, on_delete= models.CASCADE)

	def __str__(self):
		return (self.course.title)

class AdmissionStatus(models.Model):
	"Model To Store the Admission Status Of A Student"
	student =  models.OneToOneField(User, on_delete = models.CASCADE)
	basic = models.BooleanField( default = False)
	address = models.BooleanField( default = False)
	qualifications = models.BooleanField( default = False)
	uploads = models.BooleanField( default = False)
	terms = models.BooleanField( default = False)
	finalsubmission = models.BooleanField( default = False)
	
	def __str__(self):
		return(self.student.username + " : ")

