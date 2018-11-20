<template>
  <div id="help-body">
    <help-hero></help-hero>
    <help-content></help-content>
  </div>
</template>
<script>
  import Hero from './Hero.vue';
  import Content from './Content.vue'
  export default {
    components: { 
      'help-hero': Hero,
      'help-content': Content
    }
  }
</script>
