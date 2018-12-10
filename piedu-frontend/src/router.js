import Vue from "vue";
import Router from "vue-router";
import AppHeader from "./layout/AppHeader";
import AppFooter from "./layout/AppFooter";
import Landing from "./views/Home.vue";
import Login from "./views/Login.vue";
import Profile from "./views/Profile.vue";
import Contact from "./views/Contact";
import Help from "./views/Help";
import Class from "./views/Class"
import AllClass from "./views/AllClass";
import MyClass from "./views/MyClass";
import InnerClass from "./views/InnerClass";
import NewClass from "./views/NewClass";

Vue.use(Router);
var router = new Router({
    linkExactActiveClass: "active",
    mode: 'history',
    routes: [
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
            path: "/profile",
            name: "profile",
            components: {
                header: AppHeader,
                default: Profile,
                footer: AppFooter
            }
        },
        {
            path: '/class',
            components: {
                header: AppHeader,
                default: Class,
                footer: AppFooter
            },
            scrollBehavior: function () {
                return {x: 0, y: 100};
            },
            children: [
                {
                    path: 'all',
                    name: 'all-class',
                    component: AllClass
                },
                {
                    path: 'my',
                    name: 'my-class',
                    component: MyClass
                },
                {
                    path: 'new',
                    name:'new class',
                    component: NewClass
                },
                {
                    path: ':id',
                    name: 'inner-class',
                    component: InnerClass
                }
            ]
        },
        // {
        //     path: "/class/all",
        //     name: 'all-class',
        //     components: {
        //         header: AppHeader,
        //         default: AllClass,
        //         footer: AppFooter
        //     }
        // },
        // {
        //     path: "/class/my",
        //     name: 'my-class',
        //     components: {
        //         header: AppHeader,
        //         default: MyClass,
        //         footer: AppFooter
        //     }
        // },
        // {
        //     path: "/class/:id",
        //     name: "inner-class",
        //     components: {
        //         header: AppHeader,
        //         default: InnerClass,
        //         footer: AppFooter
        //     }
        // },
    ],
    scrollBehavior(to, from, savedPosition) {
        if (savedPosition) {
            return {savedPosition};
        } else {
            return {x: 0, y: 0};
        }
    }
});

router.beforeEach((to, from, next) => {
  // redirect to login page if not logged in and trying to access a restricted page
  const publicPages = ['/login', '/', '/contact', '/help', '/auth'];
  const authRequired = !publicPages.includes(to.path);
  const loggedIn = localStorage.getItem('user');

  if (authRequired && !loggedIn) {
    return next('/login');
  }

  next();
});

export default router;