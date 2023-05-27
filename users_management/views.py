from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from .serializers import UserSerializer
from django.contrib.auth import authenticate, login, logout
from .token import get_user_token
from .models import User, SeekerProfile


# from app1.models import Wilaya, Kata, Mtaa, Citizen

# Create your views here.

@api_view(["POST", "GET"])
@permission_classes([AllowAny])
def RegisterUser(request):
    if request.method == "POST":
        data = request.data
        username = data['username']
        # user = None
        user = User.objects.filter(username=username)
        if user:
            message = {'message': 'user does exist'}
            return Response(message)

        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            message = {'save': True}
            return Response(message)
        else:
            message = {'save': False}
            return Response(message)
    return Response({'message': "hey bro"})


# {
#     "first_name":"mike",
#     "last_name":"cyril",
#     "username":"mike",
#     "email":"mike@gmail.com",
#     "password":"123"
#     "type":"seeker"
# }

@api_view(["POST"])
@permission_classes([AllowAny])
def LoginView(request):
    username = request.data.get('username')
    password = request.data.get('password')
    print(request.data)
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        user_id = User.objects.get(username=username)

        response = {
            'msg': 'success',
            'token': get_user_token(user),
            'user_id': user_id.id,
            'first_name': user_id.first_name,
            'last_name': user_id.last_name,
            'username': user_id.username,
            'email': user_id.email,
            'type': user_id.type
        }

        return Response(response)
    else:
        response = {
            'msg': 'fail',
            'info': 'Invalid username or password',
        }

        return Response(response)


# {
#     "username": "mike",
#     "password": "123"
# }


@api_view(["POST"])
@permission_classes([AllowAny])
def CreateProfile(request):
    # print(request.POST)
    data = request.POST
    user = User.objects.get(id=data['user_id'])
    profile = SeekerProfile.objects.create(
        user_id=user,
        last_job_title=data['last_job_title'],
        institute_name=data['institute_name'],
        supervisor_name=data['supervisor_name'],
        supervisor_contact=data['supervisor_contact'],
        starting_date=data['starting_date'],
        end_date=data['end_date'],
        o_level_index=data['o_level_index'],
        education_level=data['education_level'],
        program=data['program'],
        country=data['country'],
        date_of_birth=data['date_of_birth'],
        gender=data['gender'],
        phone=data['phone'],
        cv=request.FILES['cv']
    )
    profile.save()
    return Response({'message': 'successful'})


@api_view(["GET"])
@permission_classes([AllowAny])
def GetProfile(request, user_id):
    user = User.objects.get(id=user_id)
    data = SeekerProfile.objects.values('id',
                                        'last_job_title',
                                        'institute_name',
                                        'supervisor_name',
                                        'supervisor_contact',
                                        'starting_date',
                                        'end_date',
                                        'o_level_index',
                                        'education_level',
                                        'program',
                                        'country',
                                        'date_of_birth',
                                        'gender',
                                        'phone',
                                        'cv').get(user_id=user)
    return Response(data)
