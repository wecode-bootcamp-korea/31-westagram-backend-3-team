from django.urls import path

from .views import *

urlpatterns = [
    path('/signin', SignIn.as_view())
]