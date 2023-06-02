from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.db.models import Q
from users_management.models import User, SeekerProfile


# Create your views here.
@api_view(["POST"])
@permission_classes([AllowAny])
def InsertVacancy(request):
    data = request.data
    vacancy = JobVacancy.objects.create(
        company=data['company'],
        jobTitle=data['jobTitle'],
        jobType=data['jobType']
    )
    vacancy.save()
    response = {'message': "success"}
    return Response(response)


# {
#     "company": "tigo",
#     "jobTitle": "software developer",
#     "jobType": "part-time",
# }


@api_view(["POST"])
@permission_classes([AllowAny])
def setQuestions(request, vac_id):
    # added by a specific company which hiring
    data = request.data
    for s in data:
        question = Question.objects.create(
            question=s['question'],
            is_checkable=s['is_checkable'],
            vacancy_id=JobVacancy.objects.get(id=vac_id)
        )
        question.save()
        q = Question.objects.get(id=question.id)
        for d in s['answer']:
            answer = Answer.objects.create(answer=d['answer'], question_id=q, is_correct=d['is_correct'])
            answer.save()

    response = {"sms": 'success'}
    return Response(response)


# data = [
#     {"question": "bra bra", "is_checkable": false,
#      "answer":[
#          {"answer": "yes", "is_correct": true},
#          {"answer": "no", "is_correct": false}
#         ]
#      },
#     {"question": "bra bra", "is_checkable": false,
#      "answer":[
#          {"answer": "yes", "is_correct": true},
#          {"answer": "no", "is_correct": false}
#         ]
#      }
# ]


@api_view(["GET"])
@permission_classes([AllowAny])
def getMultipleChoice(request, vac_id):
    vacancy = JobVacancy.objects.get(id=vac_id)
    questions = Question.objects.values('id', 'question').filter(vacancy_id=vacancy)
    data = []
    for q in questions:
        que = Question.objects.get(id=q['id'])
        ans = Answer.objects.values('id', 'answer').filter(question_id=que)
        qs = {'id': q['id'], 'question': q['question'], 'answer': ans}
        data.append(qs)
    try:
        default_question = Question.objects.values('id', 'question').filter(is_checkable=True)
        x = [e for e in default_question]
        for q in x:
            que = Question.objects.get(id=q['id'])
            ans = Answer.objects.values('id', 'answer').filter(question_id=que)
            qs = {'id': q['id'], 'question': q['question'], 'answer': ans}
            data.append(qs)

    except:
        pass
    # response = {"data": data}
    return Response(data)


# {
#     "hiring_id": 1
# }


@api_view(["POST"])
@permission_classes([AllowAny])
def setAnswer(request, seeker_id):
    # kata = Kata.objects.get(id=request.data['kata_id'])
    seeker = SeekerProfile.objects.get(user_id=User.objects.get(id=seeker_id))
    data = request.data['answers']
    fail = []
    pas = []
    d_q = []
    for r in data:
        question = Question.objects.get(id=r['question_id'])
        if not question.is_checkable:
            if Answer.objects.filter(Q(id=r['answer_id']) and Q(question_id=question) and Q(is_correct=True)):
                pas.append(1)
            else:
                fail.append(1)
        else:
            d_q.append(r)
    print(d_q)
    for r2 in d_q:
        is_corr = False
        ans = Answer.objects.get(id=r2['answer_id'])
        try:
            if ans.answer == seeker.education_level:
                is_corr = True
            else:
                pass
        except:
            pass

        try:
            if ans.answer == seeker.country:
                is_corr = True
            else:
                pass
        except:
            pass

        try:
            if ans.answer == seeker.gender:
                is_corr = True
            else:
                pass
        except:
            pass

        if is_corr:
            pas.append(1)
        else:
            fail.append(1)

    percent = 100 * len(pas) / (len(pas) + len(fail))
    if percent < 50:
        status = "failed"
    else:
        status = "pass"
    vac = request.data['vac_id']
    user_id = request.data['user_id']

    print(percent)
    print(status)
    try:
        attempts = Attempts.objects.filter(
            Q(vacancy=JobVacancy.objects.get(id=vac)) and Q(user=User.objects.get(id=user_id)))
        print('-------------===--------')
        print(len(attempts))
        if len(attempts) == 3:
            message = {'message': 'failed to save attempt', 'success': False}
            return Response(message)
        print('000000000000')
        b = len(attempts)/0

    except:
        print('reached -----------')
        attempt = Attempts.objects.create(
            vacancy=JobVacancy.objects.get(id=vac),
            user=User.objects.get(id=user_id),
            percent=str(percent),
            state=status
        )
        attempt.save()

    data = {'percent': percent, 'status': status, 'success': True}
    return Response(data)


# {
#     'vac_id': 1,
#     'user_id': 2,
#     'answers': []
# }

# [
#     {'question_id': 1, 'answer_id': 1},
#     {'question_id': 2, 'answer_id': 5},
#     {'question_id': 3, 'answer_id': 6},
#     {'question_id': 4, 'answer_id': 11},
# ]

@api_view(["GET"])
@permission_classes([AllowAny])
def GetVacancies(request):
    data = JobVacancy.objects.values('id', 'company', 'jobTitle').all()
    d = [e for e in data]
    z = []
    for i in d:
        dt = JobVacancy.objects.get(id=i['id'])
        req = Requirement.objects.values('id', 'requirement').filter(job=dt)
        x = {
            'id': dt.id,
            'company': dt.company,
            'jobTitle': dt.jobTitle,
            'jobType': dt.jobType,
            'requirements': req
        }
        z.append(x)
    return Response(z)


@api_view(["GET"])
@permission_classes([AllowAny])
def VacancyInfo(request, vac_id):
    data = JobVacancy.objects.get(id=vac_id)
    req = Requirement.objects.values('id', 'requirement').filter(vacancy_id=data)
    d = {
        'id': data.company,
        'jobTitle': data.jobTitle,
        'duration': data.duration,
        'requirements': req
    }
    return Response(d)


@api_view(["POST"])
@permission_classes([AllowAny])
def DefaultQuestion(request):
    # added by a specific company which hiring
    data = request.data
    for s in data:
        question = Question.objects.create(
            question=s['question'],
            is_checkable=s['is_checkable']
            # vacancy_id=JobVacancy.objects.get(id=vac_id)
        )
        question.save()
        q = Question.objects.get(id=question.id)
        for d in s['answer']:
            answer = Answer.objects.create(answer=d['answer'], question_id=q, is_correct=d['is_correct'])
            answer.save()

    response = {"sms": 'success'}
    return Response(response)


# [
#     {"question": "Is your country?", "is_checkable": true,
#      "answer":[
#          {"answer": "Tanzania", "is_correct": false},
#          {"answer": "Kenya", "is_correct": false},
#          {"answer": "Uganda", "is_correct": false}
#      ]
#      },
#     {"question": "Is your gender?", "is_checkable": true,
#      "answer":[
#          {"answer": "male", "is_correct": false},
#          {"answer": "female", "is_correct": false}
#         ]
#      },
#     {"question": "Is your level of education?", "is_checkable": true,
#      "answer":[
#          {"answer": "ordinary diploma", "is_correct": false},
#          {"answer": "bachelor degree", "is_correct": false},
#          {"answer": "masters", "is_correct": false},
#         ]
#      }
# ]


@api_view(["POST"])
@permission_classes([AllowAny])
def addRequirement(request):
    job = JobVacancy.objects.get(id=request.data['vac_id'])
    req = Requirement.objects.create(requirement=request.data['requirement'], job=job)
    req.save()
    response = {"save": True}
    return Response(response)


# {
#     "requirement": "bra bra",
#     "vac_id": 1
# }


@api_view(["POST"])
@permission_classes([AllowAny])
def getRequirements(request, vac_id):
    job = JobVacancy.objects.get(id=vac_id)
    req = Requirement.objects.values('requirement').filter(job=job)
    return Response(req)


@api_view(["GET"])
@permission_classes([AllowAny])
def getAttempts(request, user_id):
    attempts = Attempts.objects.filter(user=User.objects.get(id=user_id))
    datas = []
    for data in attempts:
        datas.append(
            {
                'job': data.vacancy.jobTitle,
                'company': data.vacancy.company,
                'percent': data.percent,
                'status': data.state
            }
        )
    print(datas)
    return Response(datas)
