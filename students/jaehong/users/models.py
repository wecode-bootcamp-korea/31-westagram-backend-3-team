from django.db import models

class User(models.Model) :
    name         = models.CharField(max_length =100), 
    email        = models.EmailField(unique = True), 
    password     = models.CharField(max_length=300), 
    phone_number = models.CharField(max_length=11, unique= True) 

class Meta :
    db_table = "users"
# Create your models here.
