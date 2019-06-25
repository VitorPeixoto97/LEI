<template>
  <layout-basic>
    <div id="app">
      <div v-if="userTecnico()">
        <md-table v-model="searched" md-sort="name" md-sort-order="asc"  md-fixed-header>
          <md-table-toolbar>
            <div class="md-toolbar-section-start">
              <h1 class="md-title"> </h1>
            </div>

            <md-field md-clearable class="md-toolbar-section-end">
              <md-input placeholder="Pesquisar por adversário..." v-model="search" @input="searchOnTable" />
            </md-field>
          </md-table-toolbar>

          <md-table-empty-state
            md-label="Sem jogos"
            :md-description="'Não foram encontrados jogos para a sua pesquisa.'">
          </md-table-empty-state>

          <md-table-row slot="md-table-row" slot-scope="{ item }" style="cursor:pointer" @click="verJogo(item.id, item.ativo, item.convocados)">
            <md-table-cell md-label="#" md-sort-by="id" md-numeric>{{ item.numero }}</md-table-cell>
            <md-table-cell md-label="Local" md-sort-by="casa">{{ item.c }}</md-table-cell>
            <md-table-cell md-label="Adversário" md-sort-by="adv_nome">{{ item.adv_nome }}</md-table-cell>
            <md-table-cell md-label="Resultado" md-sort-by="resultado">{{ item.resultado }}</md-table-cell>
            <md-table-cell md-label="Data" md-sort-by="data">{{ item.data }}</md-table-cell>
            <md-table-cell md-label="">
              <md-button class="md-button" @click="statsgame = true" v-if="item.ativo">
                estatísticas
              </md-button>
            </md-table-cell>
            <md-table-cell md-label="">
              <md-button class="md-button" @click="statsgamelive = true" v-if="item.ativo">
                estatísticas ao vivo
              </md-button>
            </md-table-cell>
          </md-table-row>
        </md-table>
      </div>
      <div v-if="userGestor()">
        <md-table v-model="searched" md-sort="name" md-sort-order="asc"  md-fixed-header>
          <md-table-toolbar>
            <div class="md-toolbar-section-start">
              <h1 class="md-title"> </h1>
            </div>

            <md-field md-clearable class="md-toolbar-section-end">
              <md-input placeholder="Pesquisar por adversário..." v-model="search" @input="searchOnTable" />
            </md-field>
          </md-table-toolbar>

          <md-table-empty-state
            md-label="Sem jogos"
            :md-description="'Não foram encontrados jogos para a sua pesquisa.'">
          </md-table-empty-state>

          <md-table-row slot="md-table-row" slot-scope="{ item }" style="cursor:pointer" @click="verJogo(item.id, item.ativo, item.convocados)">
            <md-table-cell md-label="#" md-sort-by="id" md-numeric>{{ item.numero }}</md-table-cell>
            <md-table-cell md-label="Local" md-sort-by="casa">{{ item.c }}</md-table-cell>
            <md-table-cell md-label="Adversário" md-sort-by="adv_nome">{{ item.adv_nome }}</md-table-cell>
            <md-table-cell md-label="Resultado" md-sort-by="resultado">{{ item.resultado }}</md-table-cell>
            <md-table-cell md-label="Data" md-sort-by="data">{{ item.data }}</md-table-cell>
            <md-table-cell md-label="">
              <md-button class="md-button" @click="statsgame = true" v-if="item.ativo">
                estatísticas
              </md-button>
            </md-table-cell>
            <md-table-cell md-label="">
              <md-button class="md-button" @click="statsgamelive = true" v-if="item.ativo">
                estatísticas ao vivo
              </md-button>
            </md-table-cell>
          </md-table-row>
        </md-table>
      </div>
      <div>
        <p class="justify-right" style="margin:auto" v-if="userGestor()">
          <button class="btn btn-lg btn-primary btn-block text-uppercase btn-timer" style="margin:auto" v-on:click="criarJogo = true">Adicionar jogo</button>
        </p>
      </div>
      <v-container text-xs-center v-if="criarJogo">
        <div class="row v-row">
          <div class="column v-column">
            <v-flex dist distleft>
              <v-card color="white" class="my-card">
                <div class="column">
                  <form class="review-form" @submit.prevent="submitJogo">
                    <div class="field">
                      <input v-model="jogo.numero" class="input" type="text" placeholder="Número de jogo" v-on:keyup.down="$event.target.nextElementSibling.focus()" v-on:keyup.up="$event.target.previousElementSibling.focus()" v-on:focus="selForm = false, selClAdv = false, selFormAdv = false">
                      <input v-model="jogo.formacao" class="input" type="text" placeholder="Formação" v-on:keyup.down="$event.target.nextElementSibling.focus()" v-on:keyup.up="$event.target.previousElementSibling.focus()" v-on:focus="selForm = true, selClAdv = false, selFormAdv = false">
                      <input v-model="clubeAdv" class="input" type="text" placeholder="Clube adversário" v-on:keyup.down="$event.target.nextElementSibling.focus()" v-on:keyup.up="$event.target.previousElementSibling.focus()" v-on:focus="selForm = false, selClAdv = true, selFormAdv = false">
                      <input v-model="jogo.formacaoAdv" class="input" type="text" placeholder="Formação adversária" v-on:keyup.down="$event.target.nextElementSibling.focus()" v-on:keyup.up="$event.target.previousElementSibling.focus()" v-on:focus="selForm = false, selClAdv = false, selFormAdv = true, formacoesAdversarias()">
                      Data   <input v-model="jogo.data" class="input" type="date" v-on:focus="selForm = false, selClAdv = false, selFormAdv = false">
                      Hora   <input v-model="hora" type="number" min="0" max="23" placeholder="00">:<input v-model="minutos" type="number" min="0" max="59" placeholder="00"><br>
                      Duração (em minutos):   <input v-model="jogo.duracao" type="number" min="0" placeholder="00"><br>
                      Partes do jogo:  <input v-model="jogo.partes" type="number" min="0" placeholder="00"><br>
                      <br>
                        <div class="column">
                          <multiselect v-model="jogo.tipo" placeholder="Selecione tipo de competição" :options="typeOptions" :searchable="false" :close-on-select="true" :show-labels="false">
                          </multiselect>
                      </div>
                      <br>
                      <div class="column">
                        <multiselect v-model="local" placeholder="Selecione tipo de jogo" :options="gameOptions" :searchable="false" :close-on-select="true" :show-labels="false">
                        </multiselect>
                      </div>
                      <br>
                      <input type="submit" value="Confirmar">
                      <button @click="criarJogo = false, jogo.formacao = null, clubeAdv = null, jogo.formacaoAdv = null, jogo.tipo = null, local = null, jogo.data = null, jogo.hora = null, jogo.duracao = null, jogo.partes = null">Cancelar</button>
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
                    <div v-if="selForm">
                      <li v-for="sugestao in formacoes">
                        <b>{{sugestao.id}}</b> {{sugestao.nome}}
                      </li>
                    </div>
                    <div v-if="selClAdv">
                      <li v-for="sugestao in clubes">
                        <b>{{sugestao.id}}</b> {{sugestao.nome}}
                      </li>
                    </div>
                    <div v-if="selFormAdv">
                      <li v-for="sugestao in formacoesAdv">
                        <b>{{sugestao.id}}</b> {{sugestao.nome}}
                      </li>
                    </div>
                  </div>
                </div>
              </v-card>
            </v-flex>
          </div>
        </div>
      </v-container>
      <br>
      <br>
    </div>
  </layout-basic>
</template>


<script> 
import router from "../../router";
import LayoutBasic from '../layouts/Basic.vue'
import axios from 'axios';
import Multiselect from 'vue-multiselect'
const toLower = text => {
  return text.toString().toLowerCase()
}
const searchByName = (items, term) => {
  if (term) {
    return items.filter(item => toLower(item.adv_nome).includes(toLower(term)))
  }
  return items
}

export default {
  name: 'Jogos',
  components: {
      LayoutBasic,
      Multiselect
  },
  data() {
      return {
        jogos: null,
        search: null,
        searched: [],
        statsgame: false,
        statsgamelive: false,
        criarJogo: false,
        jogo: {
          numero: null,
          formacao: null,
          formacaoAdv: null,
          tipo: null,
          casa: null,
          data: null,
          hora: null,
          duracao: null,
          partes: null
        },
        clubeAdv: null,
        formacoesAdv: null,
        formacoes: null,
        selForm: false,
        selClAdv: false,
        selFormAdv: false,
        local: null,
        clubes: null,
        hora:null,
        minutos:null,
        gameOptions: ['Casa','Fora'],
        typeOptions: ['Amigável', 'Competição']
      }
  },
  mounted: function() {
    this.checkLoggedIn();
    this.FetchData();
  },
  methods: {
    FetchData: function() {
      var app = this;
      axios.get(process.env.API_URL + "/server/get_jogos/"+this.$session.get('user_info').clube+"/").then(response => {
        app.jogos = response.data;
        this.searched = this.jogos
      });
      axios.get(process.env.API_URL + "/server/get_formacoes/" + this.$session.get('user_info').clube + "/").then(response => {
        app.formacoes = response.data;
      });
      axios.get(process.env.API_URL + "/server/get_clubes/").then(response => {
        app.clubes = response.data;
      })
    },
      
    checkLoggedIn() {
      if (!this.$session.has('token')) {
        router.push("/auth");
      }
    },

    verJogo(id, jogo_ativo, convocados) {
      this.$session.set('jogoTab', id);
      this.$session.set('activeTab',"jogo");

      if(this.userTecnico()){
        if(this.statsgame) {
          this.verStats();
          this.statsgame = false;
        }
        else {
          if (this.statsgamelive) {
            this.verStatsLive();
            this.statsgamelive = false;
          }
          else{
            if (jogo_ativo){
              this.$session.set('js', 1);
              if (convocados)
                router.push("/convocados");
              else router.push("/jogo");
            }
            else {
              this.$session.set('js', 0);
              router.push("/stats")
            }
          }
        }
      }
      else if(this.userGestor()){
        if(this.statsgame) {
          this.verStats();
          this.statsgame = false;
        }
        else {
          if (this.statsgamelive) {
            this.verStatsLive();
            this.statsgamelive = false;
          } else if(!jogo_ativo) {
            router.push("/stats")
          }
        }
      }
    },

    verStats(){
      router.push('/statsgame')
    },

    verStatsLive(){
      router.push('/statsgamelive')
    },

    newUser () {
      window.alert('Noop')
    },

    searchOnTable () {
      this.searched = searchByName(this.jogos, this.search)
    },

    userTecnico(){
      if(this.$session.get('user_info').tipo == "tecnico")
        return true;
      else return false;
    },

    userGestor(){
      if(this.$session.get('user_info').tipo == "gestor")
        return true;
      else return false;
    },

    submitJogo(){
      if(this.jogo.numero != null &&this.jogo.formacao != null && this.jogo.formacaoAdv != null && this.jogo.tipo != null && this.local != null && this.jogo.data != null && this.hora != null && this.minutos != null && this.jogo.duracao != null && this.jogo.partes != null){
        this.jogo.hora = this.hora + ":" + this.minutos + ":00";

        if(this.local == 'Casa')
          this.jogo.casa = true;
        else if(this.local == 'Fora')
          this.jogo.casa = false;

        axios.post(process.env.API_URL + "/server/jogo/", JSON.stringify(this.jogo)).then(response => {
          router.push('/jogos');
          this.jogo.numero = null;
          this.jogo.formacao = null;
          this.clubeAdv = null;
          this.formacoesAdv = null;
          this.jogo.formacaoAdv = null;
          this.jogo.tipo = null;
          this.jogo.casa = null;
          this.jogo.data = null;
          this.hora = null;
          this.minutos = null;
          this.jogo.hora = null;
          this.local = null;
          this.duracao = null;
          this.partes = null;
          this.criarJogo = false;

          axios.get(process.env.API_URL + "/server/get_jogos/"+this.$session.get('user_info').clube+"/").then(response => {
            this.jogos = response.data;
            this.searched = this.jogos
          });
        })
      }
    },

    formacoesAdversarias(){
      axios.get(process.env.API_URL + "/server/get_formacoes/" + this.clubeAdv + "/").then(response => {
        this.formacoesAdv = response.data;
      })
    }
  }
}
</script>

<style src="../../../dist/static/css/index.css">
</style>
