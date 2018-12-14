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
            // this.$toast.show(
            //     'What would you like to add?', "dfa",{
            //             balloon: true,
            //             position: 'topRight'
            // });
            // this.$swal({
            //     position: 'top-end',
            //     type: 'success',
            //     title: 'Your work has been saved',
            //     showConfirmButton: false,
            //     timer: 3000
            // });

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
    @import "../node_modules/izitoast/dist/css/iziToast.min.css";
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
    .section-shaped {
        .shape-style-1.shape-primary {
            background-image:url('../public/img/landing.jpg') !important;
            background-size: cover !important;
        }
    }

    .iziToast {
        opacity: 1 !important;
        font-family: "Cabin", sans-serif !important;
        background-color: #28a745 !important;
        color: #fff !important;
    }
    .swal2-container {
        font-family: "Cabin", sans-serif !important;
    }
    .swal2-title {
        font-size: 1rem !important;
    }
    .swal2-icon {
        font-size: 0.5rem;
    }
    .swal2-popup {
        width: 20em !important;
    }

    .swal2-popup {
        .swal2-styled.swal2-confirm {
            border: 0;
            border-radius: .25em;
            color: #fff;
            font-size: 0.875rem !important;
            padding: 5px 20px;
        }
        .swal2-styled.swal2-cancel {
            border: 0;
            border-radius: .25em;
            color: #fff;
            font-size: 0.875rem !important;
            padding: 5px 20px;
        }
    }
    .v-dialog {
        border-radius: 4px !important;
    }
</style>
