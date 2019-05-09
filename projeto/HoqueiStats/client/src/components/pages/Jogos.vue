<template>
  <layout-basic>
    <div id="app">


      {{this.$session.get('user_email')}}
      {{this.$session.get('clube')}}
      


<div class="container mt-4">



            <div class="card mb-4">
                <div class="card-body">
                    <!-- Grid row -->
                    <div class="row">
                        <!-- Grid column -->
                        <div class="col-md-12">
                            <div class="input-group md-form form-sm form-2 pl-0">
                                <input class="form-control my-0 py-1 pl-3 purple-border" type="text" placeholder="Pesquisar..." aria-label="Search">
                                <span class="input-group-addon waves-effect purple lighten-2" id="basic-addon1"><a><i class="fa fa-search white-text" aria-hidden="true"></i></a></span>
                            </div>
                        </div>
                    </div>

                    <table class="table table-striped">
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
                            <tr v-for="jogo in jogos">
                                <th scope="row">{{jogo.id}}</th>
                                <td>{{jogo.casa}}</td>
                                <td>{{jogo.adv_nome}}</td>
                                <td>Resultado</td>
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
import LayoutBasic from '@/components/layouts/basic'
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
      axios.get(process.env.API_URL + "/server/get_jogos/1/").then(response => {
        app.jogos = response.data;
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

    
  }
}
</script>

<style src="../../../dist/static/css/table.css">
