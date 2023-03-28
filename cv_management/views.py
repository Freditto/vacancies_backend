from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from cv_management.models import PersonalInformation, AcademicQualification, WorkingExperience, OtherPreference, \
     OtherAttachment, Referee
from cv_management.serializer import PersonalInformationSerializer, AcademicQualificationSerializer, \
    WorkingExperienceSerializer, OtherPreferenceSerializer, OtherAttachmentSerializer, \
    RefereeSerializer


# Create your views here.


class PersonalInformationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        personal_info = PersonalInformation.objects.all()
        user_id = self.request.GET.get('user_id', None)

        print(user_id)

        if user_id is not None:
            personal_info = personal_info.filter(client=user_id)

        serializer = PersonalInformationSerializer(personal_info, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        serializer = PersonalInformationSerializer(data=request.data)
        feed = dict()

        if serializer.is_valid():
            # created_by = request.user
            personal_info = serializer.save()

            feed.update({"status": 200, "data": serializer.data, "details": "Personal Info added successfully"})
            return Response(feed)

        feed.update({"status": 400, "data": serializer.errors, "details": "Record not added successfully"})
        return Response(feed)

    def delete(self, request):
        return Response("Unauthorized deletion, contact system administrator")


class AcademicQualificationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        academic_qualification = AcademicQualification.objects.all()
        user_id = self.request.GET.get('user_id', None)

        print(user_id)

        if user_id is not None:
            academic_qualification = academic_qualification.filter(client=user_id)

        serializer = AcademicQualificationSerializer(academic_qualification, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        serializer = AcademicQualificationSerializer(data=request.data)
        feed = dict()

        if serializer.is_valid():
            # created_by = request.user
            academic_qualification = serializer.save()

            feed.update({"status": 200, "data": serializer.data, "details": "Academic Qualification added successfully"})
            return Response(feed)

        feed.update({"status": 400, "data": serializer.errors, "details": "Record not added successfully"})
        return Response(feed)

    def delete(self, request):
        return Response("Unauthorized deletion, contact system administrator")


class WorkingExperienceView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        working_experience = WorkingExperience.objects.all()
        user_id = self.request.GET.get('user_id', None)

        print(user_id)

        if user_id is not None:
            working_experience = working_experience.filter(client=user_id)

        serializer = WorkingExperienceSerializer(working_experience, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        serializer = WorkingExperienceSerializer(data=request.data)
        feed = dict()

        if serializer.is_valid():
            # created_by = request.user
            working_experience = serializer.save()

            feed.update({"status": 200, "data": serializer.data, "details": "Working Experience added successfully"})
            return Response(feed)

        feed.update({"status": 400, "data": serializer.errors, "details": "Record not added successfully"})
        return Response(feed)

    def delete(self, request):
        return Response("Unauthorized deletion, contact system administrator")


class OtherPreferenceView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        other_preference = OtherPreference.objects.all()
        user_id = self.request.GET.get('user_id', None)

        print(user_id)

        if user_id is not None:
            other_preference = other_preference.filter(client=user_id)

        serializer = OtherPreferenceSerializer(other_preference, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        serializer = OtherPreferenceSerializer(data=request.data)
        feed = dict()

        if serializer.is_valid():
            # created_by = request.user
            other_preference = serializer.save()

            feed.update({"status": 200, "data": serializer.data, "details": "Other preference added successfully"})
            return Response(feed)

        feed.update({"status": 400, "data": serializer.errors, "details": "Record not added successfully"})
        return Response(feed)

    def delete(self, request):
        return Response("Unauthorized deletion, contact system administrator")


class RefereeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        referee = Referee.objects.all()
        user_id = self.request.GET.get('user_id', None)

        print(user_id)

        if user_id is not None:
            referee = referee.filter(client=user_id)

        serializer = RefereeSerializer(referee, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        serializer = RefereeSerializer(data=request.data)
        feed = dict()

        if serializer.is_valid():
            # created_by = request.user
            referee = serializer.save()

            feed.update({"status": 200, "data": serializer.data, "details": "Referee added successfully"})
            return Response(feed)

        feed.update({"status": 400, "data": serializer.errors, "details": "Record not added successfully"})
        return Response(feed)

    def delete(self, request):
        return Response("Unauthorized deletion, contact system administrator")


class OtherAttachmentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        other_attachment = OtherAttachment.objects.all()
        user_id = self.request.GET.get('user_id', None)

        print(user_id)

        if user_id is not None:
            other_attachment = other_attachment.filter(client=user_id)

        serializer = OtherAttachmentSerializer(other_attachment, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        serializer = OtherAttachmentSerializer(data=request.data)
        feed = dict()

        if serializer.is_valid():
            # created_by = request.user
            other_attachment = serializer.save()

            feed.update({"status": 200, "data": serializer.data, "details": "Other Attachment added successfully"})
            return Response(feed)

        feed.update({"status": 400, "data": serializer.errors, "details": "Record not added successfully"})
        return Response(feed)

    def delete(self, request):
        return Response("Unauthorized deletion, contact system administrator")

