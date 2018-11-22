<template>
    <header :class="classList">
        <!--<slot>Header</slot>-->
        <SidebarToggler class="d-lg-none" display="md" mobile/>
        <b-link class="navbar-brand" to="#">
            <img class="navbar-brand-full" src="img/brand/logo.svg" width="89" height="25" alt="CoreUI Logo">
            <img class="navbar-brand-minimized" src="img/brand/sygnet.svg" width="30" height="30" alt="CoreUI Logo">
        </b-link>
        <SidebarToggler class="d-md-down-none" display="lg"/>
        <b-navbar-nav class="d-md-down-none">
            <b-nav-item class="px-3" to="/dashboard">Dashboard</b-nav-item>
            <b-nav-item class="px-3" to="/users" exact>Users</b-nav-item>
            <b-nav-item class="px-3">Settings</b-nav-item>
        </b-navbar-nav>
        <b-navbar-nav class="ml-auto">
            <b-nav-item class="d-md-down-none">
                <i class="icon-bell"></i>
                <b-badge pill variant="danger">5</b-badge>
            </b-nav-item>
            <b-nav-item class="d-md-down-none">
                <i class="icon-list"></i>
            </b-nav-item>
            <b-nav-item class="d-md-down-none">
                <i class="icon-location-pin"></i>
            </b-nav-item>
            <DefaultHeaderDropdownAccnt/>
        </b-navbar-nav>
        <AsideToggler class="d-none d-lg-block"/>
    </header>
</template>

<script>
    import SidebarToggler from '../Sidebar/SidebarToggler.vue'
    import AsideToggler from '../Aside/AsideToggler.vue'
    import DefaultHeaderDropdownAccnt from '../../containers/DropdownAccnt.vue'
    export default {
        name: 'AppHeader',
        props: {
            fixed: {
                type: Boolean,
                default: false
            }
        },
        computed: {
            classList() {
                return [
                    'app-header',
                    'navbar'
                ]
            }
        },
        components: {
            AsideToggler,
            SidebarToggler,
            DefaultHeaderDropdownAccnt
        },
        mounted: function () {
            this.isFixed(this.fixed)
        },
        methods: {
            isFixed(fixed) {
                fixed ? document.body.classList.add('header-fixed') : document.body.classList.remove('header-fixed')
                return fixed
            }
        }
    }
</script>
