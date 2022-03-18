import re
import json
from django.http import JsonResponse
from django.views import View

from users.models import User

def validate_email(email):
    email_expression = re.match(r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email)
    return email_expression

def validate_password(password):
    password_expression = re.match(r'/^(?=.*\d)(?=.*[a-zA-Z])[0-9a-zA-Z!@#$%^&*]{8,20}$/', password)
    return password_expression

class SignupView(View):
    def post(self, request):
        data = json.load(request.body)

        if not (data['email'] and data['passowrd']):
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

        if not validate_email(data['email']):
            return JsonResponse({'message': 'This is not a valid email expression.'}, status=401)

        if not validate_password(data['passowrd']):
            return JsonResponse({'message': 'This is not a valid password expression.'}, status=401)

        return JsonResponse({'message':'network is woring.'}, status=200)

    def get(self, request):
        return JsonResponse({'message': 'network is woring.'}, status=200)