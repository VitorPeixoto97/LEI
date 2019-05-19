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
                <p class="justify-center"><h5><b>{{jogo.data}}</b></h5></p>
                <p class="justify-center" style="margin-top:-15px;"><h5><b>{{jogo.hora}}</b></h5></p>
              </div>
              <div class="column">
                <img :src="jogo.logoAdv" style="display:inline-flex; max-width:40%; min-width:60px;"></img>
                <v-card-title primary-title class="justify-center"><h5><b>{{jogo.adv_nome}}</b></h5></v-card-title>
              </div>
            </div>
          </v-card>
        </v-flex>
      </v-container>

      <div id="chart">
        <apexchart type=bubble height=350 :options="chartOptions" :series="series" />
      </div>

    </div>
  </layout-basic>
</template>

<script> 

function generateData(baseval, count, yrange) {
      var i = 0;
      var series = [];
      while (i < count) {
        var x = Math.floor(Math.random() * (750 - 1 + 1)) + 1;;
        var y = Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min;
        var z = Math.floor(Math.random() * (75 - 15 + 1)) + 15;

        series.push([x, y, z]);
        baseval += 86400000;
        i++;
      }
      return series;
    }

function generateBubbles(eventos){
  var series = [];
  for(evento in eventos) {
    series.push([evento.gcx, evento.gcy, 100]);
  }
  console.log(eventos.length);
  return series;
}


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
      eventos: null,
      series: null,
      chartOptions: {
        dataLabels: {
          enabled: false
        },
        fill: {
          opacity: 0.8
        },
        title: {
          text: 'Simple Bubble Chart'
        },
        xaxis: {
          tickAmount: 12,
          type: 'category',
        },
        yaxis: {
          max: 70
        }
      }
    }
  },

  mounted: function() {
    this.checkLoggedIn();
    this.FetchData();
    this.bubbles();
  },

  methods: {
    FetchData: function() {
      var app = this;
      axios.get(process.env.API_URL + "/server/get_jogo/"+this.$session.get('jogoTab')+"/").then(response => {
        app.jogo = response.data;
      })
      axios.get(process.env.API_URL + "/server/info_user/" + this.$session.get('user_email') + "/").then(response => {
        this.$session.set('clube', response.data.nome);
      })
      axios.get(process.env.API_URL + "/server/get_eventos/" + this.$session.get('jogoTab') + "/").then(response => {
        app.eventos = response.data;
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

    bubbles() {
      this.series= [{
        name: 'Bubble1',
          data: generateBubbles(this.eventos)
      }]
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
