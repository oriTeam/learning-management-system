import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios, axios)


import Demo from './components/Demo.vue'
import ASide from './components/class/ASide.vue'
import Search from './components/class/Search.vue'
import NewClass from './components/class/NewClass.vue'
import ClassBox from './components/class/ClassBox.vue'
import Footer from './components/shared/Footer.vue'
import GoTopBtn from './components/shared/GoTopBtn.vue'

import HelpPage from './components/help/Page.vue'
import ContactPage from './components/contact/Page.vue'

new Vue({
  el: '#main-app',
  delimiters: ["[[","]]"],
  // render: h => h(App)
  components: {
    Demo, NewClass, ASide, Search, ClassBox,
    'pi-footer': Footer,
    'go-top': GoTopBtn,
    'help-page': HelpPage,
    'contact-page': ContactPage,
  }
})
