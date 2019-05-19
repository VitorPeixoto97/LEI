<template>
  <layout-basic>
    <div id="app">
      <v-container  text-xs-center>
        <v-flex xs6 offset-xs3  style="min-width:500px; margin:auto;">
          <v-card color="white" class="my-card">
            <div class="row">
              <div class="column">
                <img :src="jogo.logoMe" style="display:inline-flex; max-width:40%; min-width:60px;"></img>
                <v-card-title primary-title class="justify-center"><h5><b>{{jogo.clube_nome}}</b></h5></v-card-title>
              </div>
              <div class="column">
                <p primary-title class=" justify-center resultado"><b>{{jogo.resultado}}</b>
                <p class="justify-center"><h5><b>{{jogo.data}}</b></h5>
                <p class="justify-center" style="margin-top:-15px;"><h5><b>{{jogo.hora}}</b></h5>
              </div>
              <div class="column">
                <img :src="jogo.logoAdv" style="display:inline-flex; max-width:40%; min-width:60px;"></img>
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
                <form method="post"">
                  <div class="field">
                    falta o relógio
                    <input v-model="tipo" class="input" type="text" placeholder="Tipo de evento" v-on:keydown.down="selectType" v-on:keyup.down="$event.target.nextElementSibling.focus()">
                    <input v-model="evento.equipa" class="input" type="text" placeholder="Equipa" v-if="tipo_evento!=null" v-on:keyup.down="$event.target.nextElementSibling.focus()">
                    <input v-model="evento.atleta1" class="input" type="text" placeholder="Atleta" v-if="tipo_evento!=null && tipo_evento.atleta1" v-on:keyup.down="$event.target.nextElementSibling.focus()">
                    <input v-model="evento.atleta2" class="input" type="text" placeholder="Atleta 2" v-if="tipo_evento!=null && tipo_evento.atleta2" v-on:keyup.down="$event.target.nextElementSibling.focus()">
                    <input v-model="evento.zonaCampo" class="input" type="text" placeholder="Zona de campo" v-if="tipo_evento!=null && tipo_evento.zonaCampo" v-on:keyup.down="$event.target.nextElementSibling.focus()">
                    <input v-model="evento.zonaBaliza" class="input" type="text" placeholder="Zona da baliza" v-if="tipo_evento!=null && tipo_evento.zonaBaliza" v-on:keyup.down="$event.target.nextElementSibling.focus()">
                    <input v-model="evento.zonaBaliza" class="input" type="text" placeholder="Novo instante" v-if="tipo_evento!=null && tipo_evento.novoInstante" v-on:keyup.down="$event.target.nextElementSibling.focus()">
                    {{tipo_evento}}
                  </div>
                </form>
              </div>
            </div>
          </v-card>
        </v-flex>
      </v-container>
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
      tipo: null,
      tipo_evento: null,
      evento: {
        equipa: null,
        atleta1: null,
        atleta2: null,
        zonaCampo: null,
        zonaBaliza: null,
        novoInstante: null,
      },
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
      })
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
      axios.get(process.env.API_URL + "/server/get_tipo_evento/"+app.tipo+"/").then(response => {
        app.tipo_evento = response.data;
      })
    },

    submitForm: function (data) {
      axios.post(process.env.API_URL + "/server/evento/", data)
    }
  }
}
</script>

