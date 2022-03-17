from django.urls import path

from .views import *

urlpatterns = [
    path('/signup', UserView.as_view()),
]


