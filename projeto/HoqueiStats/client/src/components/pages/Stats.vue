<template>
  <layout-basic>
    <div id="app">
      == STATS PAGE ==
      {{this.$session.get('jogoTab')}}
      <div>
        <apexchart width="500" type="bar" :options="options" :series="series"></apexchart>
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
    LayoutBasic,
  },
  data: function() {
    return {
      jogos: null,
      options: {
        chart: {
          id: 'vuechart-example'
        },
        xaxis: {
          categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]
        }
      },
      series: [{
        name: 'series-1',
        data: [30, 40, 45, 50, 49, 60, 70, 91]
      }]
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

    verJogo(id) {
      this.$session.set('jogoTab', id)
      router.push("/jogo")
    }

    
  }
}
</script>