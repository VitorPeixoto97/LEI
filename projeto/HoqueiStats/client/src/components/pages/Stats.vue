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

      <v-container text-xs-center>
        <v-card color="white" class="my-card chart">
          <img class="background" src="../../assets/ring.png"></img>
          <v-container style="width=100%; margin:0; padding:0;" v-if="window.width>1500">
            <apexchart height=550 type=bubble :options="bubbleOptions" :series="series" />
          </v-container>
          <v-container style="width=100%; margin:0; padding:0;" v-if="window.width>1000 && window.width<1500">
            <apexchart height=450 type=bubble :options="bubbleOptions" :series="series" />
          </v-container>
          <v-container style="width=100%; margin:0; padding:0;" v-if="window.width>700 && window.width<1000">
            <apexchart height=350 type=bubble :options="bubbleOptions" :series="series" />
          </v-container>
          <v-container style="width=100%; margin:0; padding:0;" v-if="window.width>370 && window.width<700">
            <apexchart height=175 type=bubble :options="bubbleOptions" :series="series" />
          </v-container>
          <v-container style="width=100%; margin:0; padding:0;" v-if="window.width>340 && window.width<370">
            <apexchart height=170 type=bubble :options="bubbleOptions" :series="series" />
          </v-container>
        </v-card>
      </v-container>

      <carousel-3d v-if="window.width>0 && window.width<400" :autoplay="false" :display="3" :width="300" :height="150" :border="0">
        <slide :index="0">
          <v-container text-xs-center style="margin:0px; padding:0px;">
            <v-card class="my-card">
              <div id="chart">
                <apexchart v-if="statsShow==0" type=bar height=150 :options="rematesOptions" :series="remates" />
              </div>
            </v-card>
          </v-container>
        </slide>
        <slide :index="1"><img src="https://unsplash.it/400/300?image=456"/></slide>
        <slide :index="2"><img src="https://unsplash.it/400/300?image=222"/></slide>
        <slide :index="3"><img src="https://unsplash.it/400/300?image=1003"/></slide>
        <slide :index="4"><img src="https://unsplash.it/400/300?image=940"/></slide>
        <slide :index="5"><img src="https://unsplash.it/400/300?image=944"/></slide>
        <slide :index="6"><img src="https://source.unsplash.com/mEr7U5yfYt8/400x300"/></slide>
        <slide :index="7"><img src="https://unsplash.it/400/300?image=1041"/></slide>
      </carousel-3d>

      <carousel-3d v-if="window.width>=400" :autoplay="false" :display="3" :width="500" :height="200" :border="0">
        <slide :index="0">
          <v-container text-xs-center style="margin:0px; padding:0px;">
            <v-card class="my-card">
              <div id="chart">
                <apexchart v-if="statsShow==0" type=bar height=200 :options="rematesOptions" :series="remates" />
              </div>
            </v-card>
          </v-container>
        </slide>
        <slide :index="1"><img src="https://unsplash.it/400/300?image=456"/></slide>
        <slide :index="2"><img src="https://unsplash.it/400/300?image=222"/></slide>
        <slide :index="3"><img src="https://unsplash.it/400/300?image=1003"/></slide>
        <slide :index="4"><img src="https://unsplash.it/400/300?image=940"/></slide>
        <slide :index="5"><img src="https://unsplash.it/400/300?image=944"/></slide>
        <slide :index="6"><img src="https://source.unsplash.com/mEr7U5yfYt8/400x300"/></slide>
        <slide :index="7"><img src="https://unsplash.it/400/300?image=1041"/></slide>
      </carousel-3d>

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
                <md-input placeholder="Pesquisar por tipo..." v-model="search" @input="searchOnTable" />
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
                  <form class="review-form" @submit.prevent="submitChange">
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
const toLower = text => {
  return text.toString().toLowerCase()
}
const searchByName = (items, term) => {
  if (term) {
    return items.filter(item => toLower(item.tipo).includes(toLower(term)))
  }
  return items
}
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
      eventos: [],
      evento_inicial: null,
      evento: {
        jogo: null,
        id: null,
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
      statsShow: 0,
      series: null,
      remates: null,
      rematesOptions: {
        grid: {
          show: true,
          xaxis: {
            lines: {
              show: false,
            },
          },
          yaxis: {
            lines: {
              show: false,
            },
          }, 
          strokeDashArray: 0,
        },
        dataLabels:{
          formatter: function(value, { seriesIndex, dataPointIndex, w }) {
            return w.config.series[seriesIndex].data[dataPointIndex] + '   (' + value.toFixed(0) + '%)'
          },
        },
        tooltip: {
          custom: function({series, seriesIndex, dataPointIndex, w}) {
            return '<div>' +
                     '<span>' + w.config.series[seriesIndex].name + '</span>' +
                   '</div>'
          },
        },
        chart: {
          stacked: true,
          stackType: '100%',
          zoom: { enabled: false },
          parentHeightOffset: 0,
        },
        plotOptions: {
          bar: {
            horizontal: true,
          },
        },
        
        colors: null,
        title: {
          text: 'Remates',
          style: {
            fontSize:  '19px',
            color:  '#37003c',
          },
        },
        xaxis: {
          categories: ['Baliza', 'Intercetado', 'Fora'],
          axisBorder: { show: false },
          labels: { show:false },
          axisTicks: {show:false},
        },
        fill: {
          opacity: 1
        },
        legend: { show: false },
      },
      bubbleOptions: {
        grid: { show: false },
        dataLabels: { enabled: false },
        fill: { opacity: 0.9 },
        legend: { show: false },
        chart: {
          toolbar: { show: false },
          zoom: { enabled: false },
          parentHeightOffset: 0,
          sparkline: { enabled: true },
        },
        tooltip: {
          custom: function({series, seriesIndex, dataPointIndex, w}) {
            return '<div class="arrow_box">' +
                     '<span>' + w.config.series[seriesIndex].name 
                     + ' | '  + w.config.series[seriesIndex].data[dataPointIndex][5]
                     + ' | '  + w.config.series[seriesIndex].data[dataPointIndex][3] 
                     + ' de ' + w.config.series[seriesIndex].data[dataPointIndex][4] + '</span>' +
                   '</div>'
          },
          theme: false,
        },
        colors: null,
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
      },
      window: {
        width: 0,
        height: 0
      },
    }
  },

  created: function() {
    axios.get(process.env.API_URL + "/server/get_eventos/" + this.$session.get('jogoTab') + "/").then(response => {
      this.eventos = response.data;
      this.searched = response.data;
      axios.get(process.env.API_URL + "/server/get_jogo/" + this.$session.get('jogoTab') + "/").then(response => {
        this.jogo = response.data;
        this.evento.jogo = this.$session.get('jogoTab');
        this.bubbleOptions.colors = [this.jogo.clube_cor, this.jogo.adv_cor, '#FFFFFF00'];
        this.rematesOptions.colors = [this.jogo.clube_cor, this.jogo.adv_cor, '#FFFFFF00'];
        
        this.series = [{
          name: this.jogo.clube_nome,
          data: this.genBubbles(this.jogo.clube_nome)
        },
        {
          name: this.jogo.adv_nome,
          data: this.genBubbles(this.jogo.adv_nome)
        }];

        this.remates = [{
          name: this.jogo.clube_nome,
          data: this.genRemates(this.jogo.clube_nome)
        },
        {
          name: this.jogo.adv_nome,
          data: this.genRemates(this.jogo.adv_nome)
        }];

      });
    });
    
    this.checkLoggedIn();

    window.addEventListener('resize', this.handleResize)
    this.handleResize();
  },


  methods: {
    checkLoggedIn() {
      if (!this.$session.has('token')) {
        router.push("/auth");
      }
    },

    handleResize() {
      this.window.width = window.innerWidth;
      this.window.height = window.innerHeight;
    },

    verJogo(id) {
      this.$session.set('jogoTab', id)
      router.push("/jogo")
    },

    genBubbles(equipa) {
      var series = [];
      var i = 0;
      series.push([300, 300, 10]);
      while(i < this.eventos.length){
        if(this.eventos[i].equipa == equipa)
          series.push([this.eventos[i].gcx,
                       this.eventos[i].gcy,
                       this.eventos[i].size,
                       this.eventos[i].tipo,
                       this.eventos[i].atleta1,
                       this.eventos[i].instante]);
        ++i;
      }
      return series;
    },

    genRemates(equipa) {
      var series = [];
      var rBal = 0;
      var rInt = 0;
      var rFor = 0;
      var i = 0;
      while(i < this.eventos.length){
        if(this.eventos[i].equipa == equipa){
          if(this.eventos[i].tipo == 'Remate à baliza'){
            rBal = rBal + 1;
          }
          if(this.eventos[i].tipo == 'Remate intercetado'){
            rInt = rInt + 1;
          }
          if(this.eventos[i].tipo == 'Remate fora'){
            rFor = rFor + 1;
          }
        }
        ++i;
      }


      series.push(rBal);
      series.push(rInt);
      series.push(rFor);
      console.log(series);
      return series;
    },

    removeEvento(id){
      axios.get(process.env.API_URL + "/server/del_evento/" + id + "/").then(response => {
        this.updateTable();
        this.updateJogo();
        this.FetchData();
      });
    },

    searchOnTable () {
      this.searched = searchByName(this.eventos, this.search)
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
        this.jogo = response.data;
        this.$session.set('jogo', response.data);
        this.$session.set('clube', response.data.clube_nome);
        this.$session.set('adv', response.data.adv_nome);
        this.$session.set('adv_cor', response.data.adv_cor);
      });
    },

    getAtletas1() {
      if(this.codigoEquipa != null){

        if(this.codigoEquipa == 1){
          axios.get(process.env.API_URL + "/server/get_atletas_campo/" + this.jogo.formacao + "/" + this.evento_inicial.jogo + "/").then(response => {
            this.sugestaoAtletas1 = response.data
          })
        }
        else{
          axios.get(process.env.API_URL + "/server/get_atletas_campo/" + this.jogo.adversario + "/" + this.evento_inicial.jogo + "/").then(response => {
            this.sugestaoAtletas1 = response.data
          })
        }
      }
    },

    getAtletas2() {
      if(this.codigoEquipa != null){

        if(this.codigoEquipa == 1){
          axios.get(process.env.API_URL + "/server/get_atletas_suplentes/" + this.jogo.formacao + "/" + this.evento_inicial.jogo + "/").then(response => {
            this.sugestaoAtletas2 = response.data
          })
        }
        else{
          axios.get(process.env.API_URL + "/server/get_atletas_suplentes/" + this.jogo.adversario + "/" + this.evento_inicial.jogo + "/").then(response => {
            this.sugestaoAtletas2 = response.data
          })
        }
      }
    },

    chooseEquipa(){
      if(this.codigoEquipa == 1)
        this.evento.equipa = this.jogo.formacao;
      else this.evento.equipa = this.jogo.adversario;
    },

    allFieldsOk() {
      axios.get(process.env.API_URL + "/server/get_tipo_evento/" + this.evento_inicial.tipo + "/").then(response => {
        var tipo_evento = response.data;

        if ((tipo_evento.equipa && (this.evento.equipa == null)) || (tipo_evento.atleta1 && (this.evento.atleta1 == null)) || (tipo_evento.atleta2 && (this.evento.atleta2 == null)) ||
          (tipo_evento.zonaCampo && (this.evento.zonaCampo == null)) || (tipo_evento.zonaBaliza && (this.evento.zonaBaliza == null)) ||
          (tipo_evento.novoinstante && (this.evento.novoinstante == null)) || this.evento.instante == null) {
          alert('oh')
          return false;
        }
        return true;

      }).catch(e => {
        return false;
      })
    },

    submitChange(){
      //if(this.allFieldsOk()){
        axios.post(process.env.API_URL + "/server/change_evento/", JSON.stringify(this.evento)).then(response => {
          router.push("/stats");
          this.updateTable();
          this.updateJogo();
          this.bubbles();
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
      //}
    },
  } 
}
</script>

<style src="../../../dist/static/css/stats.css">
</style>
