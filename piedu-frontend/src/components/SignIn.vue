<template>
  <div>
    ladfmvskdgmsd
    <button @click="logout">skjdvn</button>
    <!--<p v-for="classs in classes" :key="classes.class">{{ classs.class }}</p>-->
  </div>
</template>
<script>
  const API_URL = 'http://127.0.0.1:8000/api'
  import router from "../router"
  export default {
    name: 'ajax',
    mounted() {
    this.checkLoggedIn();
  },
  methods: {
    checkLoggedIn() {
      this.$session.start();
      console.log(this.$session);

      if (!this.$session.has("token")) {
        router.push("/auth");
        console.log(this.$session);
      }
    },
      logout: function () {
          this.axios.get(API_URL+ "/logout").then((response)=>{
              console.log(response.data);
          })
      }
  }
  }
</script>
