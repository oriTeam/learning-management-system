<template>
    <header class="header-global">
        <base-nav class="navbar-main" transparent type="" effect="light" expand>
        <!--<nav class="navbar navbar-main navbar-expand-lg navbar-light navbar-transparent">-->
            <!--<div class="container">-->
        <router-link slot="brand" class="navbar-brand mr-lg-5" to="/">
                <!--<img src="img/brand/white.png">-->
                <strong style="font-size: 30px">
                    <i class="fa fa-chalkboard" style="font-size: 30px"></i>
                    PIEdu</strong>
            </router-link>

            <div class="row" slot="content-header" slot-scope="{closeMenu}">
                <div class="col-6 collapse-brand">
                    <router-link to="/">
                        <strong style="font-size: 30px">
                            <i class="fa fa-chalkboard" style="font-size: 30px"></i>
                            PIEdu</strong>
                    </router-link>
                </div>
                <div class="col-6 collapse-close">
                    <close-button @click="closeMenu"></close-button>
                </div>
            </div>

            <ul class="navbar-nav navbar-nav-hover align-items-lg-center">
                <li class="nav-item">
                    <router-link class="nav-link nav-link-icon" to="/">
                        Trang chủ
                    </router-link>
                </li>
                <!--<base-dropdown class="nav-item" menu-classes="dropdown-menu-xl">-->
                <!--<a slot="title" href="#" class="nav-link" data-toggle="dropdown" role="button">-->
                <!--<i class="ni ni-ui-04 d-lg-none"></i>-->
                <!--<span class="nav-link-inner&#45;&#45;text">Components</span>-->
                <!--</a>-->
                <!--<div class="dropdown-menu-inner">-->
                <!--<a href="https://demos.creative-tim.com/vue-argon-design-system/documentation/"-->
                <!--class="media d-flex align-items-center">-->
                <!--<div class="icon icon-shape bg-gradient-primary rounded-circle text-white">-->
                <!--<i class="ni ni-spaceship"></i>-->
                <!--</div>-->
                <!--<div class="media-body ml-3">-->
                <!--<h6 class="heading text-primary mb-md-1">Getting started</h6>-->
                <!--<p class="description d-none d-md-inline-block mb-0">Get started with Bootstrap, the-->
                <!--world's most popular framework for building responsive sites.</p>-->
                <!--</div>-->
                <!--</a>-->
                <!--<a href="https://demos.creative-tim.com/vue-argon-design-system/documentation/"-->
                <!--class="media d-flex align-items-center">-->
                <!--<div class="icon icon-shape bg-gradient-warning rounded-circle text-white">-->
                <!--<i class="ni ni-ui-04"></i>-->
                <!--</div>-->
                <!--<div class="media-body ml-3">-->
                <!--<h5 class="heading text-warning mb-md-1">Components</h5>-->
                <!--<p class="description d-none d-md-inline-block mb-0">Learn how to use Argon-->
                <!--compiling Scss, change brand colors and more.</p>-->
                <!--</div>-->
                <!--</a>-->
                <!--</div>-->
                <!--</base-dropdown>-->
                <base-dropdown tag="li" class="nav-item">
                    <a slot="title" href="#" class="nav-link" data-toggle="dropdown" role="button">
                        <i class="ni ni-collection d-lg-none"></i>
                        <span class="nav-link-inner--text">Các lớp học</span>
                    </a>
                    <router-link to="/class/all" class="dropdown-item">Tất cả lớp học</router-link>
                    <router-link to="/class/my" class="dropdown-item">Lớp học của tôi</router-link>
                </base-dropdown>
                <li class="nav-item">
                    <router-link class="nav-link nav-link-icon" to="/contact">
                        Liên hệ
                    </router-link>
                </li>
                <li class="nav-item">
                    <router-link class="nav-link nav-link-icon" to="/help">
                        Trợ giúp
                    </router-link>
                </li>
            </ul>
            <ul class="navbar-nav align-items-lg-center ml-lg-auto">

                <li class="nav-item d-none d-lg-block ml-lg-4" v-if="username==null">
                    <router-link :to="{name:'login'}"
                                 class="btn btn-neutral btn-icon">
                        <span class="btn-inner--icon">
                          <i class="fa fa-sign-in-alt mr-2"></i>
                        </span>
                        <span class="nav-link-inner--text">Đăng nhập</span>
                    </router-link>
                </li>
                <base-dropdown v-else>
                    <base-button slot="title" type="secondary" class="dropdown-toggle" style="text-transform: none">
                        Xin chào, {{ username }}
                    </base-button>
                    <router-link class="dropdown-item"
                                 :to="{ name: 'profile', params: { id: this.$ls.get('user') }}">Trang
                        cá nhân
                    </router-link>
                    <a v-if="this.$ls.get('group') == 'admin_group'" class="dropdown-item" href="http://127.0.0.1:8000/admin">Quản lý PIEdu
                    </a>
                    <a class="dropdown-item" @click="this.logout" href="#">Đăng xuất</a>
                </base-dropdown>
            </ul>
            <!--</div>-->
        <!--</nav>-->
        </base-nav>
    </header>
</template>
<script>
    import BaseNav from "@/components/BaseNav";
    import BaseDropdown from "@/components/BaseDropdown";
    import CloseButton from "@/components/CloseButton";
    import auth from "@/auth"


    export default {
        data() {
            return {
                username: String,
                top: 0,

            }
        },
        components: {
            BaseNav,
            CloseButton,
            BaseDropdown
        },
        created() {
            this.setUsername();
        },
        watch: {
            $route(to, from) {
                this.setUsername();
            }
        },

        methods: {
            isAuthenticated: function () {
                return auth.isAuthenticated(this);
            },
            logout: function () {
                auth.logout(this);
                this.username = null;
            },
            setUsername: function () {
                this.username = this.$ls.get("username");
            },
        }
    };
</script>
<style>
    nav {
        transition: 0.3s;
    }
    .navbar-light .navbar-brand:hover, .navbar-light .navbar-brand:focus {
        color: #fff !important;
    }

</style>
