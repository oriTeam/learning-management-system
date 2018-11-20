import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import Vuetify from 'vuetify'

import ASideLecturer from './components/class/share/ASideLecturer.vue'
import ASideStudent from './components/class/share/ASideStudent.vue'
import Search from './components/class/share/Search.vue'
import NewClass from './components/class/new-class/NewClass.vue'
import Footer from './components/shared/Footer.vue'
import GoTopBtn from './components/shared/GoTopBtn.vue'
import HelpPage from './components/help/Page.vue'
import ContactPage from './components/contact/Page.vue'
import LoginContainer from './components/login/LoginContainer.vue'
import AllClass from './components/class/all-class/AllClass.vue'
import MyClass from './components/class/my-class/MyClass.vue'


axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
Vue.use(VueAxios, axios)
Vue.use(Vuetify)

new Vue({
    el: '#main-app',
    components: {
        NewClass, ASideLecturer, ASideStudent , Search,
        'pi-footer': Footer,
        'go-top': GoTopBtn,
        'help-page': HelpPage,
        'contact-page': ContactPage,
        'login-container': LoginContainer,
        'all-class': AllClass,
        'my-class': MyClass,
    },
    methods: {
    }

});


//
// function formdata_to_dict(formdata) {
//     let data = [];
//     for(var pair of formdata.entries()) {
//         data.push({'name':pair[0], 'value':pair[1]});
//     }
//     return data;
// }

