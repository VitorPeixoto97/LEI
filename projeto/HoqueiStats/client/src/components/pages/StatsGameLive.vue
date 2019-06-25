<template>
  <layout-basic>
    <div v-if="menuTipo==true" class="full">
      <v-container>
        <v-card class="my-card filter-card">
          <div style="padding:10px;">
            <button v-for="tipoevento in tiposeventos" v-if="tipoevento[1]==false" class="btn btn-lg btn-filter-false text-uppercase" @click="filterEv(tipoevento)">{{tipoevento[0]}}</button>
            <button v-for="tipoevento in tiposeventos" v-if="tipoevento[1]==true"  class="btn btn-lg btn-filter-true text-uppercase"  @click="filterEv(tipoevento)">{{tipoevento[0]}}</button>

            <div></div>

            <button class="btn btn-lg btn-filter-all text-uppercase"  @click="filterEv(1)">Selecionar tudo</button>
            <button class="btn btn-lg btn-filter-all text-uppercase"  @click="filterEv(0)">Remover tudo</button>
            <button class="btn btn-lg btn-filter-all text-uppercase"  @click="menuTipo=false">Fechar</button>
          </div>
        </v-card>
      </v-container>
    </div>
    <div v-if="menuJogador==true" class="full">
      <v-container>
        <v-card class="my-card filter-card">
          <div style="padding:10px;">
            <button v-for="jogador in jogadores" v-if="jogador[1]==false" class="btn btn-lg btn-filter-false text-uppercase" @click="filterJog(jogador)">{{jogador[0]}}</button>
            <button v-for="jogador in jogadores" v-if="jogador[1]==true"  class="btn btn-lg btn-filter-true text-uppercase"  @click="filterJog(jogador)">{{jogador[0]}}</button>

            <div></div>

            <button class="btn btn-lg btn-filter-all text-uppercase"  @click="filterJog(1)">Selecionar tudo</button>
            <button class="btn btn-lg btn-filter-all text-uppercase"  @click="filterJog(0)">Remover tudo</button>
            <button class="btn btn-lg btn-filter-all text-uppercase"  @click="menuJogador=false">Fechar</button>
          </div>
        </v-card>
      </v-container>
    </div>
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
    </div>

    <div class="row v-row">
      <v-container text-xs-center>
        <button class="btn btn-lg btn-filter text-uppercase" @click="menuTipo=true">Tipo</button>
        <button class="btn btn-lg btn-filter text-uppercase" @click="switchEquipa()">{{equipaFilter}}</button>
        <button class="btn btn-lg btn-filter text-uppercase" @click="switchParte()">{{parteFilter}} Parte</button>
        <button class="btn btn-lg btn-filter text-uppercase" @click="menuJogador=true">Jogador</button>
      </v-container>
    </div>

    <div class="row v-row">
      <v-container text-xs-center>
        <v-card style="border-radius:40px;" class="my-card chart">
          <img class="background" src="../../assets/ring.png"></img>
          <v-container style="width:100%; margin:0; padding:0;" v-if="window.width>1500">
            <apexchart height=550 type=bubble :options="bubbleOptions" :series="series" />
          </v-container>
          <v-container style="width:100%; margin:0; padding:0;" v-if="window.width>1000 && window.width<1500">
            <apexchart height=450 type=bubble :options="bubbleOptions" :series="series" />
          </v-container>
          <v-container style="width:100%; margin:0; padding:0;" v-if="window.width>700 && window.width<1000">
            <apexchart height=350 type=bubble :options="bubbleOptions" :series="series" />
          </v-container>
          <v-container style="width:100%; margin:0; padding:0;" v-if="window.width>370 && window.width<700">
            <apexchart height=175 type=bubble :options="bubbleOptions" :series="series" />
          </v-container>
          <v-container style="width:100%; margin:0; padding:0;" v-if="window.width>340 && window.width<370">
            <apexchart height=170 type=bubble :options="bubbleOptions" :series="series" />
          </v-container>
        </v-card>
      </v-container>

      <carousel-3d v-if="window.width>0 && window.width<400" :autoplay="false" :display="3" :width="300" :height="150" :border="0">
        <slide :index="0">
          <v-container text-xs-center style="margin:0px; padding:0px;">
            <v-card class="my-card">
              <div id="chart">
                <apexchart type=bar height=150 :options="rematesOptions" :series="remates" />
              </div>
            </v-card>
          </v-container>
        </slide>
        <slide :index="1">
          <v-container text-xs-center style="margin:0px; padding:0px;">
            <v-card class="my-card">
              <div id="chart">
                <apexchart type=bar height=150 :options="bolasOptions" :series="bolas" />
              </div>
            </v-card>
          </v-container>
        </slide>
        <slide :index="2">
          <v-container text-xs-center style="margin:0px; padding:0px;">
            <v-card class="my-card">
              <div id="chart">
                <apexchart type=bar height=150 :options="ataquesOptions" :series="ataques" />
              </div>
            </v-card>
          </v-container>
        </slide>
        <slide :index="3">
          <v-container text-xs-center style="margin:0px; padding:0px;">
            <v-card class="my-card">
              <div id="chart">
                <apexchart type=bar height=150 :options="faltasOptions" :series="faltas" />
              </div>
            </v-card>
          </v-container>
        </slide>
        <slide :index="4">
          <v-container text-xs-center style="margin:0px; padding:0px;">
            <v-card class="my-card">
              <div id="chart">
                <apexchart type=bar height=150 :options="disciplinaOptions" :series="disciplina" />
              </div>
            </v-card>
          </v-container>
        </slide>
      </carousel-3d>

      <carousel-3d v-if="window.width>=400" :autoplay="false" :display="3" :width="500" :height="200" :border="0">
        <slide :index="0">
          <v-container text-xs-center style="margin:0px; padding:0px;">
            <v-card class="my-card">
              <div id="chart">
                <apexchart type=bar height=200 :options="rematesOptions" :series="remates" />
              </div>
            </v-card>
          </v-container>
        </slide>
        <slide :index="1">
          <v-container text-xs-center style="margin:0px; padding:0px;">
            <v-card class="my-card">
              <div id="chart">
                <apexchart type=bar height=200 :options="bolasOptions" :series="bolas" />
              </div>
            </v-card>
          </v-container>
        </slide>
        <slide :index="2">
          <v-container text-xs-center style="margin:0px; padding:0px;">
            <v-card class="my-card">
              <div id="chart">
                <apexchart type=bar height=200 :options="ataquesOptions" :series="ataques" />
              </div>
            </v-card>
          </v-container>
        </slide>
        <slide :index="3">
          <v-container text-xs-center style="margin:0px; padding:0px;">
            <v-card class="my-card">
              <div id="chart">
                <apexchart type=bar height=200 :options="faltasOptions" :series="faltas" />
              </div>
            </v-card>
          </v-container>
        </slide>
        <slide :index="4">
          <v-container text-xs-center style="margin:0px; padding:0px;">
            <v-card class="my-card">
              <div id="chart">
                <apexchart type=bar height=200 :options="disciplinaOptions" :series="disciplina" />
              </div>
            </v-card>
          </v-container>
        </slide>
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
  import LayoutBasic from '../layouts/Basic.vue';
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
    name: 'StatsGameLive',
    components: {
      LayoutBasic,
    },
    data: function() {
      return {
        jogo: null,
        searched: [],
        search: null,
        eventos: [],
        tiposeventos: [],
        jogadores: [],
        menuTipo: false,
        menuJogador: false,
        equipaFilter: 'Equipa',
        parteFilter: '',
        menuJogador: false,
        series: null,
        remates: null,
        bolas: null,
        ataques: null,
        faltas: null,
        disciplina: null,
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
        bolasOptions: {
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
            text: 'Bolas',
            style: {
              fontSize: '19px',
              color:  '#37003c',
            },
          },
          xaxis: {
            categories: ['Perdas', 'Roubos'],
            axisBorder: { show: false },
            labels: { show:false },
            axisTicks: {show:false},
          },
          fill: {
            opacity: 1
          },
          legend: { show: false },
        },
        ataquesOptions: {
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
            text: 'Ataques',
            style: {
              fontSize: '19px',
              color:  '#37003c',
            },
          },
          xaxis: {
            categories: ['Organizado', 'Rápido', 'Contra-ataque'],
            axisBorder: { show: false },
            labels: { show:false },
            axisTicks: {show:false},
          },
          fill: {
            opacity: 1
          },
          legend: { show: false },
        },
        faltasOptions: {
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
            text: 'Faltas',
            style: {
              fontSize: '19px',
              color:  '#37003c',
            },
          },
          xaxis: {
            categories: ['Falta', 'Penalti', 'Livre direto'],
            axisBorder: { show: false },
            labels: { show:false },
            axisTicks: {show:false},
          },
          fill: {
            opacity: 1
          },
          legend: { show: false },
        },
        disciplinaOptions: {
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
            text: 'Disciplina',
            style: {
              fontSize: '19px',
              color:  '#37003c',
            },
          },
          xaxis: {
            categories: ['Cartão azul', 'Cartão vermelho', 'Powerplay'],
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

    mounted: function() {
      this.checkLoggedIn();

      window.addEventListener('resize', this.handleResize);
      this.handleResize();

      setInterval(() => this.FetchData(), 5000);
    },

    methods: {
      checkLoggedIn() {
        if (!this.$session.has('token')) {
          router.push("/auth");
        }
      },

      FetchData() {
        axios.get(process.env.API_URL + "/server/get_eventos/" + this.$session.get('jogoTab') + "/").then(response => {
          this.eventos = response.data;
          this.searched = response.data;
          axios.get(process.env.API_URL + "/server/get_jogo/" + this.$session.get('jogoTab') + "/").then(response => {
            this.jogo = response.data;
            this.bubbleOptions.colors = [this.jogo.clube_cor, this.jogo.adv_cor, '#FFFFFF00'];
            this.rematesOptions.colors = [this.jogo.clube_cor, this.jogo.adv_cor, '#FFFFFF00'];
            this.bolasOptions.colors = [this.jogo.clube_cor, this.jogo.adv_cor, '#FFFFFF00'];
            this.ataquesOptions.colors = [this.jogo.clube_cor, this.jogo.adv_cor, '#FFFFFF00'];
            this.faltasOptions.colors = [this.jogo.clube_cor, this.jogo.adv_cor, '#FFFFFF00'];
            this.disciplinaOptions.colors = [this.jogo.clube_cor, this.jogo.adv_cor, '#FFFFFF00'];

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

            this.bolas = [{
              name: this.jogo.clube_nome,
              data: this.genBolas(this.jogo.clube_nome)
            },
              {
                name: this.jogo.adv_nome,
                data: this.genBolas(this.jogo.adv_nome)
              }];

            this.ataques = [{
              name: this.jogo.clube_nome,
              data: this.genAtaques(this.jogo.clube_nome)
            },
              {
                name: this.jogo.adv_nome,
                data: this.genAtaques(this.jogo.adv_nome)
              }];

            this.faltas = [{
              name: this.jogo.clube_nome,
              data: this.genFaltas(this.jogo.clube_nome)
            },
              {
                name: this.jogo.adv_nome,
                data: this.genFaltas(this.jogo.adv_nome)
              }];

            this.disciplina = [{
              name: this.jogo.clube_nome,
              data: this.genDisciplina(this.jogo.clube_nome)
            },
              {
                name: this.jogo.adv_nome,
                data: this.genDisciplina(this.jogo.adv_nome)
              }];


            var i = 0;
            while(i < this.eventos.length){
              var a = 0;
              var flag = true;
              while(a < this.tiposeventos.length){
                if(this.tiposeventos[a][0] == this.eventos[i].tipo)
                  flag = false;
                ++a;
              }
              if(flag){
                this.tiposeventos.push([this.eventos[i].tipo, true]);
              }
              ++i;
            }

            i = 0;
            while(i < this.eventos.length){
              var a = 0;
              var flag = true;
              while(a < this.jogadores.length){
                if(this.jogadores[a][0] == this.eventos[i].atleta1)
                  flag = false;
                ++a;
              }
              if(flag){
                this.jogadores.push([this.eventos[i].atleta1, true]);
              }
              ++i;
            }
          });
        })
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
        while(i < this.searched.length){
          if(this.searched[i].equipa == equipa)
            series.push([this.searched[i].gcx,
              this.searched[i].gcy,
              this.searched[i].size,
              this.searched[i].tipo,
              this.searched[i].atleta1,
              this.searched[i].instante]);
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
        while(i < this.searched.length){
          if(this.searched[i].equipa == equipa){
            if(this.searched[i].tipo == 'Remate à baliza'){
              rBal = rBal + 1;
            }
            if(this.searched[i].tipo == 'Remate intercetado'){
              rInt = rInt + 1;
            }
            if(this.searched[i].tipo == 'Remate fora'){
              rFor = rFor + 1;
            }
          }
          ++i;
        }
        series.push(rBal);
        series.push(rInt);
        series.push(rFor);
        return series;
      },
      genBolas(equipa) {
        var series = [];
        var perdas = 0;
        var roubos = 0;
        var i = 0;
        while(i < this.searched.length){
          if(this.searched[i].equipa == equipa){
            if(this.searched[i].tipo == 'Perda de bola'){
              perdas = perdas + 1;
            }
            if(this.searched[i].tipo == 'Roubo de bola'){
              roubos = roubos + 1;
            }
          }
          ++i;
        }
        series.push(perdas);
        series.push(roubos);
        return series;
      },
      genAtaques(equipa) {
        var series = [];
        var org = 0;
        var rap = 0;
        var ctr = 0;
        var i = 0;
        while(i < this.searched.length){
          if(this.searched[i].equipa == equipa){
            if(this.searched[i].tipo == 'Ataque organizado'){
              org = org + 1;
            }
            if(this.searched[i].tipo == 'Ataque rápido'){
              rap = rap + 1;
            }
            if(this.searched[i].tipo == 'Contra-ataque'){
              ctr = ctr + 1;
            }
          }
          ++i;
        }
        series.push(org);
        series.push(rap);
        series.push(ctr);
        return series;
      },
      genFaltas(equipa) {
        var series = [];
        var falta = 0;
        var penal = 0;
        var livre = 0;
        var i = 0;
        while(i < this.searched.length){
          if(this.searched[i].equipa == equipa){
            if(this.searched[i].tipo == 'Falta'){
              falta = falta + 1;
            }
            if(this.searched[i].tipo == 'Penalti'){
              penal = penal + 1;
            }
            if(this.searched[i].tipo == 'Livre Direto'){
              livre = livre + 1;
            }
          }
          ++i;
        }
        series.push(falta);
        series.push(penal);
        series.push(livre);
        return series;
      },
      genDisciplina(equipa) {
        var series = [];
        var ca = 0;
        var cv = 0;
        var pp = 0;
        var i = 0;
        while(i < this.searched.length){
          if(this.searched[i].equipa == equipa){
            if(this.searched[i].tipo == 'Cartão azul'){
              ca = ca + 1;
            }
            if(this.searched[i].tipo == 'Cartão vermelho'){
              cv = cv + 1;
            }
            if(this.searched[i].tipo == 'Powerplay'){
              pp = pp + 1;
            }
          }
          ++i;
        }
        series.push(ca);
        series.push(cv);
        series.push(pp);
        return series;
      },

      switchEquipa(){
        if(this.equipaFilter=='Equipa'){
          this.equipaFilter=this.jogo.clube_nome;
          this.filtEventos();
          this.$forceUpdate();
        }
        else if(this.equipaFilter==this.jogo.clube_nome){
          this.equipaFilter=this.jogo.adv_nome;
          this.filtEventos();
          this.$forceUpdate();
        }
        else if(this.equipaFilter==this.jogo.adv_nome){
          this.equipaFilter='Equipa';
          this.filtEventos();
          this.$forceUpdate();
        }
      },
      switchParte(){
        if(this.parteFilter==''){
          this.parteFilter=1;
          this.filtEventos();
          this.$forceUpdate();
        }
        else if(this.parteFilter==1){
          this.parteFilter=2;
          this.filtEventos();
          this.$forceUpdate();
        }
        else if(this.parteFilter==2){
          this.parteFilter='';
          this.filtEventos();
          this.$forceUpdate();
        }
      },

      filterEv(evento){
        var i = 0;
        var a = 0;
        var b = 0;

        if(evento==1){
          while(b < this.tiposeventos.length){
            this.tiposeventos[b][1]=true;
            b=b+1;
          }
          this.filtEventos();
          this.$forceUpdate();
        }

        b = 0;
        if(evento==0){
          while(b < this.tiposeventos.length){
            this.tiposeventos[b][1]=false;
            b=b+1;
          }
          this.filtEventos();
          this.$forceUpdate();
        }

        while(a < this.tiposeventos.length){
          if(this.tiposeventos[a][0] == evento[0]){
            if(this.tiposeventos[a][1]==true){
              this.tiposeventos[a][1]=false;
              this.filtEventos();
              this.$forceUpdate();
            }
            else if(this.tiposeventos[a][1]==false){
              this.tiposeventos[a][1]=true;
              this.filtEventos();
              this.$forceUpdate();
            }
          }
          ++a;
        }
      },

      filterJog(jogador){
        var i = 0;
        var a = 0;
        var b = 0;

        if(jogador==1){
          while(b < this.jogadores.length){
            this.jogadores[b][1]=true;
            b=b+1;
          }
          this.filtEventos();
          this.$forceUpdate();
        }

        b = 0;
        if(jogador==0){
          while(b < this.jogadores.length){
            this.jogadores[b][1]=false;
            b=b+1;
          }
          this.filtEventos();
          this.$forceUpdate();
        }

        while(a < this.jogadores.length){
          if(this.jogadores[a][0] == jogador[0]){
            if(this.jogadores[a][1]==true){
              this.jogadores[a][1]=false;
              this.filtEventos();
              this.$forceUpdate();
            }
            else if(this.jogadores[a][1]==false){
              this.jogadores[a][1]=true;
              this.filtEventos();
              this.$forceUpdate();
            }
          }
          ++a;
        }
      },

      filtEventos(){
        var a = 0;
        var i = 0;
        var seriesEv = [];
        var seriesJog = [];
        while(a < this.tiposeventos.length){
          if(this.tiposeventos[a][1]==true){
            seriesEv.push(this.tiposeventos[a][0]);
          }
          a=a+1;
        }
        a=0;
        while(a < this.jogadores.length){
          if(this.jogadores[a][1]==true){
            seriesJog.push(this.jogadores[a][0]);
          }
          a=a+1;
        }
        a=0;
        this.searched=[];
        while(a < this.eventos.length){
          if(seriesEv.includes(this.eventos[a].tipo)){
            if(seriesJog.includes(this.eventos[a].atleta1)){
              if(this.eventos[a].equipa==this.equipaFilter || this.equipaFilter=="Equipa"){
                if(this.eventos[a].parte==this.parteFilter || this.parteFilter==''){
                  this.searched[i] = this.eventos[a];
                  i=i+1;
                }
              }
            }
          }
          a=a+1;
        }
        this.updateStats();
      },

      updateStats(){
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

        this.bolas = [{
          name: this.jogo.clube_nome,
          data: this.genBolas(this.jogo.clube_nome)
        },
          {
            name: this.jogo.adv_nome,
            data: this.genBolas(this.jogo.adv_nome)
          }];

        this.ataques = [{
          name: this.jogo.clube_nome,
          data: this.genAtaques(this.jogo.clube_nome)
        },
          {
            name: this.jogo.adv_nome,
            data: this.genAtaques(this.jogo.adv_nome)
          }];

        this.faltas = [{
          name: this.jogo.clube_nome,
          data: this.genFaltas(this.jogo.clube_nome)
        },
          {
            name: this.jogo.adv_nome,
            data: this.genFaltas(this.jogo.adv_nome)
          }];

        this.disciplina = [{
          name: this.jogo.clube_nome,
          data: this.genDisciplina(this.jogo.clube_nome)
        },
          {
            name: this.jogo.adv_nome,
            data: this.genDisciplina(this.jogo.adv_nome)
          }];
      },

      searchOnTable () {
        this.searched = searchByName(this.eventos, this.search)
      }
    },
    directives: {
      'click-outside': {
        bind: function(el, binding, vNode) {
          // Provided expression must evaluate to a function.
          if (typeof binding.value !== 'function') {
            const compName = vNode.context.name
            let warn = `[Vue-click-outside:] provided expression '${binding.expression}' is not a function, but has to be`
            if (compName) { warn += `Found in component '${compName}'` }

            console.warn(warn)
          }
          // Define Handler and cache it on the element
          const bubble = binding.modifiers.bubble
          const handler = (e) => {
            if (bubble || (!el.contains(e.target) && el !== e.target)) {
              binding.value(e)
            }
          }
          el.__vueClickOutside__ = handler

          // add Event Listeners
          document.addEventListener('click', handler)
        },

        unbind: function(el, binding) {
          // Remove Event Listeners
          document.removeEventListener('click', el.__vueClickOutside__)
          el.__vueClickOutside__ = null

        }
      }
    },
  }
</script>

<style src="../../../dist/static/css/stats.css">
</style>
