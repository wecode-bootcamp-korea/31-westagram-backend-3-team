from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField()
    phone_number = models.IntegerField()

    class Meta:
        db_table = 'users'
