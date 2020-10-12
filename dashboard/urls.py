from django.urls import path
from dashboard import views

urlpatterns = [
    path('', views.index10, name='index'),
    path('blank', views.index5),
    path('buttons', views.index6),
    path('cards', views.index7),
    path('charts', views.index8),
    path('forgot-password', views.index9),
    path('404', views.index4),
    path('login_dash', views.index11),
    path('tables', views.index12),
    path('utilities-animation', views.index13),
    path('utilities-border', views.index14),
    path('utilities-color', views.index15),
    path('utilities-other', views.index16),
    path('register', views.index17),
    path('choose', views.index18),

]
