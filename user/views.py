from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User
from django.contrib.auth.models import User
# Create your views here.
def index(request):
	if request.method == 'POST':
		FullName = request.POST['FullName']
		UserType = request.POST['UserType']
		UserCompany = request.POST['UserCompany']
		Designation = request.POST['Designation']
		##pin_code = request.POST['pin_code']
		EmailID = request.POST['EmailID']
		Phone = request.POST['Phone']
		##city = request.POST['city']
		Password=User.objects.make_random_password()

		user = User(FullName=FullName,UserType=UserType,UserCompany=UserCompany,Designation=Designation,EmailID=EmailID,Phone=Phone,Password=Password)
		user.save()
		print('user created')
		return render(request,'signin.html')


	else:
		return render(request,'index.html')
		
		
























def signin(request):
	return render(request,'signin.html')
def login(request):
	return render(request,'login.html')
def dashboard(request):
	return render(request,'dashboard.html')
def mandates(request):
	return render(request,'mandates.html')
def upload(request):
	return render(request,'upload.html')
def badrecords(request):
	return render(request,'badrecords.html')
def manageteam(request):
	return render(request,'manageteam.html')
def contacts(request):
	return render(request,'contacts.html')