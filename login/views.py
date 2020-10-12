from django.shortcuts import render
from login import views

# Create your views here.
def index24(request):
	return render(request,'index_login.html')