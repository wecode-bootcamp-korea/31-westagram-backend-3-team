import re
from django.http import JsonResponse

regex_email             = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$"
regex_password          = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%^&*()_+])[A-Za-z\d!@#$%^&*()_+?&]{8,}$"
regex_phone_number      = "^\d{3}-\d{3,4}-\d{4}$"

def email_validation(email):
    if not re.match(regex_email, email):
        return JsonResponse({"message": "EMAIL_FROM_ERROR"}, status=400)

def password_validation(password):
    if not re.match(regex_password, password):
        return JsonResponse({"message": "PASSWORD_FROM_ERROR"}, status=400)

def phone_number_validation(phone_number):
    if not re.match(regex_phone_number, phone_number):
        return JsonResponse({"message": "PHONE_NUMBER_FORM_ERROR"}, status=400)