from django.db import models


# Create your models here.

class JobVacancy(models.Model):
    choice = (('part-time', 'part-time'), ('full-time', 'full-time'))
    company = models.CharField(max_length=30)
    jobTitle = models.CharField(max_length=200)
    jobType = models.CharField(max_length=20, choices=choice)

    def __str__(self):
        return f''

    class Meta:
        db_table = 'job_vacancy'


class Requirement(models.Model):
    requirement = models.CharField(max_length=200)
    job = models.ForeignKey(JobVacancy, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.requirement}'

    class Meta:
        db_table = 'requirements'


class Question(models.Model):
    question = models.TextField()
    vacancy_id = models.ForeignKey(JobVacancy, on_delete=models.CASCADE, null=True)
    is_checkable = models.BooleanField(default=False)

    class Meta:
        db_table = 'question'

    def __str__(self):
        return self.question


class Answer(models.Model):
    answer = models.CharField(max_length=200)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)

    class Meta:
        db_table = 'answer'

    def __str__(self):
        return f'question {self.question_id.question} answer {self.answer}'
