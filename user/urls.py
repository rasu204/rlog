from django.urls import path
from . import views

urlpatterns = [
	path('',views.index,name='index'),
	path('signin', views.signin,name='signin'),
	path('login', views.login,name='login'),
	path('dashboard', views.dashboard,name='dashboard'),
	path('mandates', views.mandates,name='mandates'),
	path('upload', views.upload,name='upload'),
	path('badrecords', views.badrecords,name='badrecords'),
	path('manageteam', views.manageteam,name='manageteam'),
	path('contacts', views.contacts,name='contacts'),


]
