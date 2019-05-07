<template>
  <div id="app">

    <slot/>

    <div>
      <div class="phone-viewport">
        <md-bottom-bar md-type="shift">
          <div style="margin: 0 auto; width: 100%;">
            <md-bottom-bar-item id="bottom-bar-item-home" md-label="Jogos" md-icon="menu"></md-bottom-bar-item>
            <md-bottom-bar-item id="bottom-bar-item-pages" md-label="Jogo" md-icon="home"></md-bottom-bar-item>
            <md-bottom-bar-item id="bottom-bar-item-posts" md-label="Definições" md-icon="settings"></md-bottom-bar-item>
            <md-bottom-bar-item id="bottom-bar-item-favorites" @click="$router.push('/auth')" md-label="Logout" md-icon="power_settings_new"></md-bottom-bar-item>
          </div>
        </md-bottom-bar>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    computed : {
      isLoggedIn : function(){ return this.$store.getters.isLoggedIn}
    },
    methods: {
      logout() {
        if (this.$session.has("token")) {
          this.$store.dispatch('logout').then(() => {
            $router.push("/auth");
          })
        }
      }
    },
  }
</script>

<style lang="scss" scoped>
  .phone-viewport {
    position: fixed;
    bottom: 0;
    width: 100%;
    overflow: hidden;
    background: #FFFFFF;
  }
</style>