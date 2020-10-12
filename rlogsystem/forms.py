from django.forms import ModelForm
from rlogsystem.models import Agency

class AgencyForm(ModelForm):
    class Meta:
        model = Agency
        fields = '__all__'
    