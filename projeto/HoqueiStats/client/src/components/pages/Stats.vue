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
                    <p primary-title class=" justify-center resultado"><b>{{jogo.resultado}}</b></p>
                    <v-card-title primary-title class="justify-center"><h5><b>{{jogo.data}}</b></h5></v-card-title>
                  </div>
                  <div class="column">
                    <img :src="jogo.logoAdv" style="display:inline-flex; max-width:40%; min-width:60px;"></img>
                    <v-card-title primary-title class="justify-center"><h5><b>{{jogo.adv_nome}}</b></h5></v-card-title>
                  </div>
                  </div>
                  

                  <v-card-text>
                    <v-btn round class="primary" large href="#">SIGN UP</v-btn>
                  </v-card-text>
                </v-card>
              </v-flex>
          </v-container>

      <div>
        <apexchart width="500" type="bar" :options="options" :series="series"></apexchart>
      </div>
    </div>
  </layout-basic>
</template>

<script> 
import router from "../../router";
import LayoutBasic from '../layouts/Basic.vue'
import axios from 'axios';
export default {
  name: 'Stats',
  components: {
    LayoutBasic,
  },
  data: function() {
    return {
      jogo: null,
      options: {
        chart: {
          id: 'vuechart-example'
        },
        xaxis: {
          categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]
        }
      },
      series: [{
        name: 'series-1',
        data: [30, 40, 45, 50, 49, 60, 70, 91]
      }]
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
      });
      axios.get(process.env.API_URL + "/server/info_user/" + this.$session.get('user_email') + "/").then(response => {
        this.$session.set('clube', response.data.nome);
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
    }

    
  }
}
</script>

<style>
  .my-card{
    border-radius:20px; 
    -webkit-box-shadow: 1px 8px 18px -3px rgba(0,0,0,0.31);
    -moz-box-shadow: 1px 8px 18px -3px rgba(0,0,0,0.31);
    box-shadow: 1px 8px 18px -3px rgba(0,0,0,0.31);
  }
  .resultado{
    top:-30px;
    color: #31043A;
    font-size:4em !important;
  }
</style>
