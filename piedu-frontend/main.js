import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import Vuetify from 'vuetify'
import BootstrapVue from 'bootstrap-vue'
import VueRouter from 'vue-router'

import ASideLecturer from './components/class/share/AsideLecturer.vue'
import ASideStudent from './components/class/share/AsideStudent.vue'
import Search from './components/class/share/Search.vue'
import NewClass from './components/class/new-class'
import Footer from './components/shared/Footer.vue'
import GoTopBtn from './components/shared/GoTopBtn.vue'
import HelpPage from './components/help'
import ContactPage from './components/contact'
import LoginPage from './components/login'
import AllClass from './components/class/all-class'
import MyClass from './components/class/my-class'
import InnerClass from './components/class/inner-class'

import DContainer from './components/containers/MainContainer.vue'

import nav from './components/shared/_nav.js'
import {
    Aside as AppAside,
    AsideToggler,
    Breadcrumb,
    Footer as TheFooter,
    Header as AppHeader,
    Sidebar as AppSidebar,
    SidebarFooter,
    SidebarForm,
    SidebarHeader,
    SidebarMinimizer,
    SidebarNav,
    SidebarToggler
} from './components/shared'
import DefaultAside from './components/containers/Aside.vue'
import DefaultHeaderDropdownAccnt from './components/containers/DropdownAccnt.vue'

import App from './App.vue'

import AppDrawer from './components/AppDrawer.vue'
import AppToolbar from './components/AppToolbar.vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import './static/scss/coreui.scss'


axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
Vue.use(VueAxios, axios)
Vue.use(Vuetify)
Vue.use(BootstrapVue)
Vue.use(VueRouter)

import AppEvents from './components/event.js'
// import router from './router'

new Vue({
    el: '#main-app',

    data() {
        return {
            nav: nav.items,
        }
    },
    components: {
        "asideToggler": AsideToggler,
        "appHeader": AppHeader,
        "appSidebar": AppSidebar,
        "appAside": AppAside,
        "theFooter": TheFooter,
        "breadCrumb": Breadcrumb,
        "defaultAside": DefaultAside,
        "defaultHeaderDropdownAccnt": DefaultHeaderDropdownAccnt,
        "sidebarForm": SidebarForm,
        "sidebarFooter": SidebarFooter,
        "sidebarToggler": SidebarToggler,
        "sidebarHeader": SidebarHeader,
        "sidebarNav": SidebarNav,
        "sidebarMinimizer": SidebarMinimizer,

        NewClass, ASideLecturer, ASideStudent , Search,
        'pi-footer': Footer,
        'go-top': GoTopBtn,
        'help-page': HelpPage,
        'contact-page': ContactPage,
        'login-container': LoginPage,
        'all-class': AllClass,
        'my-class': MyClass,
        'inner-class': InnerClass,
        'dcontainer': DContainer,
        'app': App,

        "app-drawer": AppDrawer,
        "app-toolbar": AppToolbar
    },
    created() {
        AppEvents.forEach(item => {
            this.$on(item.name, item.callback);
        });
        window.getApp = this;
    },
    methods: {
        openThemeSettings() {
            this.$vuetify.goTo(0);
            this.rightDrawer = (!this.rightDrawer);
        }
    },

});


//
// function formdata_to_dict(formdata) {
//     let data = [];
//     for(var pair of formdata.entries()) {
//         data.push({'name':pair[0], 'value':pair[1]});
//     }
//     return data;
// }

