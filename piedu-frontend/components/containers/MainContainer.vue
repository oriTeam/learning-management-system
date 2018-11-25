<template>
    <div class="app">
        <AppHeader fixed>
        </AppHeader>
        <div class="app-body">
            <AppSidebar fixed>
                <SidebarHeader/>
                <SidebarForm/>
                <SidebarNav :navItems="nav"></SidebarNav>
                <SidebarFooter/>
                <SidebarMinimizer/>
            </AppSidebar>
            <main class="main">
                <!--<Breadcrumb :list="list"/>-->
                <div class="container-fluid">
                    <!--<router-view></router-view>-->
                </div>
            </main>
            <AppAside fixed>
                <!--aside-->
                <DefaultAside/>
            </AppAside>
        </div>
        <TheFooter>

        </TheFooter>
    </div>
</template>

<script>
    import nav from '../shared/_nav.js'
    import {
        Aside as AppAside,
        AsideToggler,
        Breadcrumb,
        Footer as TheFooter,
        Header as AppHeader,
        Sidebar as AppSidebar,
        SidebarFooter,
        SidebarForm,
        SidebarHeader,
        SidebarMinimizer,
        SidebarNav,
        SidebarToggler
    } from '../shared'
    import DefaultAside from './Aside.vue'
    import DefaultHeaderDropdownAccnt from './DropdownAccnt.vue'

    export default {
        name: 'DefaultContainer',
        components: {
            AsideToggler,
            AppHeader,
            AppSidebar,
            AppAside,
            TheFooter,
            Breadcrumb,
            DefaultAside,
            DefaultHeaderDropdownAccnt,
            SidebarForm,
            SidebarFooter,
            SidebarToggler,
            SidebarHeader,
            SidebarNav,
            SidebarMinimizer
        },
        data() {
            return {
                nav: nav.items
            }
        },
        computed: {
            // name () {
            //   return this.$route.name
            // },
            // list () {
            //   return this.$route.matched.filter((route) => route.name || route.meta.label )
            // }
        }
    }
</script>
