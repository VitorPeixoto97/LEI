<template>
  <layout-basic>
    <div>
      <v-container text-xs-left>
        <v-card color="white" class="my-card">
          <div class="row">
            <div class="column" style="margin:auto">
              <img class="crest" :src="logo" v-if="logo != null" style="width: 15%">
            </div>
            <div class="column" style="margin:auto">
              <h3>{{this.$session.get('user_info').nome}}</h3>
              <p>{{this.$session.get('user_info').email}}</p>
            </div>
          </div>
          <div class="row" v-if="userTecnico()">
            <div class="column" style="margin:auto">
              <h4>Tipos de Eventos Selecionados</h4>
              <md-table v-model="searched" md-sort="idEvento" md-sort-order="asc"  md-fixed-header ref="table">
                <md-table-toolbar>
                  <div class="md-toolbar-section-start">
                    <h1 class="md-title"> </h1>
                  </div>
                </md-table-toolbar>

                <md-table-empty-state
                  md-label="Sem tipos"
                  :md-description="'0 tipos de eventos selecionados'">
                </md-table-empty-state>

                <md-table-row slot="md-table-row" slot-scope="{ item }" style="cursor:pointer">
                  <md-table-cell md-label="ID" md-sort-by="idEvento">{{ item.idEvento }}</md-table-cell>
                  <md-table-cell md-label="Tipo de Evento" md-sort-by="tipo">{{ item.tipo }}</md-table-cell>
                  <md-table-cell md-label="">
                    <md-button class="md-icon-button md-raised" v-on:click="removeSelecionado(item.id)">
                      <i class="material-icons">close</i>
                    </md-button>
                  </md-table-cell>
                </md-table-row>
              </md-table>
            </div>
            <div class="column" style="margin:auto">
              <p class="justify-center" style="margin:auto">
                <button class="btn btn-lg btn-primary btn-block text-uppercase btn-timer" style="margin:auto" :disabled="selecionar || criar" @click="selecionar = true">Selecionar Tipo Evento</button>
                <button class="btn btn-lg btn-primary btn-block text-uppercase btn-timer" style="margin:auto" :disabled="selecionar || criar" @click="criar = true">Criar Tipo Evento</button>
              </p>
            </div>
          </div>

          <div class="row" v-if="userGestor()">
            <div class="column" style="margin:auto">
              <p class="justify-center" style="margin:auto">
                <button class="btn btn-lg btn-primary btn-block text-uppercase btn-timer" style="margin:auto" :disabled="criarAtleta || criarGestor || criarTecnico || criarFormacao || alterarFormacao" @click="criarGestor = true">Adicionar Gestor</button>
                <button class="btn btn-lg btn-primary btn-block text-uppercase btn-timer" style="margin:auto" :disabled="criarAtleta || criarGestor || criarTecnico || criarFormacao || alterarFormacao" @click="criarTecnico = true">Adicionar Técnico</button>
                <button class="btn btn-lg btn-primary btn-block text-uppercase btn-timer" style="margin:auto" :disabled="criarAtleta || criarGestor || criarTecnico || criarFormacao || alterarFormacao" @click="criarAtleta = true">Adicionar Atleta</button>
                <button class="btn btn-lg btn-primary btn-block text-uppercase btn-timer" style="margin:auto" :disabled="criarAtleta || criarGestor || criarTecnico || criarFormacao || alterarFormacao" @click="criarFormacao = true">Adicionar Formacao</button>
                <button class="btn btn-lg btn-primary btn-block text-uppercase btn-timer" style="margin:auto" :disabled="criarAtleta || criarGestor || criarTecnico || criarFormacao || alterarFormacao" @click="alterarFormacao = true">Mudar Formação Atleta</button>
              </p>
            </div>
          </div>
        </v-card>
      </v-container>

      <v-container text-xs-left>
        <v-card color="white" class="my-card">
          <div class="row">
            <div class="column" v-if="selecionar">
              <div class="column">
                <li v-if="tiposEventos != null" v-for="tipoE in tiposEventos">
                  <b>{{tipoE.id}}</b> {{tipoE.tipo}}
                </li>
              </div>
              <div class="column">
                <form class="review-form" @submit.prevent="submitSelecionado">
                  <div class="field">
                    <input v-model="selecionado" class="input" type="text" placeholder="Identificador do evento">
                    <input type="submit" value="Confirmar">
                    <button @click="selecionar = false, selecionado = null">Cancelar</button>
                  </div>
                </form>
              </div>
            </div>
            <div class="column" v-if="criar">
              <div class="column">
                <form class="review-form" @submit.prevent="submitNovoTipo">
                  <div class="field">
                    <input v-model="novoTipo.tipo" class="input" type="text" placeholder="Tipo de evento">
                    <input v-model="novoTipo.equipa" type="checkbox">equipa<br>
                    <input v-model="novoTipo.atleta1" type="checkbox">atleta<br>
                    <input v-model="novoTipo.atleta2" type="checkbox">atleta suplente<br>
                    <input v-model="novoTipo.zonaC" type="checkbox">zona de campo<br>
                    <input v-model="novoTipo.zonaB" type="checkbox">zona de baliza<br>
                    <input v-model="novoTipo.novoinst" type="checkbox">novo instante<br>
                    <input type="submit" value="Confirmar">
                    <button @click="criar = false, novoTipo.tipo = null, novoTipo.equipa = false, novoTipo.atleta1 = false, novoTipo.atleta2 = false, novoTipo.zonaCampo = false, novoTipo.zonaBaliza = false, novoTipo.novoinstante = false">Cancelar</button>
                  </div>
                </form>
              </div>
            </div>
            <div class="column" v-if="criarAtleta">
              <div class="column">
                <li v-if="formacoes != null" v-for="formacao in formacoes">
                  <b>{{formacao.id}}</b> {{formacao.nome}}
                </li>
              </div>
              <div class="column">
                <form class="review-form" @submit.prevent="submitAtleta">
                  <div class="field">
                    <input v-model="atleta.licenca" class="input" type="text" placeholder="Número de licença" v-on:keyup.down="$event.target.nextElementSibling.focus()" v-on:keyup.up="$event.target.previousElementSibling.focus()">
                    <input v-model="atleta.nome" class="input" type="text" placeholder="Nome" v-on:keyup.down="$event.target.nextElementSibling.focus()" v-on:keyup.up="$event.target.previousElementSibling.focus()">
                    <input v-model="atleta.camisola" class="input" type="text" placeholder="Número de camisola" v-on:keyup.down="$event.target.nextElementSibling.focus()" v-on:keyup.up="$event.target.previousElementSibling.focus()">
                    <input v-model="atleta.formacao" class="input" type="text" placeholder="ID da formacao" v-on:keyup.down="$event.target.nextElementSibling.focus()" v-on:keyup.up="$event.target.previousElementSibling.focus()">
                    <input type="submit" value="Confirmar">
                    <button @click="criarAtleta = false, atleta.licenca = null, atleta.nome = null, atleta.camisola = null, atleta.formacao = null">Cancelar</button>
                  </div>
                </form>
              </div>
            </div>
            <div class="column" v-if="criarTecnico">
              <div class="column">
                <form class="review-form" @submit.prevent="submitTecnico">
                  <div class="field">
                    <input v-model="tecnico.email" class="input" type="text" placeholder="Email" v-on:keyup.down="$event.target.nextElementSibling.focus()" v-on:keyup.up="$event.target.previousElementSibling.focus()">
                    <input v-model="tecnico.nome" class="input" type="text" placeholder="Nome" v-on:keyup.down="$event.target.nextElementSibling.focus()" v-on:keyup.up="$event.target.previousElementSibling.focus()">
                    <input v-model="tecnico.password" class="input" type="text" placeholder="Password" v-on:keyup.down="$event.target.nextElementSibling.focus()" v-on:keyup.up="$event.target.previousElementSibling.focus()">
                    <input type="submit" value="Confirmar">
                    <button @click="criarTecnico = false, tecnico.email = null, tecnico.nome = null, tecnico.password = null">Cancelar</button>
                  </div>
                </form>
              </div>
            </div>
            <div class="column" v-if="criarGestor">
              <div class="column">
                <form class="review-form" @submit.prevent="submitGestor">
                  <div class="field">
                    <input v-model="gestor.email" class="input" type="text" placeholder="Email" v-on:keyup.down="$event.target.nextElementSibling.focus()" v-on:keyup.up="$event.target.previousElementSibling.focus()">
                    <input v-model="gestor.nome" class="input" type="text" placeholder="Nome" v-on:keyup.down="$event.target.nextElementSibling.focus()" v-on:keyup.up="$event.target.previousElementSibling.focus()">
                    <input v-model="gestor.password" class="input" type="text" placeholder="Password" v-on:keyup.down="$event.target.nextElementSibling.focus()" v-on:keyup.up="$event.target.previousElementSibling.focus()">
                    <input type="submit" value="Confirmar">
                    <button @click="criarGestor = false, gestor.email = null, gestor.nome = null, gestor.password = null">Cancelar</button>
                  </div>
                </form>
              </div>
            </div>
            <div class="column" v-if="criarFormacao">
              <div class="column">
                <form class="review-form" @submit.prevent="submitFormacao">
                  <div class="field">
                    <input v-model="formacao.nome" class="input" type="text" placeholder="Nome da nova formação">
                    <input type="submit" value="Confirmar">
                    <button @click="criarFormacao = false, formacao.nome = null">Cancelar</button>
                  </div>
                </form>
              </div>
            </div>
            <div class="column" v-if="alterarFormacao">
              <div class="column" v-if="selF">
                <li v-if="formacoes != null" v-for="formacao in formacoes">
                  <b>{{formacao.id}}</b> {{formacao.nome}}
                </li>
              </div>
              <div class="column" v-if="selA">
                <li v-if="sugestaoAtletas != null" v-for="atleta in sugestaoAtletas">
                  <b>{{atleta.licenca}}</b> {{atleta.nome}}
                </li>
              </div>
              <div class="column">
                <form class="review-form" @submit.prevent="submitAlteracao">
                  <div class="field">
                    <input v-model="antigaFormacao" class="input" type="text" placeholder="Formação atual" v-on:keyup.down="$event.target.nextElementSibling.focus()" v-on:keyup.up="$event.target.previousElementSibling.focus()" v-on:focus="selF=true, selA=false">
                    <input v-model="novoAtleta.licenca" class="input" type="text" placeholder="Número de licença do atleta" v-on:keyup.down="$event.target.nextElementSibling.focus()" v-on:keyup.up="$event.target.previousElementSibling.focus()" v-on:focus="selF=false, selA=true, getAtletas()">
                    <input v-model="novoAtleta.formacao" class="input" type="text" placeholder="Nova formação" v-on:keyup.down="$event.target.nextElementSibling.focus()" v-on:keyup.up="$event.target.previousElementSibling.focus()" v-on:focus="selF=true, selA=false">
                    <input type="submit" value="Confirmar">
                    <button @click="alterarFormacao = false, selA = false, selF = false, sugestaoAtletas = null, novoAtleta.licenca = null, novoAtleta.formacao = null, antigaFormacao = null">Cancelar</button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </v-card>
      </v-container>
      <br>
      <br>
      <br>
    </div>
  </layout-basic>
</template>

<script>
import router from "../../router";
import LayoutBasic from '../layouts/Basic.vue'
import PlusMinusField from '../helpers/PlusMinusField.vue'
import axios from 'axios';

export default {
  name: 'Jogo',
  components: {
    LayoutBasic,
    'plusminsfield': PlusMinusField
  },
  data() {
    return {
      logo: null,
      selecionar: false,
      criar: false,
      tiposEventos: null,
      tiposSelecionados: null,
      searched: [],
      selecionado: null,
      novoTipo: {
        tipo: null,
        equipa: false,
        atleta1: false,
        atleta2: false,
        zonaC: false,
        zonaB: false,
        novoinst: false
      },

      formacoes: null,
      criarGestor: false,
      criarTecnico: false,
      criarAtleta: false,
      criarFormacao: false,
      alterarFormacao: false,
      selA: false,
      selF: false,
      sugestaoAtletas: null,
      antigaFormacao: null,
      atleta: {
        licenca: null,
        nome: null,
        camisola: null,
        formacao: null
      },
      tecnico: {
        email: null,
        nome: null,
        password: null,
        clube: null
      },
      gestor: {
        email: null,
        nome: null,
        password: null,
        clube: null
      },
      formacao: {
        clube: null,
        nome: null
      },
      novoAtleta: {
        licenca: null,
        formacao: null
      }
    }
  },
  mounted: function() {
    this.checkLoggedIn();
    this.FetchData();
    this.logo = this.$session.get('user_info').clube_logo;
  },
  methods: {
    checkLoggedIn() {
      if (!this.$session.has('token')) {
        router.push("/auth");
      }
    },

    FetchData: function() {
      var app = this;
      axios.get(process.env.API_URL + "/server/get_tipos_eventos/").then(response => {
        app.tiposEventos = response.data;
      });
      axios.get(process.env.API_URL + "/server/get_tipos_selecionados/" + this.$session.get('user_email') + "/").then(response => {
        app.tiposSelecionados = response.data;
        app.searched = app.tiposSelecionados;
      });
      axios.get(process.env.API_URL + "/server/get_formacoes/" + this.$session.get('user_info').clube + "/").then(response => {
        app.formacoes = response.data;
      })
    },

    submitSelecionado(){
      axios.get(process.env.API_URL + "/server/tipo_selecionado/" + this.selecionado + "/" + this.$session.get('user_email') + "/").then(response => {
        router.push('/definicao');
        this.updateTiposSelecionados();
        this.selecionado = null;
        this.selecionar = false;
      })
    },

    submitNovoTipo(){
      if(this.novoTipo.tipo != null){
        axios.post(process.env.API_URL + "/server/tipo_evento/", JSON.stringify(this.novoTipo)).then(response => {
          router.push('/definicao');
          this.updateTipos();
          this.novoTipo.tipo = null;
          this.novoTipo.equipa = false;
          this.novoTipo.atleta1 = false;
          this.novoTipo.atleta2 = false;
          this.novoTipo.zonaCampo = false;
          this.novoTipo.zonaBaliza = false;
          this.novoTipo.novoinstante = false;
          this.criar = false;
        })
      }
    },

    submitAtleta(){
      if(this.atleta.licenca != null && this.atleta.nome != null && this.atleta.camisola != null && this.atleta.formacao != null){
        axios.post(process.env.API_URL + "/server/atleta/", JSON.stringify(this.atleta)).then(response => {
          router.push('/definicao');
          this.atleta.licenca = null;
          this.atleta.nome = null;
          this.atleta.camisola = null;
          this.atleta.formacao = null;
          this.criarAtleta = false;
        })
      }
    },

    submitTecnico(){
      if(this.tecnico.email != null && this.tecnico.nome != null && this.tecnico.password != null){
        this.tecnico.clube = this.$session.get('user_info').clube;
        axios.post(process.env.API_URL + "/server/tecnico/", JSON.stringify(this.tecnico)).then(response => {
          router.push('/definicao');
          this.tecnico.email = null;
          this.tecnico.nome = null;
          this.tecnico.password = null;
          this.tecnico.clube = null;
          this.criarTecnico= false;
        })
      }
    },

    submitGestor(){
      if(this.gestor.email != null && this.gestor.nome != null && this.gestor.password != null){
        this.gestor.clube = this.$session.get('user_info').clube;
        axios.post(process.env.API_URL + "/server/gestor/", JSON.stringify(this.gestor)).then(response => {
          router.push('/definicao');
          this.gestor.email = null;
          this.gestor.nome = null;
          this.gestor.password = null;
          this.gestor.clube = null;
          this.criarGestor= false;
        })
      }
    },

    submitFormacao(){
      if(this.formacao.nome != null){
        this.formacao.clube = this.$session.get('user_info').clube;
        axios.post(process.env.API_URL + "/server/formacao/", JSON.stringify(this.formacao)).then(response => {
          router.push('/definicao');
          this.updateFormacoes();
          this.formacao.nome = null;
          this.formacao.clube = null;
          this.criarFormacao = false;
        })
      }
    },

    submitAlteracao(){
      if(this.novoAtleta.licenca != null && this.novoAtleta.formacao != null){
        axios.post(process.env.API_URL + "/server/change_atleta/", JSON.stringify(this.novoAtleta)).then(response => {
          router.push('/definicao');
          this.antigaFormacao = null;
          this.novoAtleta.licenca = null;
          this.novoAtleta.formacao = null;
          this.sugestaoAtletas = null;
          this.alterarFormacao = false;
        })
      }
    },

    getAtletas(){
      if(this.antigaFormacao != null){
        axios.get(process.env.API_URL + "/server/get_atletas/" + this.antigaFormacao + "/").then(response => {
          this.sugestaoAtletas = response.data;
        })
      }
    },

    removeSelecionado(id){
      axios.get(process.env.API_URL + "/server/del_tipo_selecionado/" + id + "/").then(response => {
        this.updateTiposSelecionados();
      })
    },

    updateTipos(){
      var app = this;
      axios.get(process.env.API_URL + "/server/get_tipos_eventos/").then(response => {
        app.tiposEventos = response.data;
      });
    },

    updateTiposSelecionados(){
      var app = this;
      axios.get(process.env.API_URL + "/server/get_tipos_selecionados/" + this.$session.get('user_email') + "/").then(response => {
        app.tiposSelecionados = response.data;
        app.searched = app.tiposSelecionados;
      });
    },

    updateFormacoes(){
      axios.get(process.env.API_URL + "/server/get_formacoes/" + this.$session.get('user_info').clube + "/").then(response => {
        app.formacoes = response.data;
      })
    },

    userTecnico(){
      if(this.$session.get('user_info').tipo == "tecnico")
        return true;
      else return false;
    },

    userGestor(){
      if(this.$session.get('user_info').tipo == "gestor")
        return true;
      else return false;
    }
  }
}
</script>


<style scoped>
</style>
