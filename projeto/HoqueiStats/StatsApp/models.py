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
    formacao = models.ForeignKey(Formacao, on_delete=models.CASCADE) 
    licenca = models.IntegerField()
    camisola = models.IntegerField()
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
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    clube = models.ForeignKey(Clube, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = 'Técnicos'

class Jogo(models.Model):
    tipo = models.CharField(max_length=200)
    formacao = models.ForeignKey(Formacao, on_delete=models.CASCADE, related_name='MinhaEquipa')
    adversario = models.ForeignKey(Formacao, on_delete=models.CASCADE, related_name='EquipaAdversaria')
    casa = models.BooleanField(default=True)
    data = models.DateField()
    hora = models.TimeField()
    grelhaCampo = models.CharField(max_length=5)
    grelhaBaliza = models.CharField(max_length=5)
    def __str__(self):
        return self.adversario

class Convocado(models.Model):
   atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE)
   jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
   emcampo = models.BooleanField(default=True)
   def __str__(self):
	return self.jogo

class Evento(models.Model):
   tipo = models.CharField(max_length=200)
   jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
   equipa = models.ForeignKey(Formacao, on_delete=models.CASCADE)
   atleta1 = models.ForeignKey(Atleta, on_delete=models.CASCADE, blank=True, null=True)
   atleta2 = models.ForeignKey(Atleta, on_delete=models.CASCADE, blank=True, null=True)
   zonaCampo = models.IntegerField(default=None, blank=True, null=True)
   zonaBaliza = models.IntegerField(default=None, blank=True, null=True)
   instante = models.TimeField()
   novoinstante = models.TimeField(default=Nome, blank=True, null=True)
   timestamp = models.DateTimeField(auto_now_add=True)
   def __str__(self):
       return self.tipo





