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
      <v-card color="white" class="my-card chart">
        <img class="background" src="../../assets/ring.png"></img>
        <div id="chart">
          <apexchart type=bubble width=100% :options="chartOptions" :series="series" />
        </div>
      </v-card>

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
      eventos: null,
      series: null,
      chartOptions: {
        grid: { show: false },
        dataLabels: {
          enabled: false
        },
        fill: {
          opacity: 0.8
        },
        colors: [this.$session.get('clube_cor'), this.$session.get('adv_cor'), '#FFFFFF00'],
        xaxis: {
          min: 0,
          max: 200,
          labels: { show:false },
          axisBorder: { show: false },
        },
        yaxis: {
          min: 0,
          max: 100,
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
      axios.get(process.env.API_URL + "/server/get_jogo/" + this.$session.get('jogoTab') + "/").then(response => {
        app.jogo = response.data;
        this.$session.set('jogo', response.data);
        this.$session.set('clube', response.data.clube_nome);
        this.$session.set('adv', response.data.adv_nome);
        this.$session.set('clube_cor', response.data.clube_cor);
        this.$session.set('adv_cor', response.data.adv_cor);
      })
      axios.get(process.env.API_URL + "/server/get_eventos/" + this.$session.get('jogoTab') + "/").then(response => {
        this.$session.set('eventos', response.data);
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

    genBubbles(equipa) {
      var series = [];
      var i = 0;
      while(i < this.$session.get('eventos').length){
        if(this.$session.get('eventos')[i].equipa == equipa)
          series.push([this.$session.get('eventos')[i].gcx, this.$session.get('eventos')[i].gcy, this.$session.get('eventos')[i].size]);
        ++i;
      }
      return series;
    },

    bubbles() {
      this.series= [{
        name: this.$session.get('clube'),
        data: this.genBubbles(this.$session.get('jogo').formacao)
      },
      {
        name: this.$session.get('adv'),
        data: this.genBubbles(this.$session.get('jogo').adversario)
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
  .background{
    position: absolute;
    margin-top:55px;

  }
  @media only screen and (min-width: 768px) {
    .chart{
      width:90%;
      margin:auto;
      position: relative;
    }
  }
  @media only screen and (min-width: 900px) {
    .chart{
      width:60%;
      margin:auto;
      position: relative;
    }
  }
  .resultado{
    top:-30px;
    color: #31043A;
    font-size:4em !important;
  }
</style>
