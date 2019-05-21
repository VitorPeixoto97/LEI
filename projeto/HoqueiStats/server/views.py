from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.forms.models import model_to_dict
from django.contrib.auth.models import User, Group
from . import models
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class IndexView(generic.ListView):
	template_name = 'index.html'
	context_object_name = 'club_list'
	def get_queryset(self):
		return models.Clube.objects.order_by('-nome')[:5]


class PostsView(ListAPIView):
    authentication_class = (JSONWebTokenAuthentication,) # Don't forget to add a 'comma' after first element to make it a tuple
    permission_classes = (IsAuthenticated,)


def index(request):
    context = 'Hello World'
    return render(request, 'server/index.html', context)


def infoUserView(request, email):
  if models.Gestor.objects.filter(email=email).count()==0:
    clube = models.Tecnico.objects.get(email=email).clube
  else:
    clube = models.Gestor.objects.get(email=email).clube

  return JsonResponse(model_to_dict(clube))


def advNome(request, form_id):
  formacao = get_object_or_404(models.Formacao, id=form_id)
  return JsonResponse(model_to_dict(formacao.clube))


@login_required
@permission_required('add_clube', raise_exception=True)
def clubeView(request, nome, cor, simbolo):
    existe = False
    for clube in models.Clube.objects.all():
        if clube.nome == nome:
            existe = True
    if not existe:
        models.Clube.objects.create(nome=nome, cor=cor, simbolo=simbolo)
        return HttpResponse('ok')
    else:
        return HttpResponseBadRequest(content='clube already exists')


@login_required
@permission_required('change_clube', raise_exception=True)
def cClubeView(request, id, cor, simbolo):
    models.Clube.objects.filter(id=id).update(cor=cor, simbolo=simbolo)
    return HttpResponse('ok')


@login_required
@permission_required('view_clube', raise_exception=True)
def gClubeView(request, id):
    clube = get_object_or_404(models.Clube, id=id)
    return JsonResponse(model_to_dict(clube))


@login_required
@permission_required('view_clube', raise_exception=True)
def gClubesView(request):
    clubes = models.Clube.objects.all()
    aux = []

    for clube in clubes:
        new_clube = {}
        new_clube['id'] = clube.id
        new_clube['nome'] = clube.nome
        new_clube['simbolo'] = clube.simbolo
        new_clube['cor'] = clube.cor
        aux.append(new_clube)

    return JsonResponse(aux, safe=False)


@login_required
@permission_required('add_gestor', raise_exception=True)
def gestorView(request):
    form = forms.UserForm(request.POST)
    if form.is_valid():
        existe = False
        for u in User.objects.all():
            if u.email == form.cleaned_data['email']:
                existe = True
        if not existe:
            group = Group.objects.get('Gestor')
            user, created = User.objects.create_user(first_name=form.cleaned_data['nome'], username=form.cleaned_data['email'], email=form.cleaned_data['email'], password=form.cleaned_data['password'], groups=group)
            if created:
                user.save()
                models.Gestor.objects.create(email=form.cleaned_data['email'], clube=form.cleaned_data['clube'])
                return HttpResponse('ok')
            else:
                return HttpResponseBadRequest(content='error')
        else:
            return HttpResponseBadRequest(content='email already in use')
    else:
        return HttpResponseBadRequest(content='bad form')


@login_required
@permission_required('add_formacao', raise_exception=True)
def formacaoView(request, clube, nome):
    clubex = get_object_or_404(models.Clube, id=clube)
    if clubex.formacao_set.get(nome=nome) is None:
        models.Formacao.objects.create(nome=nome, clube=clube)
        return HttpResponse('ok')
    else:
        return HttpResponseBadRequest(content='formacao already exists')


@login_required
@permission_required('delete_formacao', raise_exception=True)
def dFormacaoView(request, id):
    formacao = get_object_or_404(models.Formacao, id=id)
    formacao.delete()
    return HttpResponse('ok')


@login_required
@permission_required('view_formacao', raise_exception=True)
def gFormacoesView(request, clube):
    clubex = get_object_or_404(models.Clube, id=clube)
    formacoes = clubex.formacao_set.all()
    aux = []

    for formacao in formacoes:
        new_formacao = {}
        new_formacao['id'] = formacao.id
        new_formacao['nome'] = formacao.nome
        new_formacao['clube_id'] = formacao.clube.id
        aux.append(new_formacao)

    return JsonResponse(aux, safe=False)


@login_required
@permission_required('view_formacao', raise_exception=True)
def gFormacaoView(request, id):
    formacao = get_object_or_404(models.Formacao, id=id)
    return JsonResponse(model_to_dict(formacao))


@login_required
@permission_required('add_atleta', raise_exception=True)
def atletaView(request, licenca, nome, formacao, camisola):
    formacaox = get_object_or_404(models.Formacao, id=formacao)
    if formacaox.atleta_set.get(licenca=licenca) is None:
        models.Atleta.objects.create(nome=nome, formacao=formacao, licensa=licenca, camisola=camisola)
        return HttpResponse('ok')
    else:
        return HttpResponseBadRequest(content='atleta already exists')


@login_required
@permission_required('change_atleta', raise_exception=True)
def cAtletaView(request, id, formacao, camisola):
    models.Atleta.objects.filter(id=id).update(formacao=formacao, camisola=camisola)
    return HttpResponse('ok')


@login_required
@permission_required('delete_atleta', raise_exception=True)
def dAtletaView(request, id):
    atleta = get_object_or_404(models.Atleta, id=id)
    atleta.delete()
    return HttpResponse('ok')


#@login_required
#@permission_required('view_atleta', raise_exception=True)
def gAtletasView(request, formacao):
    formacaox = get_object_or_404(models.Formacao, id=formacao)
    atletas = formacaox.atleta_set.all()
    aux = []

    for atleta in atletas:
        new_atleta = {}
        new_atleta['id'] = atleta.id
        new_atleta['nome'] = atleta.nome
        aux.append(new_atleta)

    return JsonResponse(aux, safe=False)


#@login_required
#@permission_required('view_atleta', raise_exception=True)
def gAtletasEmCampoView(request, formacao, jogo):
    formacaox = get_object_or_404(models.Formacao, id=formacao)
    atletas = formacaox.atleta_set.all()
    aux = []

    for atleta in atletas:
        if models.Convocado.objects.filter(atleta=atleta.id, jogo=jogo).count() > 0:
            conv = get_object_or_404(models.Convocado, atleta=atleta.id, jogo=jogo)
            if conv.emCampo:
                new_atleta = {}
                new_atleta['id'] = atleta.id
                new_atleta['nome'] = atleta.nome
                aux.append(new_atleta)

    return JsonResponse(aux, safe=False)


#@login_required
#@permission_required('view_atleta', raise_exception=True)
def gAtletasSuplentesView(request, formacao, jogo):
    formacaox = get_object_or_404(models.Formacao, id=formacao)
    atletas = formacaox.atleta_set.all()
    aux = []

    for atleta in atletas:
        if models.Convocado.objects.filter(atleta=atleta.id, jogo=jogo).count() > 0:
            conv = get_object_or_404(models.Convocado, atleta=atleta.id, jogo=jogo)
            if not conv.emCampo:
                new_atleta = {}
                new_atleta['id'] = atleta.id
                new_atleta['nome'] = atleta.nome
                aux.append(new_atleta)

    return JsonResponse(aux, safe=False)


@login_required
@permission_required('view_atleta', raise_exception=True)
def gAtletaView(request, id):
    atleta = get_object_or_404(models.Atleta, id=id)
    return JsonResponse(model_to_dict(atleta))


@login_required
@permission_required('add_tecnico', raise_exception=True)
#ALTERAR ISTO, JÁ NÃO ESTAMOS A USAR FORMS
def tecnicoView(request):
    form = forms.UserForm(request.POST)
    if form.is_valid():
        existe = False
        for u in User.objects.all():
            if u.email == form.cleaned_data['email']:
                existe = True
        if not existe:
            group = Group.objects.get('Tecnico')
            user, created = User.objects.create_user(first_name=form.cleaned_data['nome'], username=form.cleaned_data['email'], email=form.cleaned_data['email'], password=form.cleaned_data['password'], groups=group)
            if created:
                user.save()
                models.Tecnico.objects.create(email=form.cleaned_data['email'], clube=form.cleaned_data['clube'])
                return HttpResponse('ok')
            else:
                return HttpResponseBadRequest(content='error')
        else:
            return HttpResponseBadRequest(content='email already in use')
    else:
        return HttpResponseBadRequest(content='bad form')


@login_required
@permission_required('change_tecnico', raise_exception=True)
def cTecnicoView(request, id, grelhaC, grelhaB):
    models.Tecnico.objects.filter(id=id).update(grelhaCampo=grelhaC, grelhaB=grelhaB)
    return HttpResponse('ok')


@login_required
@permission_required('add_jogo', raise_exception=True)
def jogoView(request, clube, formacao, formacaoAdv, casa, data, hora, tipo):
    models.Jogo.objects.create(ipo=tipo, clube=clube, formacao=formacao, adversario=formacaoAdv, casa=casa, data=data, hora=hora)
    return HttpResponse('ok')


@login_required
@permission_required('change_jogo', raise_exception=True)
def cJogoView(request, idJogo, grelhaC, grelhaB):
    models.Jogo.objects.filter(id=idJogo).update(grelhaCampo=grelhaC, grelhaBaliza=grelhaB)
    return HttpResponse('ok')


#@login_required
#@permission_required('view_jogo', raise_exception=True)
def gJogosView(request, clube):
    clubex = get_object_or_404(models.Clube, id=clube)
    formacoes = clubex.formacao_set.all()
    aux = []
    for formacao in formacoes:
        formacaox = get_object_or_404(models.Formacao, nome=formacao.nome, clube=formacao.clube)
        jogos = formacaox.minhaequipa.all()
        for jogo in jogos:
            new_jogo = {}
            new_jogo['numero'] = jogo.numero
            new_jogo['id'] = jogo.id
            new_jogo['tipo'] = jogo.tipo
            if(jogo.casa):
                new_jogo['casa'] = "C"
            else:
                new_jogo['casa'] = "F"
            new_jogo['data'] = jogo.data
            new_jogo['hora'] = jogo.hora
            new_jogo['resultado'] = gResultado(jogo.id)
            new_jogo['grelhaCampo'] = jogo.grelhaCampo
            new_jogo['grelhaBaliza'] = jogo.grelhaBaliza
            new_jogo['adversario'] = jogo.adversario.id
            new_jogo['formacao'] = jogo.formacao.id
            new_jogo['adv_nome'] = jogo.adversario.clube.nome
            new_jogo['form_nome'] = jogo.formacao.nome
            aux.append(new_jogo)
    return JsonResponse(aux, safe=False)

def adversario(form_id):
    formacao = get_object_or_404(models.Formacao, id=form_id)
    return formacao.clube


#@login_required
#@permission_required('view_jogo', raise_exception=True)
def gJogoView(request, id):
    jogo = get_object_or_404(models.Jogo, id=id)
    new_jogo = {}
    new_jogo['id'] = jogo.id
    new_jogo['numero'] = jogo.numero
    new_jogo['tipo'] = jogo.tipo
    if(jogo.casa):
        new_jogo['casa'] = "C"
    else:
        new_jogo['casa'] = "F"
    new_jogo['data'] = jogo.data
    new_jogo['hora'] = jogo.hora.strftime('%H:%M')
    new_jogo['resultado'] = gResultado(jogo.id)
    new_jogo['grelhaCampo'] = jogo.grelhaCampo
    new_jogo['grelhaBaliza'] = jogo.grelhaBaliza
    new_jogo['adversario'] = jogo.adversario.id
    new_jogo['formacao'] = jogo.formacao.id
    new_jogo['adv_nome'] = jogo.adversario.clube.nome
    new_jogo['form_nome'] = jogo.formacao.nome
    new_jogo['clube_nome'] = jogo.formacao.clube.nome
    new_jogo['logoMe'] = jogo.formacao.clube.simbolo
    new_jogo['logoAdv'] = jogo.adversario.clube.simbolo
    new_jogo['clube_cor'] = jogo.formacao.clube.cor
    new_jogo['adv_cor'] = jogo.adversario.clube.cor
    
    return JsonResponse(new_jogo)

def gResultado(id):
    jogo = get_object_or_404(models.Jogo, id=id)
    eventos = jogo.evento_set.all()
    aux = []
    golosC=0
    golosF=0
    if (eventos.count()==0): return ""
    for evento in eventos:
        if (evento.tipo.id==0 and evento.equipa==jogo.formacao):
            golosC+=1
        elif (evento.tipo.id==0 and evento.equipa==jogo.adversario):
            golosF+=1
    return str(golosC)+"-"+str(golosF) 



@login_required
@permission_required('add_convocado', raise_exception=True)
def convocadoView(request, jogo, atleta, emCampo):
    models.Convocado.objects.create(atleta=atleta, jogo=jogo, emCampo=emCampo)
    return HttpResponse('ok')


@login_required
@permission_required('change_convocado', raise_exception=True)
def cConvocadoView(request, jogo, atleta, emCampo):
    models.Convocado.objects.filter(atleta=atleta, jogo=jogo).update(emCampo=emCampo)
    return HttpResponse('ok')


@login_required
@permission_required('view_convocado', raise_exception=True)
def gConvocadosView(request, idJogo):
    jogo = get_object_or_404(models.Jogo, id=idJogo)
    convocados = jogo.convocado_set.all()
    aux = []

    for conv in convocados:
        new_convocado = {}
        new_convocado['id'] = conv.id
        new_convocado['atleta'] = conv.atleta.id
        new_convocado['jogo'] = conv.jogo.id
        new_convocado['emCampo'] = conv.emCampo
        aux.append(new_convocado)

    return JsonResponse(aux, safe=False)


#@login_required
#@permission_required('add_evento', raise_exception=True)
@csrf_exempt
def eventoView(request):
    if request.method=='POST':
        received = json.loads(request.body.decode('utf-8'))
	
        tp = received['tipo']
        jg = received['jogo']
        inst = received['instante']
        eq = received['equipa']
        at1 = received['atleta1']
        at2 = received['atleta2']
        zC = received['zonaC']
        zB = received['zonaB']
        novo = received['novoinst']
	
        if novo is not None:
            models.Evento.objects.create(tipo=tp, jogo=jg, instante=inst, novoinstante=novo)
        elif eq is not None and at1 is not None and at2 is not None:
            models.Evento.objects.create(tipo=tp, jogo=jg, equipa=eq, atleta1=at1, atleta2=at2, instante=inst)
            models.Convocado.objects.filter(atleta=at1, jogo=jg).update(emCampo=False)
            models.Convocado.objects.filter(atleta=at2, jogo=jg).update(emCampo=True)
        elif eq is not None and at1 is not None and zC is not None and zB is not None:
            models.Evento.objects.create(tipo=tp, jogo=jg, equipa=eq, atleta1=at1, zonaCampo=zC, zonaBaliza=zB, instante=inst)
        elif eq is not None and at1 is not None and zC is not None:
            models.Evento.objects.create(tipo=tp, jogo=jg, equipa=eq, atleta1=at1, zonaCampo=zC, instante=inst)
        elif eq is not None:
            models.Evento.objects.create(tipo=tp, jogo=jg, equipa=eq, instante=inst)

        return HttpResponse('ok')
    else:
        return HttpResponseBadRequest(content='bad form')


#@login_required
#@permission_required('change_evento', raise_exception=True)
@csrf_exempt
def cEventoView(request):
        
    if request.method=='POST':
        received = json.loads(request.body.decode('utf-8'))
        
        i = received['id']
        inst = received['instante']
        eq = received['equipa']
        at1 = received['atleta1']
        at2 = received['atleta2']
        zC = received['zonaC']
        zB = received['zonaB']
        novo = received['novoinst']

        if inst is not None:
            models.Evento.objects.filter(id=i).update(instante=inst)
        if novo is not None:
            models.Evento.objects.filter(id=i).update(instante=inst, novoinstante=novo)
        if eq is not None:
            models.Evento.objects.filter(id=i).update(equipa=eq)
        if at1 is not None:
            models.Evento.objects.filter(id=i).update(atleta1=at1)
        if at2 is not None:
            models.Evento.objects.filter(id=i).update(atleta2=at2)
            models.Convocado.objects.filter(atleta=at1, jogo=jg).update(emCampo=False)
            models.Convocado.objects.filter(atleta=at2, jogo=jg).update(emCampo=True)
        if zC is not None:
            models.Evento.objects.filter(id=i).update(zonaCampo=zC)
        if zB is not None:
            models.Evento.objects.filter(id=i).update(zonaBaliza=zB)

        return HttpResponse('ok')
    else:
        return HttpResponseBadRequest(content='bad form')


@login_required
@permission_required('delete_evento', raise_exception=True)
def dEventoView(request, id):
    evento = get_object_or_404(models.Evento, id=id)
    evento.delete()
    return HttpResponse('ok')


#@login_required
#@permission_required('view_evento', raise_exception=True)
def gEventosView(request, idJogo):
    jogo = get_object_or_404(models.Jogo, id=idJogo)
    eventos = jogo.evento_set.all()
    aux = []
    for evento in eventos:
        new_evento = {}
        new_evento['id'] = evento.id
        new_evento['jogo'] = evento.jogo.id
        new_evento['tipo'] = evento.tipo.id
        new_evento['equipa'] = evento.equipa.id
        new_evento['atleta1'] = evento.atleta1.id
        if(evento.atleta2):
            new_evento['atleta2'] = evento.atleta2.id
        new_evento['instante'] = evento.instante
        new_evento['novoinstante'] = evento.novoinstante
        new_evento['timestamp'] = evento.timestamp
        if(evento.jogo.grelhaCampo=="8x4"):
            if(evento.zonaCampo==1):
                new_evento['gcy'] = 13
                new_evento['gcx'] = 7
            elif(evento.zonaCampo==2):
                new_evento['gcy'] = 38
                new_evento['gcx'] = 7
            elif(evento.zonaCampo==3):
                new_evento['gcy'] = 61
                new_evento['gcx'] = 7
            elif(evento.zonaCampo==4):
                new_evento['gcy'] = 86
                new_evento['gcx'] = 7
            elif(evento.zonaCampo==5):
                new_evento['gcy'] = 13
                new_evento['gcx'] = 27
            elif(evento.zonaCampo==6):
                new_evento['gcy'] = 38
                new_evento['gcx'] = 27
            elif(evento.zonaCampo==7):
                new_evento['gcy'] = 61
                new_evento['gcx'] = 27
            elif(evento.zonaCampo==8):
                new_evento['gcy'] = 86
                new_evento['gcx'] = 27
            elif(evento.zonaCampo==9):
                new_evento['gcy'] = 13
                new_evento['gcx'] = 55
            elif(evento.zonaCampo==10):
                new_evento['gcy'] = 38
                new_evento['gcx'] = 55
            elif(evento.zonaCampo==11):
                new_evento['gcy'] = 61
                new_evento['gcx'] = 55
            elif(evento.zonaCampo==12):
                new_evento['gcy'] = 86
                new_evento['gcx'] = 55
            elif(evento.zonaCampo==13):
                new_evento['gcy'] = 13
                new_evento['gcx'] = 85
            elif(evento.zonaCampo==14):
                new_evento['gcy'] = 38
                new_evento['gcx'] = 85
            elif(evento.zonaCampo==15):
                new_evento['gcy'] = 61
                new_evento['gcx'] = 85
            elif(evento.zonaCampo==16):
                new_evento['gcy'] = 86
                new_evento['gcx'] = 85
            elif(evento.zonaCampo==17):
                new_evento['gcy'] = 13
                new_evento['gcx'] = 115
            elif(evento.zonaCampo==18):
                new_evento['gcy'] = 38
                new_evento['gcx'] = 115
            elif(evento.zonaCampo==19):
                new_evento['gcy'] = 61
                new_evento['gcx'] = 115
            elif(evento.zonaCampo==20):
                new_evento['gcy'] = 86
                new_evento['gcx'] = 115
            elif(evento.zonaCampo==21):
                new_evento['gcy'] = 13
                new_evento['gcx'] = 144
            elif(evento.zonaCampo==22):
                new_evento['gcy'] = 38
                new_evento['gcx'] = 144
            elif(evento.zonaCampo==23):
                new_evento['gcy'] = 61
                new_evento['gcx'] = 144
            elif(evento.zonaCampo==24):
                new_evento['gcy'] = 86
                new_evento['gcx'] = 144
            elif(evento.zonaCampo==25):
                new_evento['gcy'] = 13
                new_evento['gcx'] = 172
            elif(evento.zonaCampo==26):
                new_evento['gcy'] = 38
                new_evento['gcx'] = 172
            elif(evento.zonaCampo==27):
                new_evento['gcy'] = 61
                new_evento['gcx'] = 172
            elif(evento.zonaCampo==28):
                new_evento['gcy'] = 86
                new_evento['gcx'] = 172
            elif(evento.zonaCampo==29):
                new_evento['gcy'] = 13
                new_evento['gcx'] = 193
            elif(evento.zonaCampo==30):
                new_evento['gcy'] = 38
                new_evento['gcx'] = 193
            elif(evento.zonaCampo==31):
                new_evento['gcy'] = 61
                new_evento['gcx'] = 193
            elif(evento.zonaCampo==32):
                new_evento['gcy'] = 86
                new_evento['gcx'] = 193
            elif(evento.zonaCampo is None):
                new_evento['gcy'] = 200
                new_evento['gcx'] = 200

        if(evento.tipo.id==0):
            new_evento['size'] = 2
        elif(evento.tipo.id==4):
            new_evento['size'] = 8
        else:
            new_evento['size'] = 1
        aux.append(new_evento)
    return JsonResponse(aux, safe=False)


@login_required
@permission_required('view_evento', raise_exception=True)
def gEventoView(request, id):
    evento = get_object_or_404(models.Evento, id=id)
    return JsonResponse(model_to_dict(evento))


@login_required
@permission_required('add_tipoevento', raise_exception=True)
def tipoEventoView(request, tipo, equipa, atleta1, atleta2, zonaC, zonaB, novoinst):
    if models.TipoEvento.objects.get(tipo=tipo) is None:
        models.TipoEvento.objects.create(tipo=tipo, equipa=equipa, atleta1=atleta1, atleta2=atleta2, zonaC=zonaC, zonaB=zonaB, novoinst=novoinst)
        return HttpResponse('ok')
    else:
        return HttpResponseBadRequest(content='tipo already exists')


#@login_required
#@permission_required('view_tipoevento', raise_exception=True)
def gTipoEventoView(request, id):
    evento = get_object_or_404(models.Evento, id=id)
    tipoe = get_object_or_404(models.TipoEvento, tipo=evento.tipo)
    return JsonResponse(model_to_dict(tipoe))


#@login_required
#@permission_required('view_tipoevento', raise_exception=True)
def gTiposEventosView(request):
    tipos = models.TipoEvento.objects.all()
    aux = []

    for tipo in tipos:
        new_tipo = {}
        new_tipo['id'] = tipo.id
        new_tipo['tipo'] = tipo.tipo
        new_tipo['equipa'] = tipo.equipa
        new_tipo['atleta1'] = tipo.atleta1
        new_tipo['atleta2'] = tipo.atleta2
        new_tipo['zonaCampo'] = tipo.zonaCampo
        new_tipo['zonaBaliza'] = tipo.zonaBaliza
        new_tipo['novoinstante'] = tipo.novoinstante
        aux.append(new_tipo)

    return JsonResponse(aux, safe=False)


@login_required
@permission_required('add_tiposselecionados', raise_exception=True)
def tipoSelecionadoView(request, tipo, tecnico):
    models.TiposSelecionados.objects.create(tecnico=tecnico, tipo=tipo)
    return HttpResponse('ok')


@login_required
@permission_required('delete_tiposselecionados', raise_exception=True)
def dTipoSelecionadoView(request, id):
    tipo = get_object_or_404(models.TiposSelecionados, id=id)
    tipo.delete()
    return HttpResponse('ok')


#@login_required
#@permission_required('view_tiposselecionados', raise_exception=True)
def gTiposSelecionadosView(request, email):
    tecnico = get_object_or_404(models.Tecnico, email=email)
    tipos = models.TiposSelecionados.objects.filter(tecnico=tecnico.id)
    aux=[]
    
    for t in tipos:
        tipox = get_object_or_404(models.TipoEvento, tipo=t.tipo)
        new_tipo = {}
        new_tipo['id'] = tipox.id
        new_tipo['tipo'] = tipox.tipo
        aux.append(new_tipo)

    return JsonResponse(aux, safe=False)

