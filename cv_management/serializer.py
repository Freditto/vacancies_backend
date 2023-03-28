from rest_framework import serializers

from cv_management.models import PersonalInformation, AcademicQualification, WorkingExperience, OtherPreference, \
     OtherAttachment, Referee


class PersonalInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInformation
        fields = ['first_name', 'last_name', 'national_id', 'phone_number', 'region', 'district', 'street', 'user']


class AcademicQualificationSerializer(serializers.ModelSerializer):
    class Meta:
          model = AcademicQualification
          fields = ['education_level', 'country', 'institute_name', 'programme_name', 'date_from', 'date_to', 'attach_certificate', 'user']


class WorkingExperienceSerializer(serializers.ModelSerializer):
    class Meta:
          model = WorkingExperience
          fields = ['institute_name', 'job_title', 'region', 'address', 'date_from', 'date_to', 'user']


class OtherPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
          model = OtherPreference
          fields = ['language', 'computer_literacy', 'user']


class RefereeSerializer(serializers.ModelSerializer):
    class Meta:
          model = Referee
          fields = ['full_name', 'phone_number', 'address', 'user']


class OtherAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
          model = OtherAttachment
          fields = ['other_attachment', 'user']
