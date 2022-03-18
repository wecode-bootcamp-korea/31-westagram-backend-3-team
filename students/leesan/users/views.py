import json
from django.views import View
from django.http import JsonResponse
from .models import User
import re


class SignIn(View):
    def post(self, request):

            data                    = json.loads(request.body)
            name                    = data['name']
            email                   = data['email']
            email_validation        = re.compile('^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
            password                = data['password']
            password_validation     = re.compile("^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%^&*()_+])[A-Za-z\d!@#$%^&*()_+?&]{8,}$")
            phone_number            = data['phone_number']
            phone_number_validation = re.compile('/^\d{3}-\d{3,4}-\d{4}$/')
            address                 = data['address']
            
            if email=="" or password =="":
                return JsonResponse({"message": "KET_ERROR"}, status=400)
            if not email_validation.match(email):
                return JsonResponse({"message": "Email을 형식에 맞게 입력하세요"}, status=400)
            if not password_validation.match(password):
                return JsonResponse({"message": "Password를 형식에 맞게 입력하세요"}, status=400)
            if not phone_number_validation.match(phone_number):
                return JsonResponse({"message": "Phone_number를 형식에 맞게 입력하세요"}, status=400)

            result = User.objects.filter(email=email)  
            if not result:
                User.objects.create(
                    name         = name,
                    email        = email,
                    password     = password,
                    phone_number = phone_number,
                    address      = address
                    )
                return JsonResponse({"message" : "SUCCESS"}, status=201)
            return JsonResponse({"message": "다른 사용자가 사용하는 email입니다. 다시 입력해주세요."}, status=400)

                
class LogIn(View):
    def post(self, request):
        data                    = json.loads(request.body)
        email                   = data['email']
        password                = data['password']

        result_email = User.objects.filter(email=email).exists()
        result_password = User.objects.filter(password=password).exists()
        email_email = User.objects.get(email=email)
        email_id = email_email.id 
        password__password = User.objects.get(password=password)
        password_id = password__password.id
        if email == "" or password == "":
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
        elif result_email == False or result_password == False:
                return JsonResponse({"message": "INVALID_USER"}, status=401)
        if email_id == password_id:
            if result_email == True and result_password == True:
                return JsonResponse({"message" : "SUCCESS"}, status=200)
        else:
            return JsonResponse({"message": "email_id != password_id"}, status=401) 


        
