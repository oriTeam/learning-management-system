<template>
    <AppHeaderDropdown v-if="isAuthenticated" right no-caret>
        <template slot="header">
            <img :src="avatarPath"
                 class="img-avatar"
                 alt="avatar"/>
        </template>

        <template slot="dropdown">
            <b-dropdown-header tag="div" class="text-center"><strong>Account</strong></b-dropdown-header>
            <b-dropdown-item><i class="fa fa-bell-o"/> Updates
                <b-badge variant="info">{{ itemsCount }}</b-badge>
            </b-dropdown-item>
            <b-dropdown-item><i class="fa fa-envelope-o"/> Messages
                <b-badge variant="success">{{ itemsCount }}</b-badge>
            </b-dropdown-item>
            <b-dropdown-item><i class="fa fa-tasks"/> Tasks
                <b-badge variant="danger">{{ itemsCount }}</b-badge>
            </b-dropdown-item>
            <b-dropdown-item><i class="fa fa-comments"/> Comments
                <b-badge variant="warning">{{ itemsCount }}</b-badge>
            </b-dropdown-item>
            <b-dropdown-header
                    tag="div"
                    class="text-center">
                <strong>Settings</strong>
            </b-dropdown-header>
            <b-dropdown-item><i class="fa fa-user"/> Profile</b-dropdown-item>
            <b-dropdown-item><i class="fa fa-wrench"/> Settings</b-dropdown-item>
            <b-dropdown-item><i class="fa fa-usd"/> Payments
                <b-badge variant="secondary">{{ itemsCount }}</b-badge>
            </b-dropdown-item>
            <b-dropdown-item><i class="fa fa-file"/> Projects
                <b-badge variant="primary">{{ itemsCount }}</b-badge>
            </b-dropdown-item>
            <b-dropdown-divider/>
            <b-dropdown-item><i class="fa fa-shield"/> Lock Account</b-dropdown-item>
            <b-dropdown-item><i class="fa fa-lock"/> Logout</b-dropdown-item>
        </template>
    </AppHeaderDropdown>
    <AppHeaderDropdown v-else>
        <a class="btn btn-primary">Đăng nhập</a>
    </AppHeaderDropdown>
</template>

<script>
    import AppHeaderDropdown from '../shared/Header/HeaderDropdown.vue'

    export default {
        name: 'DefaultHeaderDropdownAccnt',
        components: {
            AppHeaderDropdown
        },
        data: function() {
            return {
                itemsCount: 42,
                avatarPath: '',
                name: '',
                id: ''
            }
        },
        created(){
          this.isAuthenticated();
        },
        methods: {
            isAuthenticated: function () {
                self = this;
                this.axios.get('/api/authenticated').then((response) => {
                    let response_data = response.data;
                    if(response_data.authenticated) {
                        self.avatarPath = response_data.avatarPath;
                        self.id = response_data.id;
                        self.name = response_data.name;
                        return true;
                    }
                    else return false;

                }).catch((response) => {
                    console.log(response);
                })
            }

        },
    }
</script>
