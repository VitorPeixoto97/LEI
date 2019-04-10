import datetime


from django.db import models
from django.utils import timezone


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
    password = models.CharField(max_length=200)
    clube = models.ForeignKey(Clube, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = 'Gestores'

class Tecnico(models.Model):
    nome = models.CharField(max_length=200)
    formacao = models.ForeignKey(Formacao, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = 'Técnicos'

class Jogo(models.Model):
    tipo = models.CharField(max_length=200)
    formacao = models.ForeignKey(Formacao, on_delete=models.CASCADE, related_name="Minhaequipa")
    adversario = models.ForeignKey(Formacao, on_delete=models.CASCADE, related_name="Adversário")
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE)
    casafora = models.BooleanField(default=True)
    def __str__(self):
        return self.adversario





