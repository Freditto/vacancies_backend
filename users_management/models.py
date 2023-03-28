from django.utils import timezone

from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


from .manager import CustomUserManager


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    ADMIN = 1
    USER = 2

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (USER, 'User'),


    )

    email = models.EmailField(unique=True)
    phone_number = models.CharField(verbose_name="Mobile Number", max_length=20, unique=True, null=True)
    password = models.CharField(max_length=50, blank=True)
    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, blank=True, null=True, default=7)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    # a admin user; non super-user
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE, related_name='+')
    modified_by = models.EmailField()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['phone_number']

    objects = CustomUserManager()

    def __str__(self):
        return self.phone_number


