import Vue from "vue";
import axios from "axios";
import VueAxios from "vue-axios";
import App from "./App.vue";
import router from "./router";
import Vuetify from "vuetify";
import '@/assets/vuetify.custom.min.css'; // Ensure you are using css-loader
import Argon from "./plugins/argon-kit";
import VueLocalStorage from "vue-localstorage";
import vueScrollBehavior from 'vue-scroll-behavior'
import VueScroll from 'vue-scrollto';
import VueSweetalert2 from 'vue-sweetalert2';
import VueIziToast from 'vue-izitoast';


Vue.config.productionTip = false;

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
Vue.use(VueAxios, axios);
Vue.use(Vuetify);
Vue.use(Argon);
Vue.use(VueLocalStorage, {
    name: "ls",
    bind: true
});
Vue.use(vueScrollBehavior, { router: router });
Vue.use(VueScroll);
Vue.use(VueSweetalert2);
Vue.use(VueIziToast);

new Vue({
    router,
    render: h => h(App)
}).$mount("#app");
