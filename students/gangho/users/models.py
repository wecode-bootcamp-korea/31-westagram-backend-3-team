import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db import models

def validate_email(email):
    email_expression = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

    if not email_expression.match(email):
        raise ValidationError(
            _('%(value)s is not an email expression'),
            params={'email': email},
        )

def validate_password(password):
    password_expression = re.compile('[a-zA-Z0-9+-_.]')

    if not password_expression.match(password):
        raise ValidationError(
            _('%(value)s is not an password expression'),
            params={'password': password},
        )

def validate_cell_phone(cell_phone):
    cell_phone_expression = re.compile('[]]')

    if not cell_phone_expression.match(cell_phone):
        raise ValidationError(
            _('%(value)s is not an email expression'),
            params={'email': cell_phone},
        )

class User(models.Model):
    name        = models.CharField(max_length=45, db_column='name')
    email       = models.EmailField(validators=[validate_email], db_column='email')
    password    = models.CharField(validators=[validate_password], max_length=30, db_column='password')
    cell_phone  = models.CharField(validators=[validate_cell_phone], max_length=30, db_column='cell_phone')

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name