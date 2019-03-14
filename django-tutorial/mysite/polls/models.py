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

class Clube(models.Model):
    nome = models.CharField(max_length=200)
    cor = models.CharField(max_length=6)
    simbolo = models.TextField()
    def __str__(self):
        return self.nome

class Formacao(models.Model):
    nome = models.CharField(max_length=200)
    clube = models.ForeignKey(Clube, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = 'Formações'

class Atleta(models.Model):
    nome = models.CharField(max_length=200)
    licenca = models.IntegerField()
    def __str__(self):
        return self.nome

class Gestor(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput)
    clube = forms.ForeignKey(Clube, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = 'Gestores'

class Jogo(models.Model):
    tipo = models.CharField(max_length=200)
    adversario = models.ForeignKey(Formacao, on_delete=models.CASCADE)
    



