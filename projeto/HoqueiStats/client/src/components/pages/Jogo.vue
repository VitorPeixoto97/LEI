<template>
  <layout-basic>
    <div id="app">
      <v-container  text-xs-center>
        <v-flex xs6 offset-xs3  style="min-width:500px; margin:auto;">
          <v-card color="white" class="my-card">
            <div class="row">
              <div class="column">
                <img :src="jogo.logoMe" style="display:inline-flex; max-width:40%; min-width:60px;">
                <v-card-title primary-title class="justify-center"><h5><b>{{jogo.clube_nome}}</b></h5></v-card-title>
              </div>
              <div class="column">
                <p primary-title class=" justify-center resultado"><b>{{jogo.resultado}}</b>
                <p class="justify-center"><h5><b>{{jogo.data}}</b></h5>
                <p class="justify-center" style="margin-top:-15px;"><h5><b>{{jogo.hora}}</b></h5>
              </div>
              <div class="column">
                <img :src="jogo.logoAdv" style="display:inline-flex; max-width:40%; min-width:60px;">
                <v-card-title primary-title class="justify-center"><h5><b>{{jogo.adv_nome}}</b></h5></v-card-title>
              </div>
            </div>
          </v-card>
        </v-flex>
      </v-container>
      <v-container  text-xs-center>
        <v-flex xs6 offset-xs3  style="min-width:500px; margin:auto;">
          <v-card color="white" class="my-card">
            <div class="row">
              <div class="column">
                <p class="justify-center" style="margin-top:20px;margin-left:20px;">
                  <button class="btn btn-lg btn-primary btn-block text-uppercase" v-on:click="updateClock()" :disabled="change || timer == 0">{{ paused ? 'Start' : 'Stop' }}</button>
                </p>
              </div>
              <div class="column">
                <p class="justify-center"><h5>{{ this.parte }}ª Parte</h5>
                <p class="justify-center"><h5>{{ this.minutos < 10 ? '0' + this.minutos : this.minutos }}:{{ this.segundos < 10 ? '0' + this.segundos : this.segundos }}</h5>
              </div>
              <div class="column">
                <p class="justify-center" style="margin-top:20px;margin-right:20px;"><button class="btn btn-lg btn-primary btn-block text-uppercase" v-on:click="changeClock()" :disabled="!paused || interval == null">{{ this.change ? 'Confirm' : 'Change' }}</button></p>
              </div>
            </div>
          </v-card>
        </v-flex>
      </v-container>
      <v-container text-xs-center v-if="change">
        <v-flex xs6 offset-xs3  style="min-width:500px; margin:auto;">
          <v-card color="white" class="my-card">
            <p class="justify-center" style="font-size: x-large;">
              <input type="number" v-model="clockChange.minutos" name="time_m" id="min" min="0" max="19" style="width: 10%;">:
              <input type="number" v-model="clockChange.segundos" name="time_s" id="sec" min="0" max="59" style="width: 10%;"> 
              <input type="number" v-model="clockChange.parte" name="part" id="part" min="1" max="2" style="margin-left:20px;width: 5%;">ª Parte
            </p>
          </v-card>
        </v-flex>
      </v-container>
      <div v-else class="row">
        <div class="column">
          <v-container  text-xs-center>
            <v-flex dist distleft xs6 offset-xs3 style="margin:auto">
              <v-card color="white" class="my-card">
                <div class="row">
                  <div class="column">
                    <v-card-title primary-title class="justify-center"><h5><b>Sugestões de input</b></h5></v-card-title>
                    <div v-if="selT">
                      <li v-for="sugestao in sugestaoTipos">
                        {{sugestao.id}} -> {{sugestao.tipo}}
                      </li>
                    </div>
                    <div v-if="selE">
                      <li>
                        {{jogo.formacao}} -> minha equipa
                      </li>
                      <li>
                        {{jogo.adversario}} -> adversario
                      </li>
                    </div>
                    <div v-if="selA1">
                      <li v-for="sugestao in sugestaoAtletas1">
                        {{sugestao.id}} -> {{sugestao.nome}}
                      </li>
                    </div>
                    <div v-if="selA2">
                      <li v-for="sugestao in sugestaoAtletas2">
                        {{sugestao.id}} -> {{sugestao.nome}}
                      </li>
                    </div>
                  </div>
                </div>
              </v-card>
            </v-flex>
          </v-container>
        </div>
        <div class="column">
          <v-container  text-xs-center>
            <v-flex dist distright xs6 offset-xs3 style="margin:auto">
              <v-card color="white" class="my-card">
                <div class="column">
                  <form class="review-form" @submit.prevent="submitForm">
                    <div class="field">
                      <!--falta o relógio para igualar ao instante-->
                      <input v-model="tipo" class="input" type="text" placeholder="Tipo de evento" v-on:keydown.down="selectType" v-on:keyup.down="$event.target.nextElementSibling.focus()" v-on:keyup.up="$event.target.previousElementSibling.focus()" v-on:focus="selT=true, selE=false, selA1=false, selA2=false">
                      <input v-model="evento.equipa" class="input" type="text" placeholder="Equipa" v-if="tipo_evento!=null && tipo_evento.equipa" v-on:keyup.down="$event.target.nextElementSibling.focus()" v-on:keyup.up="$event.target.previousElementSibling.focus()" v-on:focus="selT=false, selE=true, selA1=false, selA2=false">
                      <input v-model="evento.atleta1" class="input" type="text" placeholder="Atleta" v-if="tipo_evento!=null && tipo_evento.atleta1" v-on:keyup.down="$event.target.nextElementSibling.focus()" v-on:keyup.up="$event.target.previousElementSibling.focus()" v-on:focus="selT=false, selE=false, selA1=true, selA2=false, getAtletas1()">
                      <input v-model="evento.atleta2" class="input" type="text" placeholder="Atleta 2" v-if="tipo_evento!=null && tipo_evento.atleta2" v-on:keyup.down="$event.target.nextElementSibling.focus()" v-on:keyup.up="$event.target.previousElementSibling.focus()" v-on:focus="selT=false, selE=false, selA1=false, selA2=true, getAtletas2()">
                      <input v-model="evento.zonaC" class="input" type="text" placeholder="Zona de campo" v-if="tipo_evento!=null && tipo_evento.zonaCampo" v-on:keyup.down="$event.target.nextElementSibling.focus()" v-on:keyup.up="$event.target.previousElementSibling.focus()" v-on:focus="selT=false, selE=false, selA1=false, selA2=false">
                      <input v-model="evento.zonaB" class="input" type="text" placeholder="Zona da baliza" v-if="tipo_evento!=null && tipo_evento.zonaBaliza" v-on:keyup.down="$event.target.nextElementSibling.focus()" v-on:keyup.up="$event.target.previousElementSibling.focus()" v-on:focus="selT=false, selE=false, selA1=false, selA2=false">
                      <input v-model="evento.novoinst" class="input" type="text" placeholder="Novo instante" v-if="tipo_evento!=null && tipo_evento.novoinstante" v-on:keyup.down="$event.target.nextElementSibling.focus()" v-on:keyup.up="$event.target.previousElementSibling.focus()" v-on:focus="selT=false, selE=false, selA1=false, selA2=false">
                      <input type="submit" value="Submit" hidden>
                    </div>
                  </form>
                </div>
              </v-card>
            </v-flex>
          </v-container>
        </div>
      </div>
      <div class="row">
        <div class="column">
          <md-table v-model="eventos_jogo" md-sort="instante" md-sort-order="asc" md-fixed-header>
            <md-table-toolbar>
              <div class="md-toolbar-section-start">
                <h1 class="md-title"> </h1>
              </div>

              <md-field md-clearable class="md-toolbar-section-end">
                <md-input placeholder="Pesquisar por adversário..." v-model="search" @input="searchOnTable" />
              </md-field>
            </md-table-toolbar>

            <md-table-empty-state
              md-label="Sem eventos"
              :md-description="'Não foram encontrados eventos para este jogo.'">
            </md-table-empty-state>

            <md-table-row slot="md-table-row" slot-scope="{ item }" style="cursor:pointer">
              <md-table-cell md-label="Instante" md-sort-by="instante" md-numeric>{{ item.instante }}</md-table-cell>
              <md-table-cell md-label="Tipo de Evento" md-sort-by="tipo">{{ item.tipo }}</md-table-cell>
              <md-table-cell md-label="Equipa" md-sort-by="equipa">{{ item.equipa }}</md-table-cell>
            </md-table-row>
          </md-table>
        </div>
      </div>
    </div>
  </layout-basic>
</template>

<script> 
import router from "../../router";
import LayoutBasic from '../layouts/Basic.vue'
import axios from 'axios';
export default {
  name: 'Movies',
  components: {
      LayoutBasic
  },
  data() {
    return {
      jogo: null,
      sugestaoTipos: null,
      sugestaoAtletas1: null,
      sugestaoAtletas2: null,

      selT: false,
      selE: false,
      selA1: false,
      selA2: false,
      // ATENÇÃO: FALTA AS IMAGENS DO CAMPO E DA BALIZA

      eventos_jogo: null,
      tipo: null,
      tipo_evento: null,

      evento: {
        jogo: this.jogo,
        equipa: null,
        tipo: null,
        atleta1: null,
        atleta2: null,
        zonaC: null,
        zonaB: null,
        instante: null,
        novoinst: null,
      },

      timer: 2400,
      parte: 1,
      minutos: 20,
      segundos: 0,
      paused: true,
      interval: null,
      change: false,
      clockChange: {
        minutos: 0,
        segundos: 0,
        parte: 1,
      }
    }
  },
  mounted: function() {
    this.checkLoggedIn();
    this.FetchData();
  },
  methods: {
    FetchData: function() {
      var app = this;
      axios.get(process.env.API_URL + "/server/get_jogo/"+this.$session.get('jogoTab')+"/").then(response => {
        app.jogo = response.data;
        app.evento.jogo = app.jogo.id;

        axios.get(process.env.API_URL + "/server/get_eventos/"+app.jogo.id+"/").then(response => {
          app.eventos = response.data;

          axios.get(process.env.API_URL + "/server/get_tipos_selecionados/" + this.$session.get('user_email') + "/").then(response => {
            app.sugestaoTipos = response.data;
          });
        });
      });
    },
      
    checkLoggedIn() {
      if (!this.$session.has('token')) {
        router.push("/auth");
      }
    },

    verJogo(id) {
      this.$session.set('jogoTab', id)
      router.push("/jogo")
    },

    selectType() {
      var app = this;
      axios.get(process.env.API_URL + "/server/get_tipo_evento/" + app.tipo + "/").then(response => {
        app.tipo_evento = response.data;
        app.evento.tipo = app.tipo_evento.id;
      })
    },

    submitForm() {
      /*
      if(this.evento.tipo != clockchange)
        this.evento.instante = this.timer;
      */
      var app = this;
      axios.post(process.env.API_URL + "/server/evento/", JSON.stringify(app.evento)).then(response => {
        router.push("/jogo")
      }).catch(e => {})
    },

    getAtletas1() {
      if(this.evento.equipa != null){
        var app = this;

        axios.get(process.env.API_URL + "/server/get_atletas_campo/" + app.evento.equipa + "/" + app.evento.jogo + "/").then(response => {
          app.sugestaoAtletas1 = response.data
        })
      }
    },

    getAtletas2() {
      if(this.evento.equipa != null){
        var app = this;

        axios.get(process.env.API_URL + "/server/get_atletas_suplentes/" + app.evento.equipa + "/" + app.evento.jogo + "/").then(response => {
          app.sugestaoAtletas2 = response.data
        })
      }
    },

    updateClock(){
      if (!this.paused) { // está prestes a parar
        clearInterval(this.interval);
        console.log(this.evento);
        /* 
        this.evento.tipo = stop;
        this.evento.instante = this.timer;
        submitForm();
         */
      } else { // está prestes a (re)começar
        console.log('timer starts');
        /* 
        this.evento.tipo = start;
        this.evento.instante = this.timer;
        submitForm();
        */
        this.interval = setInterval(() => this.incrementTime(), 1000);
      }
      this.paused = !this.paused;
    },
    
    incrementTime() {
      if(this.timer > 0)
        this.timer -= 1;
      if(this.segundos == 0){
        if(this.minutos == 0){
          this.paused = true;
          clearInterval(this.interval);
          if(this.parte == 1){
            this.parte += 1;
            this.minutos = 20;
            /*
            this.evento.tipo = 2parte;
            this.instante = this.timer;
            submitForm();
            */
          }
          else {
            /*
            this.evento.tipo = fim;
            this.instante = this.timer;
            submitForm();
            */
          }
        }
        else{
          this.minutos -= 1;
          this.segundos = 59;
        }
      }
      else
        this.segundos -= 1;
    },

    changeClock(){
      if(!this.change) { //inicio de alteração
        this.clockChange.minutos = this.minutos;
        this.clockChange.segundos = this.segundos;
        this.clockChange.parte = this.parte;
      }
      else { //fim de alteração
          this.evento.instante = this.timer;
          this.timer = this.clockChange.minutos * 60 + this.clockChange.segundos;
          if(this.clockChange.parte == 1) this.timer += 1200;

          this.evento.novoinst = this.timer;
          this.minutos = this.clockChange.minutos;
          this.segundos = this.clockChange.segundos;
          this.parte = parseInt(this.clockChange.parte);

          /*
          this.evento.tipo = changeclock;
          submitForm();
          */
      }
      this.change = !this.change;
    }
  }
}
</script>



<style src="../../../dist/static/css/jogo.css">




