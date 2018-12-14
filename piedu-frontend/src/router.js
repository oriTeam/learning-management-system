import Vue from "vue";
import Router from "vue-router";
import AppHeader from "./layout/AppHeader";
import AppFooter from "./layout/AppFooter";
import Landing from "./views/Home.vue";
import Login from "./views/Login.vue";
import Profile from "./views/user/Profile.vue";
import Contact from "./views/Contact";
import Help from "./views/Help";
import Class from "./views/class/Class"
import AllClass from "./views/class/AllClass";
import MyClass from "./views/class/MyClass";
import InnerClass from "./views/class/InnerClass";
import NewClass from "./views/class/NewClass";
import Admin from "./views/admin/Admin";
import NotFound from "./views/NotFound";
import Dashboard from "./views/admin/Dashboard";
import CreateUser from "./views/admin/CreateUser";


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
                    name: 'new class',
                    component: NewClass
                },
                {
                    path: ':id',
                    name: 'inner-class',
                    component: InnerClass
                }
            ]
        },
        {
            path: '/user/:id',
            name: 'profile',
            components: {
                header: AppHeader,
                default: Profile,
                footer: AppFooter
            },
        },
        {
            path: '/admin',
            components: {
                header: AppHeader,
                default: Admin,
                footer: AppFooter
            },
            children: [
                {
                    path: 'dashboard',
                    name: 'dashboard',
                    component: Dashboard
                },
                {
                    path: 'create-user',
                    name: 'create-user',
                    component: CreateUser
                }
                // {
                //     path: 'e',
                //     name: '',
                //     component: Profile
                // }
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
        {path: '/404', component: NotFound},
        {path: '*', redirect: '/404'},
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