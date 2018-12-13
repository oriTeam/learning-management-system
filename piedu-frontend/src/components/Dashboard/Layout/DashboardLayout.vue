<template>
    <div class="wrapper">

        <side-bar type="sidebar" :sidebar-links="$sidebar.sidebarLinks">
            <user-menu></user-menu>
            <form class="navbar-form navbar-left navbar-search-form navbar-search-form-mobile" role="search">
                <div class="input-group">
                    <span class="input-group-addon"><i class="fa fa-search"></i></span>
                    <input type="text" value="" class="form-control" placeholder="Search...">
                </div>
            </form>
            <mobile-menu></mobile-menu>
        </side-bar>

        <div class="main-panel">
            <top-navbar></top-navbar>

            <dashboard-content @click.native="toggleSidebar">

            </dashboard-content>

            <content-footer></content-footer>
        </div>
    </div>
</template>
<style lang="scss">
    /*@import '../../../assets/scss/paper-dashboard.scss';*/
    /*@import '../../../assets/scss/element_variables.scss';*/
    /*@import '../../../assets/scss/demo.scss';*/
    /*/home/vantrong291/workspaces/python3/django/piedu/piedu-frontend/node_modules/element-ui/packages/theme-chalk/src/icon.scss*/

</style>
<script>
    import TopNavbar from './TopNavbar.vue'
    import ContentFooter from './ContentFooter.vue'
    import DashboardContent from './Content.vue'
    import UserMenu from '@/components/UIComponents/SidebarPlugin/UserMenu.vue'
    import MobileMenu from '@/components/UIComponents/SidebarPlugin/MobileMenu.vue'

    export default {
        components: {
            TopNavbar,
            ContentFooter,
            DashboardContent,
            UserMenu,
            MobileMenu
        },
        methods: {
            toggleSidebar() {
                if (this.$sidebar.showSidebar) {
                    this.$sidebar.displaySidebar(false)
                }
            }
        }
    }

</script>
