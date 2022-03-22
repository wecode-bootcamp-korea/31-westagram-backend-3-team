import json
import bcrypt

from django.views import View
from django.http import JsonResponse

from .models import User
from .validation import email_validation, password_validation, phone_number_validation

class SignUpView(View):
    def post(self, request):
        try:
            data                    = json.loads(request.body)
            name                    = data['name']
            email                   = data['email']
            password                = data['password']
            phone_number            = data['phone_number']
            address                 = data['address']
            hash_password           = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            
            email_validation(email)
            password_validation(password)
            phone_number_validation(phone_number)

            if User.objects.filter(email=email):
                    return JsonResponse({"message": "EMAIL_ALREADY_EXISTS"}, status=400)

            User.objects.create(
                name         = name,
                email        = email,
                password     = hash_password,
                phone_number = phone_number,
                address      = address
            )
            return JsonResponse({"message" : "SUCCESS"}, status=201)
            
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
                
class LogInView(View):
        def post(self, request):
            try:
                data            = json.loads(request.body)
                email           = data['email']
                password        = data['password']
                
                if not User.objects.filter(email=email, password=password).exists():
                    return JsonResponse({"message": "INVALID_USER"}, status=401)

                return JsonResponse({"message" : "SUCCESS"}, status=200)
      
            except KeyError:
                return JsonResponse({"message": "KEY_ERROR"}, status=400)



        
