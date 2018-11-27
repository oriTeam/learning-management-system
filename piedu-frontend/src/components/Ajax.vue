<template>
    <div>
        <div class="m-login__logo">
            <a href="#">
                <img src="">
            </a>
        </div>
        <div class="m-login__signin">
            <div class="m-login__head">
                <h3 class="m-login__title">Đăng nhập vào hệ thống</h3>
            </div>
            <form id="login-form" class="m-login__form m-form" action="">
                <!--{% csrf_token %}-->
                <div class="alert alert-danger d-none" role="alert" id="login_errors"></div>
                <div class="form-group m-form__group">
                    <input class="form-control m-input" type="text" placeholder="Tên tài khoản" name="username"
                           autocomplete="off">
                </div>
                <div class="form-group m-form__group">
                    <input class="form-control m-input m-login__form-input--last" type="password"
                           placeholder="Mật khẩu" name="password">
                </div>
                <div class="row m-login__form-sub">
                    <div class="col m--align-left m-login__form-left">
                        <label class="m-checkbox  m-checkbox--focus">
                            <input type="checkbox" name="remember"> Ghi nhớ đăng nhập
                            <span></span>
                        </label>
                    </div>
                    <div class="col m--align-right m-login__form-right">
                        <a href="javascript:;" id="m_login_forget_password" class="m-link">Quên mật khẩu ?</a>
                    </div>
                </div>
                <div class="m-login__form-action">
                    <button @click="submit_form" type="button" id="m_login_signin_submit"
                            class="btn m-btn--custom m-btn--air m-login__btn m-login__btn--primary w-100    ">
                        Đăng nhập
                    </button>
                </div>
            </form>
        </div>
    </div>
</template>
<script>
    const API_URL = 'http://127.0.0.1:8000/api';


    function login_success_redirect(response) {
        if (response.success == true) {
            window.location.href = 'http://' + response.redirectTo.toString();
        } else {
            toastr.error("Bạn đã nhập sai tài khoản hoặc mật khẩu. Vui lòng kiểm tra lại ...");
        }
    }

    export default {
        methods: {
            submit_form: function () {
                let csrftoken = this.getCookie("csrftoken");
                let formdata = new FormData(document.querySelector('#login-form'));
                formdata.append(
                        "csrfmiddlewaretoken",
                        csrftoken
                );
                let data = this.formdata_to_dict(formdata);
                // let config = {
                //     headers: {
                //         'X-CSRFToken': csrftoken,
                //     }
                // }
                // console.log(config);
                this.axios.post(API_URL + '/auth', data)
                        .then(function (response) {
                            if (response.data.success == true) {
                                window.location.href = 'http://' + response.data.redirectTo.toString();
                            } else {
                                toastr.error("Bạn đã nhập sai tài khoản hoặc mật khẩu. Vui lòng kiểm tra lại ...");
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
    }
</script>
<style>
    #m_login_signin_submit {
        background: linear-gradient(to right, #a4d6e7 0%, #1ba6de 100%);
        color: #fff;
        font-size: 16px;
        border-radius: 4px;
        box-shadow: 12px 15px 20px rgba(0, 0, 0, 0.1) !important;
    }
</style>



<!--<template>-->
  <!--<div>-->
    <!--<p v-for="classs in classes" :key="classes.class">{{ classs.class }}</p>-->
  <!--</div>-->
<!--</template>-->
<!--<script>-->
  <!--const API_URL = 'http://127.0.0.1:8000/api'-->
  <!--export default {-->
    <!--name: 'ajax',-->
    <!--data(){-->
      <!--return{-->
        <!--classes: ''-->
      <!--}-->
    <!--},-->
    <!--created(){-->
      <!--this.getClass();-->
    <!--},-->
    <!--methods: {-->
      <!--getClass: function () {-->
        <!--let self = this;-->
        <!--this.axios.get(API_URL + '/class/all/?format=json').then((response) => {-->
          <!--self.classes = response.data;-->
        <!--}).catch((response) => {-->
          <!--console.log(response.data);-->
        <!--})-->
      <!--}-->
    <!--}-->
  <!--}-->
<!--</script>-->
