from django.urls import path
from landpage import views

urlpatterns = [

    path('', views.index19),
    path('inner-page/', views.index20),
    path('portfolio/', views.index21),
]
