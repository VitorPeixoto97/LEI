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
        </v-card>
      </v-container>

      <v-container text-xs-left>
        <v-card color="white" class="my-card">
          <div class="row">
            <div class="column" v-if="selecionar">
              <li v-if="tiposEventos != null" v-for="tipoE in tiposEventos">
                <b>{{tipoE.id}}</b> {{tipoE.tipo}}
              </li>
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

    userTecnico(){
      if(this.$session.get('user_info').tipo == "tecnico")
        return true;
      else return false;
    }
  }
}
</script>


<style scoped>
</style>
