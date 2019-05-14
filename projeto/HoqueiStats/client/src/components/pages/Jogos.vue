<template>
  <layout-basic>
    <div id="app">
      <div class="container mt-4">
        <div class="card mb-4">
          <div class="card-body">
            <div class="row">
              <div class="col-md-12">
                <div class="input-group md-form form-sm form-2 pl-0">
                  <input class="form-control my-0 py-1 pl-3 purple-border" type="text" placeholder="Pesquisar..." aria-label="Search">
                  <span class="input-group-addon waves-effect purple lighten-2" id="basic-addon1"><a><i class="fa fa-search white-text" aria-hidden="true"></i></a></span>
                </div>
              </div>
            </div>

            <table class="table searchable table-striped sortable">
              <thead>
                <tr>
                  <th>#</th>
                  <th>Local</th>
                  <th>Adversário</th>
                  <th>Resultado</th>
                  <th>Data</th>
                  <th>Formação</th>
                </tr>
              </thead>

              <tbody>
                <tr style="cursor: pointer" @click="verJogo(jogo.id, jogo.resultado)" v-for="jogo in jogos">
                  <th scope="row">{{jogo.id}}</th>
                  <td>{{jogo.casa}}</td>
                  <td>{{jogo.adv_nome}}</td>
                  <td>{{jogo.resultado}}</td>
                  <td>{{jogo.data}}</td>
                  <td>{{jogo.form_nome}}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
        <!-- SEPARADOR: <hr class="my-4"> -->            
      </div>
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
          jogos: null,
      }
  },
  mounted: function() {
    this.checkLoggedIn();
    this.FetchData();
  },
  methods: {
    FetchData: function() {
      var app = this;
      axios.get(process.env.API_URL + "/server/info_user/" + this.$session.get('user_email') + "/").then(response => {
        this.$session.set('clube', response.data.nome)
        this.$session.set('clubeid', response.data.id)
      });
      axios.get(process.env.API_URL + "/server/get_jogos/"+this.$session.get('clubeid')+"/").then(response => {
        app.jogos = response.data;
      });
    },
      
    checkLoggedIn() {
      if (!this.$session.has('token')) {
        router.push("/auth");
      }
    },

    verJogo(id, res) {
      this.$session.set('jogoTab', id)
      this.$session.set('activeTab',"jogo")
      if(res=="") {
        this.$session.set('js', )
        router.push("/jogo");
      }
      else router.push("/stats")
    } 
  }
}
</script>

<style src="../../../dist/static/css/table.css">
