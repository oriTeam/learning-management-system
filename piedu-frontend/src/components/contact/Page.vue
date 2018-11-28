<template>
  <div id="contact-body">
    <contact-hero></contact-hero>
    <contact-content></contact-content>
  </div>
</template>
<script>
  import Hero from './Hero.vue';
  import Content from './Content.vue';
  export default {
    components: {
      'contact-hero': Hero,
      'contact-content': Content
    }
  }
</script>
