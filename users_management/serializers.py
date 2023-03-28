from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import User


class AuthAdminRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'phone_number',
            'password',
            'email',
            'role',
        )

    def create(self, validated_data):
        auth_user = User.objects.create_admin(**validated_data)
        return auth_user


class AuthUserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'password',
            'role',
        )

    def create(self, validated_data):
        auth_user = User.objects.create_user(**validated_data)
        return auth_user


class AuthUserLoginSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(read_only=True)
    role = serializers.CharField(read_only=True)
    id = serializers.CharField(read_only=True)
    email = serializers.CharField(read_only=True)

    def create(self, validated_date):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, data):
        print(data)
        email = data['email']
        password = data['password']
        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid login credentials")

        try:
            token = Token.objects.get_or_create(user=user)

            update_last_login(None, user)

            validation = {
                'token': str(token[0]),
                'email': user.email,
                'id': user.id,
                'role': user.role,
            }

            return validation
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid login credentials")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class AuthUserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'password',
            'phone_number',
            'role'
        )

    def create(self, validated_data):
        auth_user = User.objects.create_user(**validated_data)
        return auth_user


class AuthUserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(read_only=True)
    phone_number = serializers.CharField(read_only=True)
    role = serializers.CharField(read_only=True)
    id = serializers.CharField(read_only=True)

    def create(self, validated_date):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, data):
        email = data['email']
        password = data['password']
        user = authenticate(email=email, password=password)

        if user is None:
              serializers.ValidationError("Invalid login credentials")

        try:
            token = Token.objects.get_or_create(user=user)
            validation = {
                'token': str(token[0]),
                'email': user.email,
                'id': user.id,
                'role': user.role,
                'phone_number': user.phone_number
            }

            return validation
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid login credentials")


