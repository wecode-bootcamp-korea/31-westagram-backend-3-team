import json
from django.http import JsonResponse
from django.views import View

from users.models import User
from users.validators import validate_email, validate_password


class SignupView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            if validate_email(data['email']) is None:
                return JsonResponse({
                    'message': 'This email is not a valid email expression.'
                }, status=400)

            if validate_password(data['password']) is None:
                return JsonResponse({
                    'message': 'This password is not a valid password expression.'
                }, status=400)

            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({
                    'message': 'This email is already a registered email.'
                }, status=401)
            else:
                User.objects.create(
                    name=data['name'],
                    email=data['email'],
                    password=data['password'],
                    phone_number=data['phone_number']
                )
                return JsonResponse({
                    'message': 'Welcome to our service.'
                }, status=200)

        except KeyError:
            return JsonResponse({
                'message': 'Key Error'
            }, status=400)

        return JsonResponse({'message': 'network is working.'}, status=200)