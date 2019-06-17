<template>
  <layout-basic>
    <div id="app" class="row v-row">
      <v-container text-xs-center>
        <v-card color="white" class="my-card score">
          <div class="row">
            <div class="column">
              <img class="crest" :src="jogo.logoMe">
              <p primary-title class="justify-center teamname"><b>{{jogo.clube_nome}}</b></p>
            </div>
            <div class="column">
              <p primary-title class="justify-center resultado"><b>{{jogo.resultado}}</b>
              <p class="justify-center datahora"><b>{{jogo.data}}</b></p>
              <p class="justify-center datahora" style="margin-top:-15px;"><b>{{jogo.hora}}</b></p>
              <p class="justify-center datahora"><b>{{jogo.casa}}</b></p>
            </div>
            <div class="column">
              <img class="crest" :src="jogo.logoAdv">
              <p primary-title class="justify-center teamname"><b>{{jogo.adv_nome}}</b></p>
            </div>
          </div>
        </v-card>
      </v-container>
      <v-container  text-xs-center>
        <v-card color="white" class="my-card chart">
          <img class="background" src="../../assets/ring.png"></img>
          <div id="chart">
            <apexchart type=bubble width=100% :options="chartOptions" :series="series" />
          </div>
        </v-card>
      </v-container>
    </div>

    <div class="row v-row">
      <v-container text-xs-center>
        <v-card color="white" class="my-card eventos-table">
          <md-table v-model="searched" md-sort="name" md-sort-order="asc"  md-fixed-header ref="table">
            <md-table-toolbar>
              <div class="md-toolbar-section-start">
                <h1 class="md-title"> </h1>
              </div>

              <md-field md-clearable class="md-toolbar-section-end">
                <md-input placeholder="Pesquisar..." v-model="search" @input="searchOnTable" />
              </md-field>
            </md-table-toolbar>

            <md-table-empty-state
              md-label="Sem eventos"
              :md-description="'Ainda não tem eventos registados para este jogo.'">
            </md-table-empty-state>

            <md-table-row slot="md-table-row" slot-scope="{ item }" style="cursor:pointer">
              <md-table-cell md-label="Instante" md-sort-by="instante">{{ item.instante }}</md-table-cell>
              <md-table-cell md-label="Parte" md-sort-by="parte">{{ item.parte }}</md-table-cell>
              <md-table-cell md-label="Equipa" md-sort-by="equipa">{{ item.equipa }}</md-table-cell>
              <md-table-cell md-label="Tipo de Evento" md-sort-by="tipo">{{ item.tipo }}</md-table-cell>
              <md-table-cell md-label="Atleta 1" md-sort-by="atleta1">{{ item.atleta1 }}</md-table-cell>
              <md-table-cell md-label="Atleta 2" md-sort-by="atleta2">{{ item.atleta2 }}</md-table-cell>
              <md-table-cell md-label="">
                <md-button class="md-icon-button md-raised" v-if="item.sinalizado" v-on:click="sinalizaEvento(item.id)">
                  <i class="material-icons orange600">warning</i>
                </md-button>
              </md-table-cell>
              <md-table-cell md-label="">
                <md-button class="md-icon-button md-raised" v-if="item.sinalizado" v-on:click="removeEvento(item.id)">
                  <i class="material-icons">delete</i>
                </md-button>
              </md-table-cell>
            </md-table-row>
          </md-table>
        </v-card>
      </v-container>
    </div>
    <br>
    <br>
    <br>
    <br>
  </layout-basic>
</template>

<script>
  import router from "../../router";
  import LayoutBasic from '../layouts/Basic.vue'
  import axios from 'axios';
  export default {
    name: 'StatsGameLive',
    components: {
      LayoutBasic,
    },
    data: function() {
      return {
        jogo: null,
        searched: [],
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
          this.evento.jogo = this.$session.get('jogoTab');
        });
        axios.get(process.env.API_URL + "/server/get_eventos/" + this.$session.get('jogoTab') + "/").then(response => {
          this.$session.set('eventos', response.data);
          this.searched = response.data;
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
          data: this.genBubbles(this.$session.get('clube'))
        },
          {
            name: this.$session.get('adv'),
            data: this.genBubbles(this.$session.get('adv'))
          }]
      },

      removeEvento(id){
        axios.get(process.env.API_URL + "/server/del_evento/" + id + "/").then(response => {
          this.updateTable();
          this.updateJogo();
        });
      },

      sinalizaEvento(id){
        axios.get(process.env.API_URL + "/server/sinalizar_evento/" + id + "/").then(response => {
          this.updateTable();
        });
      },

      updateTable() {
        axios.get(process.env.API_URL + "/server/get_eventos/"+this.$session.get('jogoTab')+"/").then(response => {
          this.$session.set('eventos', response.data);
          this.searched = response.data;
        });
      },

      updateJogo() {
        axios.get(process.env.API_URL + "/server/get_jogo/"+this.$session.get('jogoTab')+"/").then(response => {
          app.jogo = response.data;
          this.$session.set('jogo', response.data);
          this.$session.set('clube', response.data.clube_nome);
          this.$session.set('adv', response.data.adv_nome);
          this.$session.set('clube_cor', response.data.clube_cor);
          this.$session.set('adv_cor', response.data.adv_cor);
        });
      }
    }
  }
</script>

<style src="../../../dist/static/css/stats.css">
</style>
