from django.urls import path

from . import views

app_name = 'statsapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('/change_admin/<string:email>/<string:password>/', views.cAdminView, name='cadmin'),

    path('/clube/<string:nome>/<string:cor>/<string:simbolo>/', views.clubeView, name='clube'),
    # não meti o change clube, porque fiquei na dúvida se não se pode usar o de cima
    path('/get_clube/<string:nome>/', views.gCLubeView, name='gclube'),

    path('/gestor/<string:clube>/<string:email>/<string:nome>/<string:password>/', views.gestorView, name='gestor'),
    path('/change_gestor/<string:email>/<string:password>/', views.cGestorView, name='cgestor'),

    path('/formacao/<string:clube>/<string:nome>/', views.formacaoView, name='formacao'),
    path('/del_formacao/<string:clube>/<string:nome>/', views.dFormacaoView, name='dformacao'),
    path('/get_formacao/<string:clube>/<string:nome>/', views.gFormacaoView, name='gformacao'),

    path('/atleta/<string:clube>/<int:licenca>/<string:nome>/<string:formacao>/<int:camisola>/', views.atletaView, name='atleta'),
    path('/change_atleta/<int:licenca>/<string:formacao>/<int:camisola>/', views.cAtletaView, name='catleta'),
    path('/del_atleta/<int:licenca>/', views.dAtletaView, name='datleta'),
    path('/get_atleta/<int:licenca>/', views.gAtleta, name='gatleta'),

    path('/tecnico/<string:clube>/<string:email>/<string:nome>/<string:password>/', views.tecnicoView, name='tecnico'),
    path('/change_tecnico/<string:email>/<string:password>/<string:grelhaC>/<string:grelhaB>/', views.cTecnicoView, name='ctecnico'),
    path('/get_tecnico/<string:email>/', views.gTecnico, name='gtecnico'),

    path('/jogo/<string:clube>/<string:formacao>/<string:clubeAdv>/<string:formacaoAdv>/<boolean:casa>/<date:data>/<time:hora>/<string:tipo>/', views.jogoView, name='jogo'),
    path('/change_jogo/<int:idJogo>/<string:grelhaC>/<string:grelhaB>/', views.cJogoView, name='cjogo'),
    path('/get_jogo/<string:clube>/<string:formacao>/<date:data>/<time:hora>/', views.gJogoView, name='gjogo'),

    path('/convocado/<int:idJogo>/<int:licenca>/<boolean:emCampo>/', views.convocadoView, name='convocado'),
    # não meti o change_convocado, porque fiquei na dúvida se não se pode usar o de cima
    path('/get_convocados/<int:idJogo>/', views.gConvocadosView, name='gconvocados'),
    # não fiz o get_convocado para um jogador em específico, porque não vi utilidade

    path('/evento/<int:idJogo>/<int:idEquipa>/<string:tipo>/<int:atleta1>/<int:atleta2>/<int:zonaC>/<int:zonaB>/<time:instante>/<time:novoinst>/', views.eventoView, name='evento'),
    # não meti o change evento, porque fiquei na dúvida se não se pode usar o de cima
    path('/del_evento/<int:idJogo>/<string:tipo>/<time:instante>/', views.dEventoView, name='devento'),
    path('/get_evento/<int:idJogo>/<string:tipo>/<time:instante>/', views.gEventoView, name='gevento'),
    path('/get_eventos/<int:idJogo>/', views.gEventosView, name='geventos'),

    path('/tipo_evento/<string:tipo>/<boolean:atleta1>/<boolean:atleta2>/<boolean:zonaC>/<boolean:<zonaB>/<boolean:novoinst>/', views.tipoEventoView, name='tipoevento'),
    path('/get_tipos_eventos/', views.gTiposEventosView, name='gtiposeventos'),

    path('/tipo_selecionado/<string:tipo>/<string:email>/', views.tipoSelecionadoView, name='tiposelecionado'),
    path('/del_tipo_selecionado/<string:tipo>/<string:email>/', views.dTipoSelecionadoView, name='dtiposelecionado'),
    path('/get_tipos_selecionados/<string:email>', views.gTiposSelecionadosView, name='gtiposselecionados'),
]