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
      <v-container text-xs-center v-if="!edit">
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
                <md-button class="md-icon-button md-raised" v-if="item.sinalizado" v-on:click="editEvento(item.id)">
                  <i class="material-icons">edit</i>
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
      <v-container text-xs-center v-else v-if="edit">
        <div class="row">
          <div class="column">
            <v-flex dist distleft>
              <v-card color="white" class="my-card">
                <div class="column">
                  <form class="review-form" @submit.prevent="submitForm">
                    <div class="field">
                      <input v-model="evento.instante" autofocus class="input" type="text" placeholder="Instante" v-if="this.evento_inicial!=null" v-on:keyup.down="$event.target.nextElementSibling.focus(), chooseEquipa()" v-on:keyup.up="$event.target.previousElementSibling.focus()" v-on:focus="selT=false, selE=false, selA1=false, selA2=false">
                      <input v-model="evento.parte" class="input" type="text" placeholder="Parte" v-if="this.evento_inicial!=null" v-on:keyup.down="$event.target.nextElementSibling.focus(), chooseEquipa()" v-on:keyup.up="$event.target.previousElementSibling.focus()" v-on:focus="selT=false, selE=false, selA1=false, selA2=false">
                      <input v-model="codigoEquipa" class="input" type="text" placeholder="Equipa" v-if="this.evento_inicial!=null && this.evento_inicial.equipa!=null" v-on:keyup.down="$event.target.nextElementSibling.focus(), chooseEquipa()" v-on:keyup.up="$event.target.previousElementSibling.focus()" v-on:focus="selT=false, selE=true, selA1=false, selA2=false">
                      <input v-model="evento.atleta1" class="input" type="text" placeholder="Atleta" v-if="this.evento_inicial!=null && this.evento_inicial.atleta1!=null" v-on:keyup.down="$event.target.nextElementSibling.focus()" v-on:keyup.up="$event.target.previousElementSibling.focus()" v-on:focus="selT=false, selE=false, selA1=true, selA2=false, selC=false, selB=false, getAtletas1()">
                      <input v-model="evento.atleta2" class="input" type="text" placeholder="Atleta 2" v-if="this.evento_inicial!=null && this.evento_inicial.atleta2!=null" v-on:keyup.down="$event.target.nextElementSibling.focus()" v-on:keyup.up="$event.target.previousElementSibling.focus()" v-on:focus="selT=false, selE=false, selA1=false, selA2=true, selC=false, selB=false, getAtletas2()">
                      <input v-model="evento.zonaCampo" class="input" type="text" placeholder="Zona de campo" v-if="this.evento_inicial!=null && this.evento_inicial.zonaCampo!=null" v-on:keyup.down="$event.target.nextElementSibling.focus()" v-on:keyup.up="$event.target.previousElementSibling.focus()" v-on:focus="selT=false, selE=false, selA1=false, selA2=false, selC=true, selB=false">
                      <input v-model="evento.zonaBaliza" class="input" type="text" placeholder="Zona da baliza" v-if="this.evento_inicial!=null && this.evento_inicial.zonaBaliza!=null" v-on:keyup.down="$event.target.nextElementSibling.focus()" v-on:keyup.up="$event.target.previousElementSibling.focus()" v-on:focus="selT=false, selE=false, selA1=false, selA2=false, selC=false, selB=true">
                      <input v-model="evento.novoinstante" class="input" type="text" placeholder="Novo instante" v-if="this.evento_inicial!=null && this.evento_inicial.novoinstante!=null" v-on:keyup.down="$event.target.nextElementSibling.focus()" v-on:keyup.up="$event.target.previousElementSibling.focus()" v-on:focus="selT=false, selE=false, selA1=false, selA2=false, selC=false, selB=false">
                      <input type="submit" value="Guardar">
                    </div>
                  </form>
                </div>
              </v-card>
            </v-flex>
          </div>
          <div class="column v-column">
            <v-flex dist distright style="margin:auto">
              <v-card color="white" class="my-card">
                <div class="row">
                  <div class="column">
                    <p primary-title class="justify-center"><b>Sugestões de input</b></p>
                    <div v-if="selT">
                      <li v-for="sugestao in sugestaoTipos">
                        <b>{{sugestao.id}}</b> {{sugestao.tipo}}
                      </li>
                    </div>
                    <div v-if="selE">
                      <li>
                        <b>1</b> minha equipa
                      </li>
                      <li>
                        <b>2</b> adversario
                      </li>
                    </div>
                    <div v-if="selA1">
                      <li v-for="sugestao in sugestaoAtletas1">
                        <b>{{sugestao.id}}</b> {{sugestao.nome}} ({{sugestao.camisola}})
                      </li>
                    </div>
                    <div v-if="selA2">
                      <li v-for="sugestao in sugestaoAtletas2">
                        <b>{{sugestao.id}}</b> {{sugestao.nome}} ({{sugestao.camisola}})
                      </li>
                    </div>
                    <div v-if="selC">
                      <img src="../../assets/grids/8x4_alt.png" v-if="jogo.grelhaCampo == '8x4'" style="width: 90%">
                    </div>
                    <div v-if="selB">
                      <img src="../../assets/grids/2x2.png" v-if="jogo.grelhaBaliza == '2x2'" style="width: 50%">
                      <img src="../../assets/grids/2x3.png" v-if="jogo.grelhaBaliza == '2x3'" style="width: 50%">
                      <img src="../../assets/grids/3x3.png" v-if="jogo.grelhaBaliza == '3x3'" style="width: 50%">
                    </div>
                  </div>
                </div>
              </v-card>
            </v-flex>
          </div>
        </div>
      </v-container>
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
      edit: false,
      searched: [],
      evento_inicial: null,
      evento: {
        jogo: this.jogo,
        equipa: null,
        atleta1: null,
        atleta2: null,
        zonaCampo: null,
        zonaBaliza: null,
        instante: null,
        novoinstante: null,
        parte: null,
      },
      codigoEquipa: null,
      sugestaoAtletas1: null,
      sugestaoAtletas2: null,
      selE: false,
      selA1: false,
      selA2: false,
      selC: false,
      selB: false,
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

    editEvento(id){
      axios.get(process.env.API_URL + "/server/get_evento/" + id + "/").then(response => {
        this.evento_inicial = response.data;
        this.evento.id = this.evento_inicial.id;
        this.evento.instante = this.evento_inicial.instante;
        this.evento.parte = this.evento_inicial.parte;
        this.evento.equipa = this.evento_inicial.equipa;
        this.evento.atleta1 = this.evento_inicial.atleta1;
        this.evento.atleta2 = this.evento_inicial.atleta2;
        this.evento.zonaCampo = this.evento_inicial.zonaCampo;
        this.evento.zonaBaliza = this.evento_inicial.zonaBaliza;
        this.evento.novoinstante = this.evento_inicial.novoinstante;

        if(this.evento_inicial.equipa != null){
          if(this.evento_inicial.equipa == this.jogo.formacao)
            this.codigoEquipa = 1;
          else this.codigoEquipa = 2;
        }

        this.edit = true;
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
    },

    getAtletas1() {
      if(this.codigoEquipa != null){
        var app = this;

        if(this.codigoEquipa == 1){
          axios.get(process.env.API_URL + "/server/get_atletas_campo/" + app.jogo.formacao + "/" + app.evento_inicial.jogo + "/").then(response => {
            app.sugestaoAtletas1 = response.data
          })
        }
        else{
          axios.get(process.env.API_URL + "/server/get_atletas_campo/" + app.jogo.adversario + "/" + app.evento_inicial.jogo + "/").then(response => {
            app.sugestaoAtletas1 = response.data
          })
        }
      }
    },

    getAtletas2() {
      if(this.codigoEquipa != null){
        var app = this;

        if(this.codigoEquipa == 1){
          axios.get(process.env.API_URL + "/server/get_atletas_suplentes/" + app.jogo.formacao + "/" + app.evento_inicial.jogo + "/").then(response => {
            app.sugestaoAtletas2 = response.data
          })
        }
        else{
          axios.get(process.env.API_URL + "/server/get_atletas_suplentes/" + app.jogo.adversario + "/" + app.evento_inicial.jogo + "/").then(response => {
            app.sugestaoAtletas2 = response.data
          })
        }
      }
    },

    allFieldsOk() {
      if (this.evento_inicial == null || ((this.evento_inicial.equipa != null) && (this.evento.equipa == null)) || ((this.evento_inicial.atleta1 != null) && (this.evento.atleta1 == null)) ||
        ((this.evento_inicial.atleta2 != null) && (this.evento.atleta2 == null)) || ((this.evento_inicial.zonaCampo != null) && (this.evento.zonaC == null)) ||
        ((this.evento_inicial.zonaBaliza != null) && (this.evento.zonaB == null)) || ((this.evento_inicial.novoinstante != null) && (this.evento.novoinst == null))) {
        return false;
      }

      return true;
    },
    chooseEquipa(){
      if(this.codigoEquipa == 1)
        this.evento.equipa = this.jogo.formacao;
      else this.evento.equipa = this.jogo.adversario;

    },

    submitForm(){
      //if(this.allFieldsOk()){
        var app = this;
        axios.post(process.env.API_URL + "/server/change_evento/", JSON.stringify(app.evento)).then(response => {
          router.push("/stats");
          this.updateTable();
          this.updateJogo();
          this.tipo=null;
          this.evento_inicial = null;
          this.evento.id = null;
          this.evento.instante = null;
          this.evento.parte = null;
          this.evento.equipa = null;
          this.evento.atleta1 = null;
          this.evento.atleta2 = null;
          this.evento.zonaCampo = null;
          this.evento.zonaBaliza = null;
          this.evento.novoinstante = null;
          this.edit = false;
        }).catch(e => {});

        console.log("refresh");
      //}
    }
  } 
}
</script>

<style src="../../../dist/static/css/stats.css">
</style>
