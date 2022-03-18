import json
from django.http import JsonResponse
from django.views import View

from users.models import User
from users.validators import validate_email, validate_password


class SignupView(View):
    def post(self, request):
        data = json.loads(request.body)

        if not (data['email'] and data['password']):
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

        validate_email(data['email'])
        validate_password(data['password'])

        if data['email']:
            user_in_database = User.objects.get(email=data['email'])
            if user_in_database:
                return JsonResponse({'message': 'You are already a registered user.'}, status=401)
            else:
                User.objects.create(
                    name        = data['name'],
                    email       = data['email'],
                    password    = data['password'],
                    phone_number= data['phone_number'],
                    created_at  = data['created_at'],
                    updated_at  = data['updated_at']
                )
                return JsonResponse({'message': 'Welcome to our service.'}, status=200)

        return JsonResponse({'message': 'network is working.'}, status=200)