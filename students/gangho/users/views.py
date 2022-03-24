import json, bcrypt, jwt

from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.views import View
from django.db import IntegrityError

from users.models import User
from users.validators import validate_email, validate_password
from django.conf import settings

class SignupView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            name            = data['name']
            email           = data['email']
            password        = data['password']
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            phone_number    = data['phone_number']

            validate_email(email)
            validate_password(password)

            if User.objects.filter(email=email).exists():
                return JsonResponse({
                    'message': 'This email is already a registered email.'
                }, status=401)

            User.objects.create(
                name            = name,
                email           = email,
                password        = hashed_password,
                phone_number    = phone_number
            )

            return JsonResponse({
                'message': 'Welcome to our service.'
            }, status=200)

        except KeyError:
            return JsonResponse({
                'message': 'Key Error'
            }, status=400)
        except ValidationError as e:
            return JsonResponse({
                'message': e.messages
            }, status=400)
        except IntegrityError:
            return JsonResponse({
                'message': 'email overlap.'
            }, status=400)

class SigninView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            email    = data['email']
            password = data['password']

            validate_email(email)
            validate_password(password)

            user = User.objects.get(email=email)
            if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({'message': 'INVALID_USER'}, status=401)

            return JsonResponse({
                'message': "SUCCESS"
            }, status=200)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        except ValidationError as e:
            return JsonResponse({'message': e.messages}, status=400)
        except User.DoesNotExist:
            return JsonResponse({'message': "Invalid user"}, status=404)
