from django.urls import path

from users.views import SignupView, SigninView

urlpatterns = [
    path('/signup', SignupView.as_view()),
    path('/login', SigninView.as_view())
]
