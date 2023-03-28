import math
import uuid
from random import random

from django.contrib.auth import authenticate
from django.shortcuts import render
from urllib import request
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import User
from .serializers import AuthAdminRegistrationSerializer, AuthUserRegistrationSerializer, AuthUserLoginSerializer, \
    UserSerializer


# Create your views here.


class AuthAdminRegistrationView(APIView):
    serializer_class = AuthAdminRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User successfully registered!',
                'user': serializer.data
            }

            return Response(response, status=status_code)


class AuthUserRegistrationView(APIView):
    serializer_class = AuthUserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        if 'role' not in data:
            return Response('bad request', status=403)

        if str(data['role']) == '1':
            serializer = AuthAdminRegistrationSerializer(data=data)

        elif str(data['role']) == '2':
            serializer = AuthUserRegistrationSerializer(data=data)

        valid = serializer.is_valid(raise_exception=True)

        if valid:
            try:
                serializer.save()
            except ValueError:
                return Response({
                    'success': False,
                    'statusCode': 401
                })
            status_code = status.HTTP_201_CREATED

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User successfully registered!',
                'user': serializer.data
            }

            return Response(response, status=status_code)


def generateOTP():
    # Declare a digits variable
    # which stores all digits
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    OTP = ""

    # length of password can be changed
    # by changing value in range
    for i in range(4):
        OTP += digits[math.floor(random() * 10)]

    print("OTP", OTP)
    return OTP


class RequesOTP(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        if 'email' in request.data:
            code = generateOTP()
            print(code)
            try:
                user = User.objects.get(email=str(request.data['email']))
                print('saving')
                user.set_password(code)
                user.save()
                # todo send email with code
            except User.DoesNotExist:
                return Response({"status": False})

        return Response({"status": False})


class VerifyOTP(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data
        if "email" in data and "code" in data:
            print(data)
            try:
                the_user = User.objects.get(email=data['email'])
                user = authenticate(email=the_user.email, password=data['code'])
                if user is not None:
                    token = Token.objects.get_or_create(user=user)
                    user_serializer = UserSerializer(instance=user, many=False)

                    response = {
                        'token': str(token[0]),
                        'user': user_serializer.data
                    }
                    return Response(response)

                return Response({"message": "Invalid OTP"}, status=401)
            except User.DoesNotExist:
                return Response("User not found", status=404)

        return Response({"message": "Bad Request"}, status=400)


class GetUsers(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)


class AuthUserRegistrationView(APIView):
    serializer_class = AuthUserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        print(request.data)
        print('jdhshshd')
        serializer = self.serializer_class(data=request.data)
        print('333333')
        valid = serializer.is_valid()
        print('he')
        if valid:
            print('here')
            serializer.save()

            return Response(serializer.data, status=201)


        print(serializer.errors)
        return Response(serializer.errors)


class AuthUserLoginView(APIView):
    serializer_class = AuthUserLoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        print("Data", request.data)
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_200_OK


            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User logged in successfully',
                'token': serializer.data['token'],

                'user': {
                    'email': serializer.data['email'],
                    'role': serializer.data['role'],
                    'id': serializer.data['id'],
                    'phone_number': serializer.data['phone_number']
                }
            }

            return Response(response, status=status_code)
