from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


def get_user_token(user: User):
    refresh = RefreshToken.for_user(user)
    # tokens = {
    #     "access": str(refresh.access_token),
    #     "refresh": str(refresh),
    # }

    return str(refresh.access_token)
