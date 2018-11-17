import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'

import ASideLecturer from './components/class/ASideLecturer.vue'
import ASideStudent from './components/class/ASideStudent.vue'
import Search from './components/class/Search.vue'
import NewClass from './components/class/NewClass.vue'
import Footer from './components/shared/Footer.vue'
import GoTopBtn from './components/shared/GoTopBtn.vue'
import HelpPage from './components/help/Page.vue'
import ContactPage from './components/contact/Page.vue'
import LoginContainer from './components/login/LoginContainer.vue'
import AllClass from './components/class/AllClass.vue'

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
Vue.use(VueAxios, axios)

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

