import json
import re
import bcrypt

from django.views import View
from django.http import JsonResponse

from .models import User

class SignUpView(View):
    def post(self, request):
        try:
            data                    = json.loads(request.body)
            name                    = data['name']
            email                   = data['email']
            password                = data['password']
            phone_number            = data['phone_number']
            address                 = data['address']
            encoded_password        = password.encode('utf-8')
            hash_password           = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
            decoded_hashed_password = hash_password.decode('utf-8')
            regex_email             = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$"
            regex_password          = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%^&*()_+])[A-Za-z\d!@#$%^&*()_+?&]{8,}$"
            regex_phone_number      = "^\d{3}-\d{3,4}-\d{4}$"

            if not re.match(regex_email, email):
                return JsonResponse({"message": "EMAIL_FORM_ERROR"}, status=400)
            if not re.match(regex_password, password):
                return JsonResponse({"message": "PASSWORD_FORM_ERROR"}, status=400)
            if not re.match(regex_phone_number, phone_number):
                return JsonResponse({"message": "PHONE_NUMBER_FORM_ERROR"}, status=400)
            if User.objects.filter(email=email):
                    return JsonResponse({"message": "EMAIL_ALREADY_EXISTS"}, status=400)

            User.objects.create(
                name         = name,
                email        = email,
                password     = decoded_hashed_password,
                phone_number = phone_number,
                address      = address
            )
            return JsonResponse({"message" : "SUCCESS"}, status=201)
            
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
                
class LogInView(View):
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



        
