from django.db import models
from django.contrib.auth.models import AbstractUser
from users_management.models import *


class User(AbstractUser):
    choice = (('seeker', 'seeker'), ('hire', 'hire'))
    type = models.CharField(max_length=20, choices=choice)
    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'


class SeekerProfile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = (('male', 'male'), ('female', 'female'))
    count = (('Tanzania', 'Tanzania'), ('Kenya', 'Kenya'),
             ('Uganda', 'Uganda'))
    level = (('ordinary diploma', 'ordinary diploma'),
             ('bachelor degree', 'bachelor degree'),
             ('masters', 'masters'))
    # choice
    last_job_title = models.CharField(max_length=200, null=True)
    institute_name = models.CharField(max_length=200, null=True)
    supervisor_name = models.CharField(max_length=200, null=True)
    supervisor_contact = models.CharField(max_length=10, null=True)
    starting_date = models.DateField(auto_now_add=True, null=True)
    end_date = models.DateField(auto_now_add=True, null=True)

    # required info
    o_level_index = models.CharField(max_length=20)
    education_level = models.CharField(max_length=200, choices=level)
    program = models.CharField(max_length=200)
    country = models.CharField(max_length=30, choices=count)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20, choices=gender)
    phone = models.CharField(max_length=10)

    # to upload cv
    cv = models.FileField(upload_to="cvs/")

    def __str__(self):
        return f'{self.user_id.username} = {self.user_id.type}'

    class Meta:
        db_table = 'seeker_profile'



