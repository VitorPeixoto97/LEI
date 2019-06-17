<template>
  <layout-basic>
    <div id="app">
      <div>
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

          <md-table-row slot="md-table-row" slot-scope="{ item }" style="cursor:pointer" @click="verJogo(item.id, item.ativo, item.convocado)">
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
    </div>
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
    return items.filter(item => toLower(item.adv_nome).includes(toLower(term)))
  }
  return items
}

export default {
  name: 'Jogos',
  components: {
      LayoutBasic
  },
  data() {
      return {
        jogos: null,
        search: null,
        searched: [],
        statsgame: false,
        statsgamelive: false,
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
    },
      
    checkLoggedIn() {
      if (!this.$session.has('token')) {
        router.push("/auth");
      }
    },

    verJogo(id, jogo_ativo, convocados) {
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
          this.$session.set('jogoTab', id);
          this.$session.set('activeTab',"jogo");
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
    }
  }
}
</script>

<style src="../../../dist/static/css/index.css">


