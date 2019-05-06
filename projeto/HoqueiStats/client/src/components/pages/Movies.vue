<template>
  <div id="app">
    Movies Page
    {{jogo.adversario}}
  </div>
</template>
<script>
import router from "../../router";
import axios from 'axios';
export default {
  name: 'Movies',
  data() {
      return {
          jogo: null,
      }
  },
  mounted: function() {
    this.checkLoggedIn();
    this.FetchData();
  },
  methods: {
    FetchData: function() {
      var app = this;
      axios.get(process.env.API_URL + "/server/get_jogo/1").then(response => {
        app.jogo = response.data;
      });
    },
      
    checkLoggedIn() {
      this.$session.start();
      if (!this.$session.has("token")) {
        router.push("/auth");
      }
    }
  }
}
</script>
<style>
</style>