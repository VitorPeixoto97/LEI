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
        <v-card color="white" class="my-card">
          <ul>
            <li v-for="atleta in atletas" :key="atleta.id">
              <input type="checkbox" 
                v-model="convocados.atletas" 
                :id="atleta.id"
                :value="atleta"
                :disabled="convocados.atletas.length > 9 && convocados.atletas.indexOf(atleta) === -1"> 
              <input class="txt_conv" v-model.number="atleta.camisola" :disabled="convocados.atletas.indexOf(atleta) === -1">
              <label>{{ atleta.nome }}</label>
            </li>
          </ul>
          <button class="btn btn-lg btn-primary btn-block text-uppercase"  
                  v-on:click="menuConv = false; convocados.atletas.sort(function(a, b){return a.camisola - b.camisola})" 
                  :disabled="convocados.atletas.length < 10 && convocados.atletas.indexOf(atleta) === -1 && has_null">Avançar
          </button>
        </v-card>
      </v-container>

      <v-container text-xs-center v-else>
        <v-card color="white" class="my-card">
          <ul>
            <li v-for="atleta in convocados.atletas" :key="atleta.id">
              <input type="checkbox" 
                v-model="convocados.inicial"
                :id="atleta.id"
                :value="atleta"
                :disabled="convocados.inicial.length > 4 && convocados.inicial.indexOf(atleta) === -1">
              <label>{{ atleta.camisola }} - {{ atleta.nome }}</label>
            </li>
          </ul>
          <button class="btn btn-lg btn-primary btn-block text-uppercase"  
                  v-on:click="addConvocados()" 
                  :disabled="convocados.inicial.length < 5 && convocados.inicial.indexOf(atleta) === -1">Guardar
          </button>
        </v-card>
      </v-container>
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
        convocados: {
          atletas: [],
          inicial: [],
          jogo: this.$session.get('jogoTab')
        },

        menuConv: true
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
          app.atletas = response.data
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
      for(var atleta in this.atletas){
        if(atleta.camisola == ''){
          nulls = true
          break
        }
      }
      return nulls
    },

    addConvocados() {
      axios.post(process.env.API_URL + "/server/convocados/", JSON.stringify(this.convocados)).then(response => {
        router.push("/jogo");
      })
    }
  },
}
</script>

<style src="../../../dist/static/css/index.css">