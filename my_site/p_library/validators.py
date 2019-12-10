from django.db import models
from django.core.exceptions import ValidationError

def validate_zero(value):
    if value <= 0:
        raise ValidationError(u'%s cannot be left blank' % value)