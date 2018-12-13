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
    </div>
</template>
<script>
    import {FadeTransition} from "vue2-transitions";

    export default {
        components: {
            FadeTransition
        },
        created() {
            console.log(this.$ls.get('user'));
            console.log(this.$route);
        },
        watch: {
            $route(to, from) {
                this.$ls.set("savedPosition");
                // alert('1');
            }
        }
    };
</script>
<style lang="scss">
    @import url('https://fonts.googleapis.com/css?family=Muli');
    @import url('https://fonts.googleapis.com/css?family=Cabin');
    /*@import "./assets/scss/materialize.css";*/
    /*@import "./assets/scss/style.css";*/
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
</style>
