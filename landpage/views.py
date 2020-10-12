from django.shortcuts import render
from landpage import views


# Create your views here.
def index19(request):
    return render(request, 'index-home.html')


def index20(request):
    return render(request, 'inner-page.html')


def index21(request):
    return render(request, 'portfolio-details.html')
