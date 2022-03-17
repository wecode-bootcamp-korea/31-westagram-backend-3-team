import json
from django.views import View
from django.http import JsonResponse
from .models import User
import re


class UserView(View):
    def post(self, request):

            data                = json.loads(request.body)
            name                = data['name']
            email               = data['email']
            email_validation    = re.compile('^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
            password            = data['password']
            password_validation = re.compile("^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$")
            phone_number        = data['phone_number']

            if email == "" or password == "":
                return JsonResponse({"mesage": "Email과 Password를 입력하세요"}, status=400)
            if not email_validation.match(email):
                return JsonResponse({"mesage": "Email을 형식에 맞게 입력하세요"}, status=400)
            if not password_validation.match(password):
                return JsonResponse({"mesage": "Password를 형식에 맞게 입력하세요"}, status=400)

            User.objects.create(
                name         = name,
                email        = email,
                password     = password,
                phone_number = phone_number
                )
            return JsonResponse({"message" : "SUCCESS"}, status=201)

