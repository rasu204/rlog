from django.urls import path
from . import views

urlpatterns = [
    path('', views.index2, name='records')
    # path('', views.MappingView.as_view(), name = 'mapping')

]
