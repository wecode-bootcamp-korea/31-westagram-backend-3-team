from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField()
    phone_number = models.IntegerField()
    address = models.CharField(max_length=50)

    class Meta:
        db_table = 'users'

