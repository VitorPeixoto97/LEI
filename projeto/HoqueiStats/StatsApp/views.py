from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.forms.models import model_to_dict
from . import models

class IndexView(generic.ListView):
	template_name = 'index.html'
	context_object_name = 'club_list'
	def get_queryset(self):
		return models.Clube.objects.order_by('-nome')[:5]


def index(request):
    context = 'Hello World'
    return render(request, 'statsapp/index.html', context)


def cAdminView(request, password):
    models.Admin.objects.filter(id=1).update(password=password)


def clubeView(request, nome, cor, simbolo):
    models.Clube.objects.create(nome=nome, cor=cor, simbolo=simbolo)


def cClubeView(request, id, cor, simbolo):
    models.Clube.objects.filter(id=id).update(cor=cor, simbolo=simbolo)


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


def cGestorView(request, id, password):
    models.Gestor.objects.filter(id=id).update(password=password)


def gGestorView(request, email):
    gestor = get_object_or_404(models.Gestor, email=email)
    return JsonResponse(model_to_dict(gestor))


def formacaoView(request, clube, nome):
    clube = get_object_or_404(models.Clube, nome=clube)
    models.Formacao.objects.create(nome=nome, clube=clube.id)


def dFormacaoView(request, id):
    formacao = get_object_or_404(models.Formacao, id=id)
    formacao.delete()


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


def cAtletaView(request, id, formacao, camisola):
    models.Atleta.objects.filter(id=id).update(formacao=formacao, camisola=camisola)


def dAtletaView(request, id):
    atleta = get_object_or_404(models.Atleta, id=id)
    atleta.delete()


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


def cTecnicoView(request, id, password, grelhaC, grelhaB):
    models.Tecnico.objects.filter(id=id).update(password=password, grelhaCampo=grelhaC, grelhaB=grelhaB)


def gTecnico(request, email):
    tecnico = get_object_or_404(models.Tecnico, email=email)
    return JsonResponse(model_to_dict(tecnico))


def jogoView(request, clube, formacao, formacaoAdv, casa, data, hora, tipo):
    models.Jogo.objects.create(ipo=tipo, clube=clube, formacao=formacao, adversario=formacaoAdv, casa=casa, data=data, hora=hora)


def cJogoView(request, idJogo, grelhaC, grelhaB):
    models.Jogo.objects.filter(id=idJogo).update(grelhaCampo=grelhaC, grelhaBaliza=grelhaB)


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


def convocadoView(request, jogo, atleta, emCampo):
    models.Convocado.objects.create(atleta=atleta, jogo=jogo, emCampo=emCampo)


def cConvocadoView(request, jogo, atleta, emCampo):
    models.Convocado.objects.filter(atleta=atleta, jogo=jogo).update(emCampo=emCampo)


def gConvocadosView(request, idJogo):
    jogo = get_object_or_404(models.Jogo, id=idJogo)
    convocados = jogo.convocado_set.all()
    aux = []
    for conv in convocados:
        aux.append(model_to_dict(conv))
    return JsonResponse(aux)


def eventoView(request, idJogo, idEquipa, tipo, atleta1, atleta2, zonaC, zonaB, instante, novoinst):
    #models.Evento.objects.create(tipo=tipo, jogo=idJogo, equipa=idEquipa, instante=instante)
    return None


def cEventoView(request, id, idEquipa, atleta1, atleta2, zonaC, zonaB, instante, novoinstate):
    #models.Evento.objects.filter(id=id).update(equipa=idEquipa, instante=instante)
    return None


def dEventoView(request, id):
    evento = get_object_or_404(models.Evento, id=id)
    evento.delete()


def gEventosView(request, idJogo):
    jogo = get_object_or_404(models.Jogo, id=idJogo)
    eventos = jogo.evento_set.all()
    aux = []
    for evento in eventos:
        aux.append(model_to_dict(evento))
    return JsonResponse(aux)


def gEventoView(request, id):
    evento = get_object_or_404(models.Evento, id=id)
    return JsonResponse(model_to_dict(evento))


def tipoEventoView(request, tipo, atleta1, atleta2, zonaC, zonaB, novoinst):
    models.TipoEvento.objects.create(tipo=tipo, atleta1=atleta1, atleta2=atleta2, zonaC=zonaC, zonaB=zonaB, novoinst=novoinst)


def gTiposEventosView(request):
    tipos = models.TipoEvento.objects.all()
    aux = []
    for tipo in tipos:
        aux.append(model_to_dict(tipo))
    return JsonResponse(aux)


def tipoSelecionadoView(request, tipo, tecnico):
    models.TiposSelecionados.objects.create(tecnico=tecnico, tipo=tipo)


def dTipoSelecionadoView(request, id):
    tipo = get_object_or_404(models.TiposSelecionados, id=id)
    tipo.delete()


def gTiposSelecionadosView(request, tecnico):
    tecnicox = get_object_or_404(models.Tecnico, id=tecnico)
    tipos = tecnicox.tiposselecionados_set.all()
    aux=[]
    for tipo in tipos:
        aux.append(model_to_dict(tipo))
    return JsonResponse(aux)

