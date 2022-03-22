import json, re

from .models import User

from django.http import JsonResponse
from django.views import View


class SignUpView (View):
    def post(self, request):
        try:
            data= json.loads(request.body)
            
            name         = data["name"]
            email        = data["email"]
            password     = data["password"]
            phone_number = data["phone_number"]
                
            if User.objects.filter(email=email).exists() : 
                return JsonResponse({"message" : "ALREADY EXISTS"}, status=400)
            
            REGEX_EMAIL    = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            REGEX_PASSWORD = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$"
                
            if not re.match(REGEX_EMAIL, email) :
                return JsonResponse({"message" : "INVALID EMAIL"}, status=400)
                                    
            if not re.match(REGEX_PASSWORD, password) :
               return JsonResponse({"message" : "INVALID PASSWORD"}, status=400)
           
           
            User.objects.create(
                
                name         = name,
                email        = email,
                password     = password,
                phone_number = phone_number,
            )
           
            return JsonResponse({"message": "SUCCESS"}, status=201)
                
        except KeyError: 
            return JsonResponse({"message": "KEY_ERROR"},status =400)