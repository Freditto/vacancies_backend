from django.contrib import admin
from django.urls import path
from .views import GetUsers, AuthUserRegistrationView, AuthUserLoginView

urlpatterns = [

    path('users', GetUsers.as_view()),

    path(r'register', AuthUserRegistrationView.as_view()),
    path(r'login', AuthUserLoginView.as_view()),




]