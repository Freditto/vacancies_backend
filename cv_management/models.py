from django.db import models

from users_management.models import User


# Create your models here.

class PersonalInformation(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    national_id = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    region = models.CharField(max_length=200 )
    district = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class AcademicQualification(models.Model):
    DEGREE = 1
    DIPLOMA = 2
    CERTIFICATE = 3
    A_LEVEL = 4
    O_LEVEL = 5

    EDUCATION_LEVEL_CHOICES = (
        (DEGREE, 'Degree'),
        (DIPLOMA, 'Diploma'),
        (CERTIFICATE, 'Certificate'),
        (A_LEVEL, 'A Level'),
        (O_LEVEL, 'O Level'),

    )

    education_level = models.PositiveSmallIntegerField(
        choices=EDUCATION_LEVEL_CHOICES, blank=True, null=True, default=7)
    country = models.CharField(max_length=200)
    institute_name = models.CharField(max_length=200)
    programme_name = models.CharField(max_length=200)
    date_from = models.DateField()
    date_to = models.DateField()
    attach_certificate = models.FileField(upload_to="uploads/", null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)


class WorkingExperience(models.Model):
    institute_name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    date_from = models.DateField()
    date_to = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class OtherPreference(models.Model):
    KISWAHILI = 1
    ENGLISH = 2
    BOTH = 3

    LANGUAGE_CHOICES = (
        (KISWAHILI, 'Kiswahili'),
        (ENGLISH, 'English'),
        (BOTH, 'Both'),


    )

    BEGINNER = 1
    INTERMEDIATE = 2
    ADVANCE = 3

    COMPUTER_CHOICES = (
        (BEGINNER, 'Beginner'),
        (INTERMEDIATE, 'Intermediate'),
        (ADVANCE, 'Advance'),

    )

    language = models.PositiveSmallIntegerField(
        choices=LANGUAGE_CHOICES, blank=True, null=True, default=7)

    computer_literacy = models.PositiveSmallIntegerField(
        choices=COMPUTER_CHOICES, blank=True, null=True, default=7)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Referee(models.Model):
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class OtherAttachment(models.Model):
    other_attachment = models.FileField(upload_to="uploads/", null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

