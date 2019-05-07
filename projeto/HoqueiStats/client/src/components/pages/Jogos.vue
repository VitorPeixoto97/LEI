<template>
  <layout-basic>
    <div id="app">

      Movies Page
      {{jogo.tipo}}
    

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
      axios.get(process.env.API_URL + "/server/get_jogo/1/").then(response => {
        app.jogo = response.data;
      });
    },
      
    checkLoggedIn() {
      this.$session.start();
      if (!this.$session.has("token")) {
        router.push("/auth");
      }
    },
  }
}
</script>

