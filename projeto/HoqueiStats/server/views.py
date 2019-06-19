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
    user_info = {}
    user_info['email'] = email
    user_info['nome'] = get_object_or_404(User, email=email).first_name
    user_info['pass'] = get_object_or_404(User, email=email).password

    if models.Gestor.objects.filter(email=email).count() > 0:
        clube = get_object_or_404(models.Gestor, email=email).clube
        user_info['tipo'] = 'gestor'
        user_info['clube'] = clube.id
        user_info['clube_logo'] = clube.simbolo

    elif models.Tecnico.objects.filter(email=email).count() > 0:
        tecnico = get_object_or_404(models.Tecnico, email=email)
        user_info['tipo'] = 'tecnico'
        user_info['clube'] = tecnico.clube.id
        user_info['clube_logo'] = tecnico.clube.simbolo
        user_info['grelhaCampo'] = tecnico.grelhaCampo
        user_info['grelhaBaliza'] = tecnico.grelhaBaliza

    return JsonResponse(user_info, safe=False)


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


#@login_required
#@permission_required('view_clube', raise_exception=True)
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


#@login_required
#@permission_required('add_gestor', raise_exception=True)
@csrf_exempt
def gestorView(request):
    if request.method=='POST':
        received = json.loads(request.body.decode('utf-8'))
        
        email = received['email']
        password = received['password']
        nome = received['nome']
        clubeID = received['clube']
        clube = get_object_or_404(models.Clube, id=clubeID)

        if models.Gestor.objects.filter(email=email).count() == 0:
            group = Group.objects.get(name='Gestor')
            user = User.objects.create_user(first_name=nome, username=email, email=email, password=password)
            user.save()
            user.groups.add(group)
            models.Gestor.objects.create(email=email, clube=clube)
            return HttpResponse('ok')
        else:
            return HttpResponseBadRequest(content='gestor already exists')
    else:
        return HttpResponseBadRequest(content='bad form')


#@login_required
#@permission_required('add_formacao', raise_exception=True)
@csrf_exempt
def formacaoView(request):
    if request.method=='POST':
        received = json.loads(request.body.decode('utf-8'))
        
        nome = received['nome']
        clubeID = received['clube']
        clube = get_object_or_404(models.Clube, id=clubeID)

        if models.Formacao.objects.filter(clube=clube, nome=nome).count() == 0:
            models.Formacao.objects.create(nome=nome, clube=clube)
            return HttpResponse('ok')
        else:
            return HttpResponseBadRequest(content='formacao already exists')
    else:
        return HttpResponseBadRequest(content='bad form')


#@login_required
#@permission_required('view_formacao', raise_exception=True)
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


#@login_required
#@permission_required('add_atleta', raise_exception=True)
@csrf_exempt
def atletaView(request):
    if request.method=='POST':
        received = json.loads(request.body.decode('utf-8'))
        
        licenca = received['licenca']
        camisola = received['camisola']
        nome = received['nome']
        formID = received['formacao']
        formacao = get_object_or_404(models.Formacao, id=formID)

        if models.Atleta.objects.filter(licenca=licenca).count() == 0:
            models.Atleta.objects.create(nome=nome, formacao=formacao, licenca=licenca, camisola=camisola)
            return HttpResponse('ok')
        else:
            return HttpResponseBadRequest(content='atleta already exists')
    else:
        return HttpResponseBadRequest(content='bad form')


#@login_required
#@permission_required('change_atleta', raise_exception=True)
@csrf_exempt
def cAtletaView(request):
    if request.method=='POST':
        received = json.loads(request.body.decode('utf-8'))
        
        licenca = received['licenca']
        formID = received['formacao']
        formacao = get_object_or_404(models.Formacao, id=formID)

        if models.Atleta.objects.filter(licenca=licenca).count() == 0:
            return HttpResponseBadRequest(content='atleta does not exists')
        else:
            models.Atleta.objects.filter(licenca=licenca).update(formacao=formacao)
            return HttpResponse('ok')  
    else:
        return HttpResponseBadRequest(content='bad form')


#@login_required
#@permission_required('view_atleta', raise_exception=True)
def gAtletasView(request, formacao):
    formacaox = models.Atleta.objects.filter(formacao=formacao).order_by('camisola')
    atletas = []

    for atleta in formacaox:
        new_atleta = {}
        new_atleta['licenca'] = atleta.licenca
        new_atleta['id'] = atleta.id
        new_atleta['nome'] = atleta.nome
        new_atleta['camisola'] = atleta.camisola
        atletas.append(new_atleta)

    return JsonResponse(atletas, safe=False)


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
                new_atleta['camisola'] = atleta.camisola
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
                new_atleta['camisola'] = atleta.camisola
                new_atleta['nome'] = atleta.nome
                aux.append(new_atleta)

    return JsonResponse(aux, safe=False)


#@login_required
#@permission_required('add_tecnico', raise_exception=True)
@csrf_exempt
def tecnicoView(request):
    if request.method=='POST':
        received = json.loads(request.body.decode('utf-8'))
        
        email = received['email']
        password = received['password']
        nome = received['nome']
        clubeID = received['clube']
        clube = get_object_or_404(models.Clube, id=clubeID)

        if models.Tecnico.objects.filter(email=email).count() == 0:
            group = Group.objects.get(name='Tecnico')
            user = User.objects.create_user(first_name=nome, username=email, email=email, password=password)
            user.save()
            user.groups.add(group)
            models.Tecnico.objects.create(email=email, clube=clube)
            return HttpResponse('ok')
        else:
            return HttpResponseBadRequest(content='tecnico already exists')
    else:
        return HttpResponseBadRequest(content='bad form')


@login_required
@permission_required('change_tecnico', raise_exception=True)
def cTecnicoView(request, id, grelhaC, grelhaB):
    models.Tecnico.objects.filter(id=id).update(grelhaCampo=grelhaC, grelhaB=grelhaB)
    return HttpResponse('ok')


#@login_required
#@permission_required('add_jogo', raise_exception=True)
@csrf_exempt
def jogoView(request):
    if request.method=='POST':
        received = json.loads(request.body.decode('utf-8'))
        
        numero = received['numero']
        casa = received['casa']
        data = received['data']
        hora = received['hora']
        tipo = received['tipo']
        formID = received['formacao']
        formacao = get_object_or_404(models.Formacao, id=formID)
        formAdvID = received['formacaoAdv']
        formacaoAdv = get_object_or_404(models.Formacao, id=formAdvID)

        models.Jogo.objects.create(tipo=tipo, formacao=formacao, adversario=formacaoAdv, casa=casa, data=data, hora=hora, numero=numero, grelhaCampo="8x4", grelhaBaliza="3x3")
        return HttpResponse('ok')
    else:
        return HttpResponseBadRequest(content='bad form')


@login_required
@permission_required('change_jogo', raise_exception=True)
#nao esta atualizado com todos os novos camos de um jogo
def cJogoView(request, idJogo, grelhaC, grelhaB):
    models.Jogo.objects.filter(id=idJogo).update(grelhaCampo=grelhaC, grelhaBaliza=grelhaB)
    return HttpResponse('ok')


#@login_required
#@permission_required('change_jogo', raise_exception=True)
def endJogoView(request, id):
    models.Jogo.objects.filter(id=id).update(ativo=False)
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
                new_jogo['c'] = "C"
                new_jogo['casa'] ="CASA"
            else:
                new_jogo['c'] = "F"
                new_jogo['casa'] ="FORA"
            new_jogo['ativo'] = jogo.ativo
            new_jogo['data'] = jogo.data
            new_jogo['hora'] = jogo.hora
            new_jogo['resultado'] = gResultado(jogo.id)
            new_jogo['grelhaCampo'] = jogo.grelhaCampo
            new_jogo['grelhaBaliza'] = jogo.grelhaBaliza
            new_jogo['adversario'] = jogo.adversario.id
            new_jogo['formacao'] = jogo.formacao.id
            new_jogo['adv_nome'] = jogo.adversario.clube.nome
            new_jogo['form_nome'] = jogo.formacao.nome
            new_jogo['duracao'] = jogo.duracao
            new_jogo['partes'] = jogo.partes
            new_jogo['convocados'] = jogo.convocados
            aux.append(new_jogo)
    return JsonResponse(aux, safe=False)

def adversario(form_id):
    formacao = get_object_or_404(models.Formacao, id=form_id)
    return formacao.clube


#@login_required
#@permission_required('view_jogo', raise_exception=True)
@csrf_exempt
def gJogoView(request, id):
    jogo = get_object_or_404(models.Jogo, id=id)
    new_jogo = {}
    new_jogo['id'] = jogo.id
    new_jogo['numero'] = jogo.numero
    new_jogo['tipo'] = jogo.tipo
    if(jogo.casa):
        new_jogo['c'] = "C"
        new_jogo['casa'] ="CASA"
    else:
        new_jogo['c'] = "F"
        new_jogo['casa'] ="FORA"
    new_jogo['data'] = jogo.data
    new_jogo['hora'] = jogo.hora.strftime('%H:%M')
    new_jogo['resultado'] = gResultado(jogo.id)
    new_jogo['ativo'] = jogo.ativo
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
    new_jogo['duracao'] = jogo.duracao
    new_jogo['partes'] = jogo.partes
    
    return JsonResponse(new_jogo)


def confirmConvocadosView(request, id):
    models.Jogo.objects.filter(id=id).update(convocados=False)
    return HttpResponse('ok')


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


@csrf_exempt
def convocadosView(request):
    if request.method=='POST':
        received = json.loads(request.body.decode('utf-8'))

        atletas = received['atletas']
        inicial = received['inicial']
        jogo = models.Jogo.objects.get(id=received['jogo'])

        for atleta in atletas:
            convocado = models.Atleta.objects.get(id=atleta['id'])
            convocado.camisola = atleta['camisola']
            convocado.save()

            if atleta in inicial:
                models.Convocado.objects.create(atleta=convocado, jogo=jogo, emCampo=True)

            else:
                models.Convocado.objects.create(atleta=convocado, jogo=jogo, emCampo=False)

        jogo.convocados = False
        jogo.save()

        return HttpResponse('ok')
    else:
        return HttpResponseBadRequest(content='bad form')


#@login_required
#@permission_required('add_evento', raise_exception=True)
@csrf_exempt
def eventoView(request):
    if request.method=='POST':
        received = json.loads(request.body.decode('utf-8'))

        tp = get_object_or_404(models.TipoEvento, id=received['tipo'])
        jg = get_object_or_404(models.Jogo, id=received['jogo'])
        inst = received['instante']
        pt = received['parte']
        eq = received['equipa']
        at1 = received['atleta1']
        at2 = received['atleta2']
        zC = received['zonaC']
        zB = received['zonaB']
        novo = received['novoinst']

        if tp.id == 16 and novo is not None:
            print(novo)
            models.Evento.objects.create(tipo=tp, jogo=jg, instante=inst, novoinstante=novo, parte=pt)

        elif eq is not None:
            equipa = get_object_or_404(models.Formacao, id=eq)
            if at1 is not None:
                atleta1 = get_object_or_404(models.Atleta, id=at1)
                if at2 is not None:
                    atleta2 = get_object_or_404(models.Atleta, id=at2)
                    models.Evento.objects.create(tipo=tp, jogo=jg, equipa=equipa, atleta1=atleta1, atleta2=atleta2, instante=inst, parte=pt)
                    models.Convocado.objects.filter(atleta=atleta1, jogo=jg).update(emCampo=False)
                    models.Convocado.objects.filter(atleta=atleta2, jogo=jg).update(emCampo=True)
                elif zC is not None:
                    if zB is not None:
                        models.Evento.objects.create(tipo=tp, jogo=jg, equipa=equipa, atleta1=atleta1, zonaCampo=zC, zonaBaliza=zB, instante=inst, parte=pt)
                    else:
                        models.Evento.objects.create(tipo=tp, jogo=jg, equipa=equipa, atleta1=atleta1, zonaCampo=zC, instante=inst, parte=pt)
            else:
                models.Evento.objects.create(tipo=tp, jogo=jg, equipa=equipa, instante=inst, parte=pt)

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
        zC = received['zonaCampo']
        zB = received['zonaBaliza']
        novo = received['novoinstante']
        pt = received['parte']
        jg = get_object_or_404(models.Jogo, id=received['jogo'])

        if inst is not None:
            models.Evento.objects.filter(id=i).update(instante=inst)
        if pt is not None:
            models.Evento.objects.filter(id=i).update(parte=pt)
        if novo is not None:
            models.Evento.objects.filter(id=i).update(instante=inst, novoinstante=novo)
        if eq is not None:
            models.Evento.objects.filter(id=i).update(equipa=eq)
        if at1 is not None:
            atleta1 = get_object_or_404(models.Atleta, id=at1)
            models.Evento.objects.filter(id=i).update(atleta1=atleta1)
            if at2 is not None:
                atleta2 = get_object_or_404(models.Atleta, id=at2)
                models.Evento.objects.filter(id=i).update(atleta2=atleta2)
                models.Convocado.objects.filter(atleta=atleta1, jogo=jg).update(emCampo=False)
                models.Convocado.objects.filter(atleta=atleta2, jogo=jg).update(emCampo=True)
        if zC is not None:
            models.Evento.objects.filter(id=i).update(zonaCampo=zC)
        if zB is not None:
            models.Evento.objects.filter(id=i).update(zonaBaliza=zB)

        return HttpResponse('ok')
    else:
        return HttpResponseBadRequest(content='bad form')


#@login_required
#@permission_required('delete_evento', raise_exception=True)
def dEventoView(request, id):
    evento = get_object_or_404(models.Evento, id=id)
    evento.delete()
    return HttpResponse('ok')


#@login_required
#@permission_required('delete_evento', raise_exception=True)
def sinalizarEventoView(request, id):
    evento = get_object_or_404(models.Evento, id=id)

    if evento.sinalizado:
        models.Evento.objects.filter(id=id).update(sinalizado=False)
    else:
        models.Evento.objects.filter(id=id).update(sinalizado=True)
    return HttpResponse('ok')


#@login_required
#@permission_required('view_evento', raise_exception=True)
def gEventoView(request, id):
    evento = get_object_or_404(models.Evento, id=id)
    
    new_evento = {}
    new_evento['id'] = evento.id
    new_evento['jogo'] = evento.jogo.id
    new_evento['tipo'] = evento.tipo.id
    new_evento['equipa'] = evento.equipa.id

    if evento.atleta1 :
        new_evento['atleta1'] = evento.atleta1.id
    else:
        new_evento['atleta1'] = None

    if evento.atleta2 :
        new_evento['atleta2'] = evento.atleta2.id
    else:
        new_evento['atleta2'] = None

    if evento.novoinstante :
        new_evento['novoinstante'] = evento.novoinstante
    else:
        new_evento['novoinstante'] = None

    new_evento['instante'] = evento.instante
    new_evento['timestamp'] = evento.timestamp
    new_evento['parte'] = evento.parte
    new_evento['sinalizado'] = evento.sinalizado
    
    if evento.zonaCampo :
        new_evento['zonaCampo'] = evento.zonaCampo
    else:
        new_evento['zonaCampo'] = None

    if evento.zonaBaliza :
        new_evento['zonaBaliza'] = evento.zonaBaliza
    else:
        new_evento['zonaBaliza'] = None

    return JsonResponse(new_evento, safe=False)



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
        new_evento['tipo'] = evento.tipo.tipo
        if(evento.equipa):
            new_evento['equipa'] = evento.equipa.clube.nome
        else:
            new_evento['equipa'] = " - "

        if(evento.atleta1):
            new_evento['atleta1'] = evento.atleta1.nome
        else:
            new_evento['atleta1'] = " - "

        if(evento.atleta2):
            new_evento['atleta2'] = evento.atleta2.nome
        else:
            new_evento['atleta2'] = " - "
        
        new_evento['instante'] = evento.instante
        
        if(evento.novoinstante):
            new_evento['novoinstante'] = evento.novoinstante
        else:
            new_evento['novoinstante'] = " - "
        
        new_evento['timestamp'] = evento.timestamp
        new_evento['parte'] = evento.parte
        new_evento['sinalizado'] = evento.sinalizado
        
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


#@login_required
#@permission_required('add_tipoevento', raise_exception=True)
@csrf_exempt
def tipoEventoView(request):
    if request.method=='POST':
        received = json.loads(request.body.decode('utf-8'))
        
        tipo = received['tipo']
        equipa = received['equipa']
        atleta1 = received['atleta1']
        atleta2 = received['atleta2']
        zonaC = received['zonaC']
        zonaB = received['zonaB']
        novoinst = received['novoinst']

        if models.TipoEvento.objects.filter(tipo=tipo).count() == 0:
            models.TipoEvento.objects.create(tipo=tipo, equipa=equipa, atleta1=atleta1, atleta2=atleta2, zonaCampo=zonaC, zonaBaliza=zonaB, novoinstante=novoinst)
            return HttpResponse('ok')
        else:
            return HttpResponseBadRequest(content='tipo already exists')
    else:
        return HttpResponseBadRequest(content='bad form')

    


#@login_required
#@permission_required('view_tipoevento', raise_exception=True)
@csrf_exempt
def gTipoEventoView(request, id):
    tipoe = get_object_or_404(models.TipoEvento, id=id)
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


#@login_required
#@permission_required('add_tiposselecionados', raise_exception=True)
def tipoSelecionadoView(request, tipo, email):
    tecnico = get_object_or_404(models.Tecnico, email=email)
    tipoE = get_object_or_404(models.TipoEvento, id=tipo)

    if models.TiposSelecionados.objects.filter(tecnico=tecnico, tipo=tipoE).count() == 0:
    	models.TiposSelecionados.objects.create(tecnico=tecnico, tipo=tipoE)

    return HttpResponse('ok')


#@login_required
#@permission_required('delete_tiposselecionados', raise_exception=True)
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
        new_tipo['id'] = t.id
        new_tipo['idEvento'] = tipox.id
        new_tipo['tipo'] = tipox.tipo
        aux.append(new_tipo)

    return JsonResponse(aux, safe=False)

