from django.http import JsonResponse
from django.views import View

from users.models import User


class UserCreateView(View):
    def post(self, request):
        data = request.body

        if data['email']:
            comparison_data = User.objects.get(email=data['email'])
            if comparison_data is None:
                User.objects.create(
                    name        = data["name"],
                    email       = data["email"],
                    password    = data["password"],
                    cell_phone  = data['cell_phone']
                )
            else:
                return JsonResponse({'error': '이미 회원가입된 이메일 입니다.'}, status=401)

        return JsonResponse({'message': 'SUCCESS'}, status=201)
