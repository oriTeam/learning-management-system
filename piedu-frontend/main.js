import Vue from 'vue'
import Demo from './components/Demo.vue'
import ASide from './components/ASide.vue'
import Search from './components/Search.vue'
import NewClass from './components/NewClass.vue'
import ClassBox from './components/ClassBox.vue'

new Vue({
  el: '#main-app',
  // render: h => h(App)
  components: {
    Demo, NewClass, ASide, Search, ClassBox
  }
})
