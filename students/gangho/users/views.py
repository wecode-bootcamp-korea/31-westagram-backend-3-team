import json

from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.views import View
from django.db import IntegrityError

from users.models import User
from users.validators import validate_email, validate_password


class SignupView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            name         = data['name']
            email        = data['email']
            password     = data['password']
            phone_number = data['phone_number']

            validate_email(email)
            validate_password(password)

            if User.objects.filter(email=email).exists():
                return JsonResponse({
                    'message': 'This email is already a registered email.'
                }, status=401)

            User.objects.create(
                name            = name,
                email           = email,
                password        = password,
                phone_number    = phone_number
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
                'message': 'Invalid Key'
            }, status=400)
        except IntegrityError:
            return JsonResponse({
                'message': 'email overlap.'
            })