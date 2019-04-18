from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from . import models
import json

#isto é mesmo preciso?

class IndexView(generic.ListView):
	template_name = 'index.html'
	context_object_name = 'club_list'
	def get_queryset(self):
		return models.Clube.objects.order_by('-nome')[:5]

def index(request):
    context = 'Hello World'
    return render(request, 'statsapp/index.html', context)


def cAdminView(request, email, password):
    return None


def clubeView(request, nome, cor, simbolo):
    return None


def gCLubeView(request, nome):
    clube = get_object_or_404(models.Clube, nome=nome)
    jsonOut = json.dumps(clube)
    return HttpResponse(jsonOut, content_type="clube/json")


def gestorView(request, clube, email, nome, password):
    return None


def cGestorView(request, email, password):
    return None


def formacaoView(request, clube, nome):
    return None


def dFormacaoView(request, clube, nome):
    return None


def gFormacaoView(request, clube, nome):
    formacao = get_object_or_404(models.Formacao, clube=clube, nome=nome)
    jsonOut = json.dumps(formacao)
    return HttpResponse(jsonOut, content_type="formacao/json")

def atletaView(request, clube, licenca, nome, formacao, camisola):
    return None


def cAtletaView(request, licenca, formacao, camisola):
    return None


def dAtletaView(request, licenca):
    return None


def gAtleta(request, licenca):
    atleta = get_object_or_404(models.Atleta, licenca=licenca)
    jsonOut = json.dumps(atleta)
    return HttpResponse(jsonOut, content_type="atleta/json")


def tecnicoView(request, clube, email, nome, password):
    return None


def cTecnicoView(request, email, password, grelhaC, grelhaB):
    return None


def gTecnico(request, email):
    tecnico = get_object_or_404(models.Tecnico, email=email)
    jsonOut = json.dumps(tecnico)
    return HttpResponse(jsonOut, content_type="tecnico/json")


def jogoView(request, clube, formacao, clubeAdv, formacaoAdv, casa, data, hora, tipo):
    return None


def cJogoView(request, idJogo, grelhaC, grelhaB):
    return None


def gJogoView(request, clube, formacao, data, hora):
    form = get_object_or_404(models.Formacao, clube=clube, nome=formacao)
    jogo = get_object_or_404(models.Jogo, formacao=form.id, data=data, hora=hora)
    jsonOut = json.dumps(jogo)
    return HttpResponse(jsonOut, content_type="jogo/json")

def convocadoView(request, idJogo, licenca, emCampo):
    return None


def gConvocadosView(request, idJogo):
    return None


def eventoView(request, idJogo, idEquipa, tipo, atleta1, atleta2, zonaC, zonaB, instante, novoinst):
    return None


def dEventoView(request, idJogo, tipo, instante):
    return None


def gEventoView(request, idJogo, tipo, instante):
    evento = get_object_or_404(models.Evento, jogo=idJogo, tipo=tipo, instante=instante)
    jsonOut = json.dumps(evento)
    return HttpResponse(jsonOut, content_type="evento/json")


def gEventosView(request, idJogo):
    return None


def tipoEventoView(request, tipo, atleta1, atleta2, zonaC, zonaB, novoinst):
    return None


def gTiposEventosView(request):
    return None


def tipoSelecionadoView(request, tipo, email):
    return None


def dTipoSelecionadoView(request, tipo, email):
    return None


def gTiposSelecionadosView(request, email):
    return None