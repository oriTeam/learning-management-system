<template>
    <section class="section section-shaped section-lg my-0">
        <div class="shape shape-style-1 bg-gradient-default">
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
        </div>
        <div class="container pt-lg-md">
            <div class="row justify-content-center">
                <div class="col-lg-6">
                    <card type="secondary" shadow
                          header-classes="bg-white"
                          body-classes="px-lg-5 py-lg-5"
                          class="border-0">
                        <template>
                            <div class="text-muted text-center mb-2">
                                <p>Đăng nhập hệ thống</p>
                            </div>
                            <div class="btn-wrapper text-center mb-4">
                                <h3 class="h4 text-success font-weight-bold">
                                    <i class="fa fa-chalkboard"></i>
                                    PIEDU
                                </h3>
                            </div>
                        </template>
                        <v-layout row fill-height justify-center align-center v-if="loading">
                            <v-progress-circular :size="50" color="primary" indeterminate/>

                        </v-layout>
                        <template v-else>
                            <form role="form" id="login-form" @submit.prevent="submit">
                                <div class="form-group input-group input-group-alternative"><!---->
                                    <div class="input-group-prepend"><span class="input-group-text"><i
                                            class="ni ni-email-83"></i></span>
                                    </div>
                                    <input aria-describedby="addon-right addon-left" placeholder="Tên tài khoản"
                                           class="form-control px-3" name="username" v-model="credentials.username"/>
                                </div>
                                <div class="form-group input-group input-group-alternative"><!---->
                                    <div class="input-group-prepend"><span class="input-group-text"><i
                                            class="ni ni-lock-circle-open"></i></span>
                                    </div>
                                    <input aria-describedby="addon-right addon-left" type="password"
                                           placeholder="Mật khẩu" class="form-control px-3" name="password"
                                           v-model="credentials.password"/>
                                </div>
                                <div class="text-center">
                                    <button type="submit" class="btn btn-primary mt-5 mb-4"
                                            @click="submit">Đăng
                                        nhập
                                    </button>
                                </div>
                            </form>
                        </template>

                    </card>
                    <div class="row mt-3">
                        <div class="col-12 text-center">
                            <a href="#" class="text-light">
                                <small>Quên mật khẩu</small>
                            </a>
                        </div>

                    </div>
                </div>
            </div>
        </div>
    </section>
</template>
<script>
    import auth from "../auth"
    export default {
        name: "login",
        data: () => ({
            credentials: {},
            valid: true,
            loading: false,
            // rules: {
            //     username: [
            //         v => !!v || "Username is required",
            //         v => (v && v.length > 3) || "A username must be more than 3 characters long",
            //         v => /^[a-z0-9_]+$/.test(v) || "A username can only contain letters and digits"
            //     ],
            //     password: [
            //         v => !!v || "Password is required",
            //         v => (v && v.length > 2) || "The password must be longer than 4 characters"
            //     ]
            // }
        }),
        beforeCreate() {
            if(this.$ls.get('user') != null) {
                this.$swal({
                    type: 'error',
                    title: 'Bạn đã đăng nhập',
                    showConfirmButton: false,
                    timer: 1500
                });
                this.$router.push('/');

            };
        },
        methods: {
            submit: function() {
                // this.loading = true;
                let credentials = {
                    username: this.credentials.username,
                    password: this.credentials.password
                };
                auth.login(this, credentials, "/");

            },
        }
    };
</script>
<style>
</style>
