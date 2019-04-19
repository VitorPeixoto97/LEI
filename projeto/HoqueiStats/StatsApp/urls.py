from django.urls import path, register_converter
from . import converters, views

register_converter(converters.BoolConverter, 'bool')
register_converter(converters.DateConverter, 'date')
register_converter(converters.TimeConverter, 'time')

app_name = 'statsapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('change_admin/<str:email>/<str:password>/', views.cAdminView, name='cadmin'),

    path('clube/<str:nome>/<str:cor>/<str:simbolo>/', views.clubeView, name='clube'),
    # não meti o change clube, porque fiquei na dúvida se não se pode usar o de cima
    path('get_clube/<str:nome>/', views.gCLubeView, name='gclube'),

    path('gestor/<str:clube>/<str:email>/<str:nome>/<str:password>/', views.gestorView, name='gestor'),
    path('change_gestor/<str:email>/<str:password>/', views.cGestorView, name='cgestor'),

    path('formacao/<str:clube>/<str:nome>/', views.formacaoView, name='formacao'),
    path('del_formacao/<str:clube>/<str:nome>/', views.dFormacaoView, name='dformacao'),
    path('get_formacao/<str:clube>/<str:nome>/', views.gFormacaoView, name='gformacao'),

    path('atleta/<str:clube>/<int:licenca>/<str:nome>/<str:formacao>/<int:camisola>/', views.atletaView, name='atleta'),
    path('change_atleta/<int:licenca>/<str:formacao>/<int:camisola>/', views.cAtletaView, name='catleta'),
    path('del_atleta/<int:licenca>/', views.dAtletaView, name='datleta'),
    path('get_atleta/<int:licenca>/', views.gAtleta, name='gatleta'),

    path('tecnico/<str:clube>/<str:email>/<str:nome>/<str:password>/', views.tecnicoView, name='tecnico'),
    path('change_tecnico/<str:email>/<str:password>/<str:grelhaC>/<str:grelhaB>/', views.cTecnicoView, name='ctecnico'),
    path('get_tecnico/<str:email>/', views.gTecnico, name='gtecnico'),

    path('jogo/<str:clube>/<str:formacao>/<str:clubeAdv>/<str:formacaoAdv>/<bool:casa>/<date:data>/<time:hora>/<str:tipo>/', views.jogoView, name='jogo'),
    path('change_jogo/<int:idJogo>/<str:grelhaC>/<str:grelhaB>/', views.cJogoView, name='cjogo'),
    path('get_jogo/<str:clube>/<str:formacao>/<date:data>/<time:hora>/', views.gJogoView, name='gjogo'),

    path('convocado/<int:idJogo>/<int:licenca>/<bool:emCampo>/', views.convocadoView, name='convocado'),
    # não meti o change_convocado, porque fiquei na dúvida se não se pode usar o de cima
    path('get_convocados/<int:idJogo>/', views.gConvocadosView, name='gconvocados'),
    # não fiz o get_convocado para um jogador em específico, porque não vi utilidade

    path('evento/<int:idJogo>/<int:idEquipa>/<str:tipo>/<int:atleta1>/<int:atleta2>/<int:zonaC>/<int:zonaB>/<time:instante>/<time:novoinst>/', views.eventoView, name='evento'),
    # não meti o change evento, porque fiquei na dúvida se não se pode usar o de cima
    path('del_evento/<int:idJogo>/<str:tipo>/<time:instante>/', views.dEventoView, name='devento'),
    path('get_evento/<int:idJogo>/<str:tipo>/<time:instante>/', views.gEventoView, name='gevento'),
    path('get_eventos/<int:idJogo>/', views.gEventosView, name='geventos'),

    path('tipo_evento/<str:tipo>/<bool:atleta1>/<bool:atleta2>/<bool:zonaC>/<bool:<zonaB>/<bool:novoinst>/', views.tipoEventoView, name='tipoevento'),
    path('get_tipos_eventos/', views.gTiposEventosView, name='gtiposeventos'),

    path('tipo_selecionado/<str:tipo>/<str:email>/', views.tipoSelecionadoView, name='tiposelecionado'),
    path('del_tipo_selecionado/<str:tipo>/<str:email>/', views.dTipoSelecionadoView, name='dtiposelecionado'),
    path('get_tipos_selecionados/<str:email>', views.gTiposSelecionadosView, name='gtiposselecionados'),
]