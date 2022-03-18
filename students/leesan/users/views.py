import json
import re

from django.views import View
from django.http import JsonResponse

from .models import User

class SignIn(View):
    def post(self, request):
        data                    = json.loads(request.body)
        name                    = data['name']
        email                   = data['email']
        email_validation        = re.compile('^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        password                = data['password']
        password_validation     = re.compile("^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%^&*()_+])[A-Za-z\d!@#$%^&*()_+?&]{8,}$")
        phone_number            = data['phone_number']
        phone_number_validation = re.compile("^\d{3}-\d{3,4}-\d{4}$")
        address                 = data['address']
        result                  = User.objects.filter(email=email)

        if email == "" or password == "":
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
        if not email_validation.match(email):
            return JsonResponse({"message": "EMAIL_FORM_ERROR"}, status=400)
        if not password_validation.match(password):
            return JsonResponse({"message": "PASSWORD_FORM_ERROR"}, status=400)
        if not phone_number_validation.match(phone_number):
            return JsonResponse({"message": "PHONE_NUMBER_FORM_ERROR"}, status=400)

        if not result:
            User.objects.create(
                name         = name,
                email        = email,
                password     = password,
                phone_number = phone_number,
                address      = address
                )
            return JsonResponse({"message" : "SUCCESS"}, status=201)
        return JsonResponse({"message": "ALREADY_USED_EMAIL"}, status=400)

                
class LogIn(View):
    def post(self, request):
        data                    = json.loads(request.body)
        email                   = data['email']
        password                = data['password']

        result_email = User.objects.filter(email=email).exists()
        result_password = User.objects.filter(password=password).exists()
        a = User.objects.get(email = email)
        a_password = a.password
        b = User.objects.get(password = password)
        b_email = b.email

        if email == "" or password == "":
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
        elif result_email == False or result_password == False:
                return JsonResponse({"message": "INVALID_USER"}, status=401)
        if a_password == password and b_email == email:
            if result_email == True and result_password == True:
                return JsonResponse({"message" : "SUCCESS"}, status=200)
        else:
            return JsonResponse({"message" : "INVALID_PASSWORD"}, status=200)



        
