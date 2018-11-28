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
                            <form role="form" id="login-form">
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
                                    <base-button typ                                                                                                                                                                            e="primary" class="mt-5 mb-4" @click="submit">Đăng
                                        nhập
                                    </base-button>
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
    import BACKEND_URL from "@/backendServer";
    import router from "../router";
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
        methods: {
            submit: function() {
                this.loading = true;
                let credentials = {
                    username: this.credentials.username,
                    password: this.credentials.password
                };
                auth.login(this, credentials, "/");
            },



            submit_form: function () {
                let csrftoken = this.getCookie("csrftoken");
                let formdata = new FormData(document.querySelector('#login-form'));
                formdata.append(
                    "csrfmiddlewaretoken",
                    csrftoken
                );
                let data = this.formdata_to_dict(formdata);
                this.axios.post(BACKEND_URL + '/api/auth/', data)
                    .then(function (response) {
                        if (response.data.success == true) {
                            // window.location.href = 'http://' + response.data.redirectTo.toString();
                        } else {
                            alert("Bạn đã nhập sai tài khoản hoặc mật khẩu. Vui lòng kiểm tra lại ...");
                        }
                    })
                    .catch(function (response) {
                        console.log(response.data);
                    });
            },
            getCookie: function (name) {
                var cookieValue = null;
                if (document.cookie && document.cookie !== "") {
                    var cookies = document.cookie.split(";");
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = cookies[i].trim();
                        if (cookie.substring(0, name.length + 1) === name + "=") {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            },

            formdata_to_dict: function (formdata) {
                let data = {};
                for (var pair of formdata.entries()) {
                    data[pair[0]] = pair[1]
                }
                return data;
            }
        }
    };
</script>
<style>
</style>
