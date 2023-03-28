from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model where the email address is the unique identifier
    and has an is_admin field to allow access to the admin app
    """

    def create_admin(self,email, first_name, last_name, password=None, phone_number=None, role=None):

        if not email:
            raise ValueError(_("The email number must be set"))

        if not phone_number:
            raise ValueError(_("The phone number must be set"))
        if not password:
            raise ValueError(_("The password must be set"))
        if not role:
            raise ValueError(_("User must have a role"))

        email = self.normalize_email(email)
        user = self.model(email=email)
        user.first_name = first_name
        user.last_name = last_name
        user.phone_number = phone_number
        user.role = role
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user

    def create_user(self, email, first_name=None, last_name=None, password=None, phone_number=None, role=None):
        if not password:
            raise ValueError(_("The password must be set"))

        if not email:
            raise ValueError(_("Email must have a phone number"))

        if not phone_number:
            raise ValueError(_("User must have a phone number"))
        if not role:
            raise ValueError(_("User must have a role"))

        email = self.normalize_email(email)
        user = self.model(email=email)
        user.first_name = first_name
        user.last_name = last_name
        user.phone_number = phone_number
        user.role = role
        user.set_password(password)
        user.is_admin = False
        user.is_staff = False
        user.save()
        return user

    def create_superuser(self, email, password=None, phone_number=None):
        if not email:
            raise ValueError(_("The Email must be set"))
        if not password:
            raise ValueError(_("The password must be set"))

        email = self.normalize_email(email)
        user = self.model(email=email)
        user.phone_number = phone_number
        user.set_password(password)
        user.is_admin = False
        user.is_staff = False
        user.role = 1
        user.save()
        return user

