<template>
  <layout-basic>
    <div id="app">
        == JOGO PAGE ==
        {{this.$session.get('jogoTab')}}

    </div>
  </layout-basic>
</template>

<script> 
import router from "../../router";
import LayoutBasic from '../layouts/basic'
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
      axios.get(process.env.API_URL + "/server/info_user/" + this.$session.get('user_email') + "/").then(response => {
        this.$session.set('clube', response.data.nome);
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
    }

    
  }
}
</script>