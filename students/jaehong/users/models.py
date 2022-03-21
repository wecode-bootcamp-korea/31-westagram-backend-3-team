from django.db import models

class User(models.Model):
    name = models.CharField(max_length=11)
    email = models.EmailField(max_length=45, unique=True)
    password = models.CharField(max_length=100)    
    phone_number = models.CharField(max_length=11) 
   

    class Meta :
        db_table = "users"

