<template>
  <layout-basic>
    <div id="app">
      <v-container text-xs-center>
        <v-card color="white" class="my-card score">
          <div class="row">
            <div class="column">
              <img class="crest" :src="jogo.logoMe">
              <p primary-title class="justify-center teamname"><b>{{jogo.clube_nome}}</b></p>
            </div>
            <div class="column">
              <p primary-title class="justify-center resultado"><b> </b>
              <p class="justify-center datahora"><b>{{jogo.data}}</b></p>
              <p class="justify-center datahora" style="margin-top:-15px;"><b>{{jogo.hora}}</b></p>
            </div>
            <div class="column">
              <img class="crest" :src="jogo.logoAdv">
              <p primary-title class="justify-center teamname"><b>{{jogo.adv_nome}}</b></p>
            </div>
          </div>
        </v-card>
      </v-container>

      <v-container text-xs-center v-if="menuConv">
        <h1 class="justify-center teamname">Equipa - Convocados</h1>
        <v-card color="white" class="my-card">
          <ul>
            <li v-for="atleta in atletas" :key="atleta.id">
              <md-checkbox class="md-primary"
                v-model="convocados.atletas" 
                :id="atleta.id.toString()"
                :value="atleta"
                :disabled="convocados.atletas.length > 9 && convocados.atletas.indexOf(atleta) === -1"></md-checkbox>
              <input class="txt_conv" v-model.number="atleta.camisola" type="number" min="1" :disabled="convocados.atletas.indexOf(atleta) === -1">
              <label>{{ atleta.nome }}</label>
            </li>
          </ul>
          <button class="btn btn-lg btn-primary btn-block btn-convocados text-uppercase"  
                  v-on:click="menuConv = false; menuInicial = true; convocados.atletas.sort(function(a, b){return a.camisola - b.camisola})" 
                  :disabled="convocados.atletas.length < 10 && convocados.atletas.indexOf(atleta) === -1 && has_null">Avançar
          </button>
        </v-card>
      </v-container>

      <v-container text-xs-center v-else-if="menuInicial">
        <h1 class="justify-center teamname">Equipa - 5 Inicial</h1>
        <v-card color="white" class="my-card">
          <ul>
            <li v-for="atleta in convocados.atletas" :key="atleta.id">
              <md-checkbox class="md-primary"
                v-model="convocados.inicial"
                :id="atleta.id.toString()"
                :value="atleta"
                :disabled="convocados.inicial.length > 4 && convocados.inicial.indexOf(atleta) === -1"></md-checkbox>
              <label>{{ atleta.camisola }} - {{ atleta.nome }}</label>
            </li>
          </ul>
          <button class="btn btn-lg btn-primary btn-block btn-convocados text-uppercase"  
                  v-on:click="menuInicial = false; menuConvAdv = true;" 
                  :disabled="convocados.inicial.length < 5 && convocados.inicial.indexOf(atleta) === -1">Avançar
          </button>
        </v-card>
      </v-container>

      <v-container text-xs-center v-else-if="menuConvAdv">
        <h1 class="justify-center teamname">Adversário - Convocados</h1>
        <v-card color="white" class="my-card">
          <ul>
            <li v-for="atleta in atletasAdv" :key="atleta.id">
              <md-checkbox class="md-primary"
                v-model="convocadosAdv.atletas" 
                :id="atleta.id.toString()"
                :value="atleta"
                :disabled="convocadosAdv.atletas.length > 9 && convocadosAdv.atletas.indexOf(atleta) === -1"></md-checkbox>
              <input class="txt_conv" v-model.number="atleta.camisola" type="number" min="1" :disabled="convocadosAdv.atletas.indexOf(atleta) === -1">
              <label>{{ atleta.nome }}</label>
            </li>
          </ul>
          <button class="btn btn-lg btn-primary btn-block btn-convocados text-uppercase"  
                  v-on:click="menuConvAdv = false; menuInicialAdv = true; convocadosAdv.atletas.sort(function(a, b){return a.camisola - b.camisola})" 
                  :disabled="convocadosAdv.atletas.length < 10 && convocadosAdv.atletas.indexOf(atleta) === -1 && has_null">Avançar
          </button>
        </v-card>
      </v-container>

      <v-container text-xs-center v-else>
        <h1 class="justify-center teamname">Adversário - 5 Inicial</h1>
        <v-card color="white" class="my-card">
          <ul>
            <li v-for="atleta in convocadosAdv.atletas" :key="atleta.id">
              <md-checkbox class="md-primary"
                v-model="convocadosAdv.inicial"
                :id="atleta.id.toString()"
                :value="atleta"
                :disabled="convocadosAdv.inicial.length > 4 && convocadosAdv.inicial.indexOf(atleta) === -1"></md-checkbox>
              <label>{{ atleta.camisola }} - {{ atleta.nome }}</label>
            </li>
          </ul>
          <button class="btn btn-lg btn-primary btn-block btn-convocados text-uppercase"  
                  v-on:click="addConvocados()" 
                  :disabled="convocadosAdv.inicial.length < 5 && convocadosAdv.inicial.indexOf(atleta) === -1">Guardar
          </button>
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
import LayoutBasic from '@/components/layouts/Basic.vue'
import axios from 'axios';
export default {
  name: 'Convocados',
  components: {
      LayoutBasic
  },
  data() {
      return {
        jogo: null,
        atletas: null,
        atletasAdv: null,
        convocados: {
          atletas: [],
          inicial: []
        },
        convocadosAdv: {
          atletas: [],
          inicial: []
        },

        menuConv: true,
        menuInicial: false,
        menuConvAdv: false,
        menuInicialAdv: false
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
        axios.get(process.env.API_URL + "/server/get_atletas/" + app.jogo.formacao + "/").then(response => {
          app.atletas = response.data.sort(function(a, b){return a.camisola - b.camisola})
          axios.get(process.env.API_URL + "/server/get_atletas/" + app.jogo.adversario + "/").then(response => {
            app.atletasAdv = response.data.sort(function(a, b){return a.camisola - b.camisola})
          });
        });
      });
    },
      
    checkLoggedIn() {
      if (!this.$session.has('token')) {
        router.push("/auth");
      }
    },

    has_null() {
      var nulls = false
      for(var atleta in this.convocados.atletas){
        if(atleta.camisola === null){
          nulls = true
          break
        }
      }
      return nulls
    },

    addConvocados() {
      var convocados = {
          atletas: [],
          inicial: [],
          jogo: this.$session.get('jogoTab')
      }
      convocados.atletas = this.convocados.atletas.concat(this.convocadosAdv.atletas)
      convocados.inicial = this.convocados.inicial.concat(this.convocadosAdv.inicial)
      axios.post(process.env.API_URL + "/server/convocados/", JSON.stringify(convocados)).then(response => {
        router.push("/jogo");
      })
    }
  },
}
</script>

<style src="../../../dist/static/css/index.css">