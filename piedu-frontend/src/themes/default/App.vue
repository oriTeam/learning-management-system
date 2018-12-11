<template>
  <div id="app">
    <!--<sidebar></sidebar>-->
    <navigation></navigation>
    <div id="main-app" style="margin-top: 118px">
      <router-view/>
    </div>
    <the-footer></the-footer>
  </div>
</template>

<script>
  import Navigation from "@@/themes/default/components/shared/Navigation.vue";
  import Footer from "@@/themes/default/components/shared/Footer.vue";
  import Sidebar from "@@/themes/default/components/shared/Sidebar"
  export default {
    name: 'App',
    components: {
      "navigation": Navigation,
      "the-footer": Footer,
      "sidebar": Sidebar,
    }
  }
</script>

<style>
  /*@import "./assets/css/font-awesome.css";*/
  @import "../../assets/css/phongvu-icon.css";
  @import "../../assets/css/main.css";
  @import url('https://fonts.googleapis.com/css?family=Muli');
  #app, body, html {
    font-family: Muli, sans-serif !important;
  }

  #app {
    font-family: Roboto, sans-serif;
  }
  section {
    padding-right: 24px;
    padding-left: 24px;
  }
</style>
