from django.urls import path

from .views import *

urlpatterns = [
    path('/signin', SignUpView.as_view()),
    path('/login', LogInView.as_view()),
]


