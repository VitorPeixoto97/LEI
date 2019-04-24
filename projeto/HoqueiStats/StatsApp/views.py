from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.forms.models import model_to_dict
from . import models

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
    models.Clube.objects.create(nome=nome, cor=cor, simbolo=simbolo)


def gClubeView(request, id):
    clube = get_object_or_404(models.Clube, id=id)
    return JsonResponse(model_to_dict(clube))

def gClubesView(request):
    clubes = models.Clube.objects.all()
    aux = []
    for clube in clubes:
        aux.append(model_to_dict(clube))
    return JsonResponse(aux)

def gestorView(request, clube, email, nome, password):
    clube = get_object_or_404(models.Clube, nome=clube)
    models.Gestor.objects.create(nome=nome, email=email, password=password, clube=clube.id)


def cGestorView(request, email, password):
    return None


def gGestorView(request, email):
    gestor = get_object_or_404(models.Gestor, email=email)
    return JsonResponse(model_to_dict(gestor))


def formacaoView(request, clube, nome):
    clube = get_object_or_404(models.Clube, nome=clube)
    models.Formacao.objects.create(nome=nome, clube=clube.id)


def dFormacaoView(request, clube, id):
    return None


def gFormacoesView(request, clube):
    clubex = get_object_or_404(models.Clube, id=clube)
    formacoes = clubex.formacao_set.all()
    aux = []
    for formacao in formacoes:
        aux.append(model_to_dict(formacao))
    return JsonResponse(aux)


def gFormacaoView(request, id):
    formacao = get_object_or_404(models.Formacao, id=id)
    return JsonResponse(model_to_dict(formacao))


def atletaView(request, licenca, nome, formacao, camisola):
    models.Atleta.objects.create(nome=nome, formacao=formacao, licensa=licenca, camisola=camisola)


def cAtletaView(request, licenca, formacao, camisola):
    return None


def dAtletaView(request, licenca):
    return None


def gAtletas(request, formacao):
    formacaox = get_object_or_404(models.Formacao, id=formacao)
    atletas = formacaox.atleta_set.all()
    aux = []
    for atleta in atletas:
        aux.append(model_to_dict(atleta))
    return JsonResponse(aux)


def gAtleta(request, id):
    atleta = get_object_or_404(models.Atleta, id=id)
    return JsonResponse(model_to_dict(atleta))


def tecnicoView(request, clube, email, nome, password):
    clube = get_object_or_404(models.Clube, nome=clube)
    models.Tecnico.objects.create(nome=nome, email=email, password=password, clube=clube.id)


def cTecnicoView(request, email, password, grelhaC, grelhaB):
    return None


def gTecnico(request, email):
    tecnico = get_object_or_404(models.Tecnico, email=email)
    return JsonResponse(model_to_dict(tecnico))


def jogoView(request, clube, formacao, clubeAdv, formacaoAdv, casa, data, hora, tipo):
    return None


def cJogoView(request, idJogo, grelhaC, grelhaB):
    return None


def gJogosView(request, clube):
    clubex = get_object_or_404(models.Clube, id=clube)
    jogos = clubex.jogo_set.all()
    aux = []
    for jogo in jogos:
        aux.append(model_to_dict(jogo))
    return JsonResponse(aux)


def gJogoView(request, id):
    jogo = get_object_or_404(models.Jogo, id=id)
    return JsonResponse(model_to_dict(jogo))

def convocadoView(request, idJogo, licenca, emCampo):
    return None


def gConvocadosView(request, idJogo):
    return None


def eventoView(request, idJogo, idEquipa, tipo, atleta1, atleta2, zonaC, zonaB, instante, novoinst):
    return None


def dEventoView(request, idJogo, tipo, instante):
    return None


def gEventosView(request, idJogo):
    return None


def gEventoView(request, id):
    evento = get_object_or_404(models.Evento, id=id)
    return JsonResponse(model_to_dict(evento))


def tipoEventoView(request, tipo, atleta1, atleta2, zonaC, zonaB, novoinst):
    return None


def gTiposEventosView(request):
    return None


def tipoSelecionadoView(request, tipo, tecnico):
    return None


def dTipoSelecionadoView(request, tipo, tecnico):
    return None


def gTiposSelecionadosView(request, tecnico):
    return None