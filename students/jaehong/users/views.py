import json, re

from .models import User

from django.http import JsonResponse
from django.views import View


class SignUpView (View):
    def post(self, request):
        try:
            data= json.loads(request.body)
            
            name = data["name"]
            email = data["email"]
            password = data["password"]
            phone_number = data["phone_number"]
                
            if User.objects.filter(email=email).exists() : # 기존 가입한 회원의 이메일과 가입할려는 사람의 이메일이 같을시 에러 반환
                return JsonResponse({"message" : "ALREADY EXISTS"}, status=400)
            
            regex_email = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            regex_password = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$"
                
            if not re.match(regex_email, email) :
                return JsonResponse({"message" : "INVALID EMAIL"}, status=400)
                                    
            if not re.match(regex_password, password) :
               return JsonResponse({"message" : "INVALID PASSWORD"}, status=400)
           
           
            User.objects.create(
                
                name = name,
                email = email,
                password = password,
                phone_number = phone_number,
            )
           
            return JsonResponse({"message": "SUCCESS"}, status=201)
                
        except KeyError: 
            return JsonResponse({"message": "KEY_ERROR"},status =400)