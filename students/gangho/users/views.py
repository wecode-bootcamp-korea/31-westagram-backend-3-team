import json

from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.views import View

from users.models import User
from users.validators import validate_email, validate_password


class SignupView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            validate_email(data['email'])
            validate_password(data['password'])

            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({
                    'message': 'This email is already a registered email.'
                }, status=401)
            else:
                User.objects.create(
                    name            =data['name'],
                    email           =data['email'],
                    password        =data['password'],
                    phone_number    =data['phone_number']
                )
                return JsonResponse({
                    'message': 'Welcome to our service.'
                }, status=200)

        except KeyError:
            return JsonResponse({
                'message': 'Key Error'
            }, status=400)
        except ValidationError:
            return JsonResponse({
                'message': 'Email or Password is not a valid expression.'
            }, status=400)