from django.urls import path
from . import views

urlpatterns = [
        path('import', views.import_data),
        path('fieldmatching', views.fieldmatching),
        path('choose', views.choose),
        path('', views.disp, name='mapping'),
        path('import_p', views.import_data_p),
        # path('', views.MappingView.as_view(), name = 'mapping')

]
