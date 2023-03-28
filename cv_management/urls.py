from django.contrib import admin
from django.urls import path
from .views import PersonalInformationView, AcademicQualificationView, WorkingExperienceView, OtherPreferenceView, RefereeView, OtherAttachmentView

urlpatterns = [
    path('personal-info', PersonalInformationView.as_view()),
    path('academic-qualification', AcademicQualificationView.as_view()),
    path('working-experience', WorkingExperienceView.as_view()),
    path('other-preference', OtherPreferenceView.as_view()),
    path('referees', RefereeView.as_view()),
    path('other-attachment', OtherAttachmentView.as_view()),

]