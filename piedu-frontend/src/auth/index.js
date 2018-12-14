import axios from 'axios';
import router from "../router";
import BACKEND_URL from "../backendServer";
const API_URL = BACKEND_URL + "/api";

export default {
    user: {
        authenticated: false,
    },
    login: function(context, creds, rediect) {
        context.axios.post(API_URL + "/auth/", creds).then((response) => {
            context.$ls.set("user", response.data.user_id);
            localStorage.setItem("user", response.data.user_id);
            context.$ls.set("username", response.data.username);
            context.$ls.set("token", response.data.token);
            context.$ls.set("group", response.data.group);
            context.$ls.set("email", response.data.email);
            context.$ls.set("avatarPath", response.data.avatarPath);
            this.user.authenticated = true;
            router.push(rediect);
            context.$swal({
                position: 'top-end',
                type: 'success',
                title: 'Đăng nhập thành công',
                showConfirmButton: false,
                timer: 1000
            });
        }).catch((response) => {
            // console.log(response);
            context.$swal({
                position: 'top-end',
                type: 'error',
                title: 'Đăng nhập thất bại. Vui lòng xem lại tên tài khoản hoặc mật khẩu',
                showConfirmButton: false,
                timer: 1000
            });
        });
    },
    logout: function (context) {
        context.$ls.remove('user');
        localStorage.removeItem("user");
        context.$ls.remove('token');
        context.$ls.remove('username');
        context.$ls.remove('email');
        context.$ls.remove('group');
        context.$ls.remove('avatarPath');
        this.user.authenticated = false;
        router.push('/login');
    },
    isAuthenticated: function(context) {
        let jwt = context.$ls.get('user');
        if(jwt) return true;
        else return false;
    },
    checkAuthenticated: function (context) {
        let jwt = context.$ls.get('user');
        if(jwt) {
            this.user.authenticated = true;
        }
        else this.user.authenticated = false;
    },
    getAuthenticatedHeader: function (context) {
        return {
            "Authorization": "Bearer" + context.$ls.get("token")
        }
    }

}
