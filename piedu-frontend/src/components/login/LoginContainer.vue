<template>
  <div class="m-login__container">
    <login-form></login-form>
    <forget-password></forget-password>
  </div>
</template>
<script>
  import LoginForm from './LoginForm.vue'
  import ForgetPassword from './ForgetPassword.vue'

  export default {
    components: {
      'login-form': LoginForm,
      'forget-password': ForgetPassword
    }
  }
</script>
<style>

</style>
