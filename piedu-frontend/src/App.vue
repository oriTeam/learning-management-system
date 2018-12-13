<template>
    <div id="app" data-app="true">
        <router-view name="header"></router-view>
        <main id="main">
            <div class="wrapper">
                <fade-transition origin="center" mode="out-in" :duration="250">
                    <router-view/>
                </fade-transition>
            </div>
        </main>
        <router-view name="footer"></router-view>
        <div v-if="this.showGotop">
            <button v-scroll-to="'#app'" class="btn btn-primary" data-toggle="tooltip" data-placement="left" id="gotop"
                    title="Lên trên cùng"
                    style="display: block;">
                <i class="fa fa-arrow-up"></i>
            </button>
        </div>
    </div>
</template>
<script>
    import {FadeTransition} from "vue2-transitions";

    export default {
        data() {
            return {
                showGotop: false,
            }
        },
        components: {
            FadeTransition
        },
        created() {
            console.log(this.$ls.get('user'));
            console.log(this.$route);
            window.addEventListener('scroll', this.showGoTopBtn);
            this.$toasted.show("Toasted !!", {
                theme: "bubble",
                position: "top-right",
                duration: 3000
            });

        },
        watch: {
            $route(to, from) {
                this.$ls.set("savedPosition");
                // alert('1');
            }
        },
        destroyed() {
            window.removeEventListener('scroll', this.showGoTopBtn);
        },
        methods: {
            showGoTopBtn: function () {
                let supportPageOffset = window.pageXOffset !== undefined;
                let isCSS1Compat = ((document.compatMode || "") === "CSS1Compat");
                let scrollTop = supportPageOffset ? window.pageYOffset : isCSS1Compat ?
                    document.documentElement.scrollTop : document.body.scrollTop;
                this.showGotop = (scrollTop > 70);
            }
        }
    };
</script>
<style lang="scss">
    @import url('https://fonts.googleapis.com/css?family=Muli');
    @import url('https://fonts.googleapis.com/css?family=Cabin');
    @import './assets/scss/form.css';

    #app, html {
        font-family: "Cabin", "Muli", sans-serif;
        font-size: 16px !important;
    }

    ;
    @media (min-width: 1200px) {
        .container {
            max-width: 1234px !important;
        }
    }

    @media (min-width: 992px) {
        .container {
            width: 100%;
            padding-left: 20px !important;
            padding-right: 20px !important;
        }
    }

    h4, .h4 {
        font-size: 1rem !important;
    }

    #gotop {
        float: right;
        position: fixed;
        bottom: 10px;
        right: 30px;
        display: none;
        z-index: 8;
    }

    .navbar-nav .nav-link {
        font-size: 1rem !important;
        font-family: "Muli", sans-serif !important;
        font-weight: 400;
        text-transform: uppercase !important;
        letter-spacing: 0;
        -webkit-transition: all 0.15s linear;
        transition: all 0.15s linear;
    }
</style>
