import datetime


from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Atleta(models.Model):
    nome = models.CharField(max_length=200)
    licenca = models.IntegerField()
    def __str__(self):
        return self.nome

class Clube (models.Model):
    nome = models.CharField(max_length=200)
    cor = models.CharField(max_length=6)
    simbolo = models.TextField()
    def __str__(self):
        return self.nome
