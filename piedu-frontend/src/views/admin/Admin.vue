<template>
    <div>
        <section class="section section-myclass-cover section-shaped my-0">
            <!-- <search></search> -->
            <div class="shape shape-style-1 shape-primary alpha-4 bg-image bg-parallax overlay">
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
            </div>
        </section>
        <section id="content">
            <div class="container">
                <div class="row">
                    <div class="col-lg-3" id="myside">
                        <a href="javascript:void(0)" class="closebtn" @click="closeSidebar">&times;</a>
                        <sidebar></sidebar>
                    </div>
                    <div class="col-lg-9 col-sm-12 p-0">
                        <fade-transition origin="center" mode="out-in" :duration="250">
                            <router-view></router-view>
                        </fade-transition>
                    </div>
                </div>
            </div>
        </section>
        <div @click="openSidebar" id="my-open-menu" class="btn btn-sm">
            <i class="fa fa-angle-double-right px-3 py-1" style="font-size: 20px"></i>
        </div>
    </div>
</template>
<script>
    import {FadeTransition} from "vue2-transitions";
    import Sidebar from "@/components/class/Aside"

    export default {
        name: 'admin',
        components: {
            'sidebar': Sidebar,
            FadeTransition,
        },
        beforeCreate() {
            if(this.$ls.get('group') != 'admin_group') {
                this.$router.push('/');
                this.$swal({
                    type: 'error',
                    title: 'Bạn không phải Quản Trị Viên',
                    showConfirmButton: false,
                    timer: 1500
                });
            }
        },
        methods: {
            openSidebar: function () {
                document.querySelector("#myside").style.width = "270px";
            },
            closeSidebar: function () {
                document.querySelector("#myside").style.width = "0";
            },
            isAdmin: function () {
                if(this.$ls.get('group') == 'admin_group') {
                    return true;
                }
                else return false;
            },

        }
    }
</script>
<style lang="scss">
    @media (max-width: 992px) {
        #myside {
            /*display: none;*/
            height: 100%; /* 100% Full-height */
            width: 0; /* 0 width - change this with JavaScript */
            position: fixed; /* Stay in place */
            z-index: 1200; /* Stay on top */
            top: 0; /* Stay at the top */
            left: 0;
            padding: 0;
            background-color: #fff; /* Black*/
            overflow-x: hidden; /* Disable horizontal scroll */
            padding-top: 60px; /* Place content 60px from the top */
            transition: 0.5s; /* 0.5 second transition effect to slide in the sidenav */
        }
    ;

    }

    @media (min-width: 992px) {
        #myside {
            .closebtn {
                display: none;
            }
        }
    ;
        #my-open-menu {
            display: none !important;
        }
    }

    .section-myclass-cover {
        height: 450px;
        background-size: cover;
        background-position: center center;
    }

    #myside {
        .closebtn {
            position: absolute;
            top: 0;
            right: 25px;
            font-size: 36px;
            margin-left: 50px;
        }
    }

    #my-open-menu {
        position: fixed;
        top: 63px;
        left: 0px;
        font-size: 15px;
        z-index: 2;
        color: #fff;
        background-color: #0a8cf0;
        border-radius: 0px;
    }
    /*.section-shaped .shape-style-1.shape-primary {*/
        /*background: linear-gradient(150deg, #7795f8 15%, #6772e5 70%, #555abf 94%);*/
    /*}*/
</style>