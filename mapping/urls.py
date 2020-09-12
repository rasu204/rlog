from django.urls import path
from . import views

urlpatterns = [
        path('import', views.import_data),
        path('fieldmatching', views.fieldmatching),
        path('', views.disp, name='mapping')
        # path('', views.MappingView.as_view(), name = 'mapping')

]
