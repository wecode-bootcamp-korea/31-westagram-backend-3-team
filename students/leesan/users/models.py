from django.db import models


class User(models.Model):
    name         = models.CharField(max_length=50)
    email        = models.EmailField(max_length=50, unique=True)
    password     = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=50)
    address      = models.CharField(max_length=50)

    class Meta:
        db_table = 'users'

