import json
import re

from django.views import View
from django.http import JsonResponse

from .models import User

class SignUpView(View):
    def post(self, request):
        try:
            data               = json.loads(request.body)
            name               = data['name']
            email              = data['email']
            password           = data['password']
            phone_number       = data['phone_number']
            address            = data['address']
            regex_email        = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$"
            regex_password     = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%^&*()_+])[A-Za-z\d!@#$%^&*()_+?&]{8,}$"
            regex_phone_number = "^\d{3}-\d{3,4}-\d{4}$"

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
                password     = password,
                phone_number = phone_number,
                address      = address
            )
            return JsonResponse({"message" : "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)