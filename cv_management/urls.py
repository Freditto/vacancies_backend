from django.urls import path
from .views import *

app_name = 'app1'

urlpatterns = [
    path('setQuestion/<int:vac_id>', setQuestions),
    path('getQuestion/<int:vac_id>', getMultipleChoice),
    path('addRequirement', addRequirement),
    path('getRequirements/<int:vac_id>', getRequirements),
    path('setAnswer', setAnswer),
    path('insertVacancy', InsertVacancy),
    path('getVacancies', GetVacancies),
    path('vacancyInfo/<int:vac_id>', VacancyInfo),
    path('addDefaultQuestion', DefaultQuestion),
]
