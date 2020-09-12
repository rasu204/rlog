from django import forms

from records.models import Staging

class Staging_form(forms.ModelForm):

    class Meta:
        model = Staging
        fields = '__all__'