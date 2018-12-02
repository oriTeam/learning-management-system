<template>
    <div id="app">
        <router-view name="header"></router-view>
        <main>
            <fade-transition origin="center" mode="out-in" :duration="250">
                <router-view/>
            </fade-transition>
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

    #app, html {
        font-family: "Cabin", "Muli", sans-serif;
        font-size: 16px !important;
    }

    ;
    @media (min-width: 1200px) {
        .container {
            max-width: 1174px !important;
        }
    }

    @media (min-width: 992px) {
        .container {
            width: 100%;
            padding-left: 20px !important;
            padding-right: 20px !important;
        }
    }
</style>
