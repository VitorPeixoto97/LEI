from django.urls import include, path, register_converter
from . import views

app_name = 'server'
urlpatterns = [
    path('info_user/<str:email>/', views.infoUserView, name='info'),
    path('adversario_nome/<int:form_id>/', views.advNome, name='adversarionome'),

    path('clube/', views.clubeView, name='clube'),
    path('get_clubes/', views.gClubesView, name='gclubes'),

    path('gestor/', views.gestorView, name='gestor'),

    path('formacao/', views.formacaoView, name='formacao'),
    path('get_formacoes/<int:clube>/', views.gFormacoesView, name='gformacoes'),

    path('atleta/', views.atletaView, name='atleta'),
    path('change_atleta/', views.cAtletaView, name='catleta'),
    path('get_atletas/<int:formacao>/', views.gAtletasView, name='gatletas'),
    path('get_atletas_campo/<int:formacao>/<int:jogo>/', views.gAtletasEmCampoView, name='gatletascampo'),
    path('get_atletas_suplentes/<int:formacao>/<int:jogo>/', views.gAtletasSuplentesView, name='gatletassuplentes'),

    path('tecnico/', views.tecnicoView, name='tecnico'),
    path('change_tecnico/', views.cTecnicoView, name='ctecnico'),

    path('jogo/', views.jogoView, name='jogo'),
    path('change_jogo/', views.cJogoView, name='cjogo'),
    path('get_jogos/<str:clube>/', views.gJogosView, name='gjogos'),
    path('get_jogo/<int:id>/', views.gJogoView, name='gjogo'),
    path('end_jogo/<int:id>/', views.endJogoView, name='ejogo'),
    path('confirm_convocados/<int:id>/', views.confirmConvocadosView, name='confjogo'),

    path('convocados/', views.convocadosView, name='convocados'),

    path('evento/', views.eventoView, name='evento'),
    path('change_evento/', views.cEventoView, name='cevento'),
    path('del_evento/<int:id>/', views.dEventoView, name='devento'),
    path('sinalizar_evento/<int:id>/', views.sinalizarEventoView, name='sevento'),
    path('get_eventos/<int:idJogo>/', views.gEventosView, name='geventos'),
    path('get_evento/<int:id>/', views.gEventoView, name='gevento'),

    path('tipo_evento/', views.tipoEventoView, name='tipoevento'),
    path('get_tipo_evento/<int:id>/', views.gTipoEventoView, name='gtipoevento'),
    path('get_tipos_eventos/', views.gTiposEventosView, name='gtiposeventos'),

    path('tipo_selecionado/<int:tipo>/<str:email>/', views.tipoSelecionadoView, name='tiposelecionado'),
    path('del_tipo_selecionado/<int:id>/', views.dTipoSelecionadoView, name='dtiposelecionado'),
    path('get_tipos_selecionados/<str:email>/', views.gTiposSelecionadosView, name='gtiposselecionados'),
]
