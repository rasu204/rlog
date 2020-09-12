from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

def alnum(value):
    pass
    # if not value.isalpha():
    #     raise ValidationError(_("Not alphanumeric"))

def phone_len(value):
    pass
    # if len(str(value)) != 10:
    #     raise ValidationError(_("Not 10 digits"))
