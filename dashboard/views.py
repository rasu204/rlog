from django.shortcuts import render, redirect
from dashboard import views
from mapping import views




# Create your views here.

def index10(request):
    return render(request, 'index_dash.html')


def index11(request):
    return render(request, 'login_dash.html')


def index12(request):
    return render(request, 'tables.html')


def index13(request):
    return render(request, 'utilities-animation.html')


def index14(request):
    return render(request, 'utilities-border.html')


def index15(request):
    return render(request, 'utilities-color.html')


def index16(request):
    return render(request, 'utilities-other.html')


def index4(request):
    return render(request, '404.html')


def index5(request):
    return render(request, 'blank.html')


def index6(request):
    return render(request, 'buttons.html')


def index7(request):
    return render(request, 'cards.html')


def index8(request):
    return render(request, 'charts.html')


def index9(request):
    return render(request, 'forgot-password.html')


def index17(request):
    return render(request, 'register.html')


def index18(request):
    return redirect('/choose')

