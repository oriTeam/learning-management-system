import Vue from "vue";
import Router from "vue-router";
import AppHeader from "./layout/AppHeader";
import AppFooter from "./layout/AppFooter";
import Components from "./views/Components.vue";
import Landing from "./views/Landing.vue";
import Login from "./views/Login.vue";
import Register from "./views/Register.vue";
import Profile from "./views/Profile.vue";
import Contact from "./components/contact"
import Help from "./components/help"
import Auth from "@/components/Auth"
import SignIn from  "@/components/SignIn"

Vue.use(Router);
var router = new Router({
    linkExactActiveClass: "active",
    routes: [
        {
            path: "/components",
            name: "components",
            components: {
                header: AppHeader,
                default: Components,
                footer: AppFooter
            }
        },
        {
            path: "/auth",
            name: "auth",
            component: Auth
        },
        {
            path: "/signin",
            name: "signin",
            component: SignIn
        },
        {
            path: "/",
            name: "home",
            components: {
                header: AppHeader,
                default: Landing,
                footer: AppFooter
            }
        },
        {
            path: '/contact',
            name: 'contact',
            components: {
                header: AppHeader,
                default: Contact,
                footer: AppFooter
            }
        },
        {
            path: '/help',
            name: 'help',
            components: {
                header: AppHeader,
                default: Help,
                footer: AppFooter
            }
        },
        {
            path: "/login",
            name: "login",
            components: {
                header: AppHeader,
                default: Login,
                footer: AppFooter
            }
        },
        {
            path: "/register",
            name: "register",
            components: {
                header: AppHeader,
                default: Register,
                footer: AppFooter
            }
        },
        {
            path: "/profile",
            name: "profile",
            components: {
                header: AppHeader,
                default: Profile,
                footer: AppFooter
            }
        }
    ],
    scrollBehavior: to => {
        if (to.hash) {
            return {selector: to.hash};
        } else {
            return {x: 0, y: 0};
        }
    }
});

router.beforeEach((to, from, next) => {
  // redirect to login page if not logged in and trying to access a restricted page
  const publicPages = ['/login', '/', '/contact', '/help', '/auth'];
  const authRequired = !publicPages.includes(to.path);
  const loggedIn = localStorage.getItem('user_id');

  if (authRequired && !loggedIn) {
    return next('/login');
  }

  next();
});

export default router;