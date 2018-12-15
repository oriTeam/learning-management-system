<template>
    <div class="profile-page">
        <section class="section-profile-cover section-shaped my-0">
            <div class="shape shape-style-1 shape-primary alpha-4  bg-image bg-parallax overlay">
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
            </div>
        </section>
        <section class="section section-skew">
            <div class="container">
                <card shadow class="card-profile mt--300" no-body>
                    <div class="px-4">
                        <div class="row justify-content-center">
                            <div class="col-lg-3 order-lg-2">
                                <div class="card-profile-image">
                                    <a href="#">
                                        <img :src="imageUrl(profile.avatar)" class="rounded-circle">
                                    </a>
                                </div>
                            </div>
                            <div class="col-lg-4 order-lg-3 text-lg-right align-self-lg-center">
                                <div class="card-profile-actions py-4 mt-lg-0">
                                    <!--<v-btn slot="activator" color="primary" dark>Open Dialog</v-btn>-->
                                    <!--<base-button type="info" size="sm" class="mr-4">Connect</base-button>-->
                                    <!--<base-button type="default" size="sm" class="float-right">Message</base-button>-->
                                    <v-dialog v-model="editProfile.dialog" fullscreen hide-overlay
                                              transition="dialog-bottom-transition">
                                        <base-button slot="activator" type="info" size="sm" class="mr-4">Sửa thông
                                            tin cá nhân
                                        </base-button>
                                        <v-card>
                                            <v-toolbar dark color="#5e72e4">
                                                <v-btn icon dark @click="editProfile.dialog = false">
                                                    <v-icon>close</v-icon>
                                                </v-btn>
                                                <v-toolbar-title>Thay đổi thông tin cá nhân</v-toolbar-title>
                                                <v-spacer></v-spacer>
                                                <v-toolbar-items>
                                                    <v-btn dark flat @click="editProfile.dialog = false">Lưu lại</v-btn>
                                                </v-toolbar-items>
                                            </v-toolbar>
                                            <v-list three-line subheader>
                                                <!--<v-subheader>User Controls</v-subheader>-->
                                                <v-card-text>
                                                    <v-container grid-list-md>
                                                        <v-layout wrap>
                                                            <v-flex xs12 sm6 md4>
                                                                <v-text-field label="Họ"
                                                                              required></v-text-field>
                                                            </v-flex>
                                                            <v-flex xs12 sm6 md4>
                                                                <v-text-field label="Tên"></v-text-field>
                                                            </v-flex>
                                                            <v-flex xs12 sm6 md4>
                                                                <v-text-field
                                                                        label="Mã sinh viên/giảng viên"
                                                                        required
                                                                ></v-text-field>
                                                            </v-flex>
                                                            <v-flex xs12 sm6 md4>
                                                                <v-select
                                                                        :items="['Nam', 'Nữ', 'Khác']"
                                                                        label="Giới tính"
                                                                ></v-select>
                                                            </v-flex>
                                                            <v-flex xs12 sm6 md4>
                                                                <v-text-field label="Số điện thoại"
                                                                              required></v-text-field>
                                                            </v-flex>
                                                            <v-flex xs12 sm6 md4>
                                                                <v-text-field
                                                                        label="Tên đơn vị/lớp"
                                                                        required
                                                                ></v-text-field>
                                                            </v-flex>
                                                            <v-flex xs12>
                                                                <v-text-field label="Địa chỉ Email"
                                                                              required></v-text-field>
                                                            </v-flex>
                                                            <v-flex xs12>
                                                                <v-text-field label="Địa chỉ liên hệ"
                                                                              required></v-text-field>
                                                            </v-flex>
                                                        </v-layout>
                                                    </v-container>
                                                </v-card-text>
                                            </v-list>
                                        </v-card>
                                    </v-dialog>
                                    <v-dialog v-model="changePassword.dialog" persistent max-width="600px">
                                        <!--<v-btn slot="activator" color="primary" dark>Open Dialog</v-btn>-->
                                        <base-button slot="activator" type="default" size="sm" class="mr-4" >Đổi mật
                                            khẩu
                                        </base-button>
                                        <v-card>
                                            <v-card-title>
                                                <span class="headline   ">Thay đổi mật khẩu</span>
                                            </v-card-title>
                                            <v-card-text>
                                                <v-container grid-list-md>
                                                    <v-layout wrap>
                                                        <v-flex xs12>
                                                            <v-text-field
                                                                    v-model="changePassword.currentPassword"
                                                                    :append-icon="changePassword.showCurrentPass ? 'visibility_off'
                                                                    : 'visibility'"
                                                                    :type="changePassword.showCurrentPass ? 'text' :
                                                                    'password'"
                                                                    name="input-10-1"
                                                                    label="Nhập mật khẩu hiện tại của bạn"
                                                                    hint="At least 8 characters"
                                                                    counter
                                                                    @click:append="changePassword.showCurrentPass =
                                                                    !changePassword.showCurrentPass"
                                                            ></v-text-field>
                                                        </v-flex>
                                                        <v-flex xs12>
                                                            <v-text-field
                                                                    v-model="changePassword.newPassword1"
                                                                    :append-icon="changePassword.showNewPass1 ?
                                                                    'visibility_off'
                                                                    : 'visibility'"
                                                                    :type="changePassword.showNewPass1 ? 'text' :
                                                                    'password'"
                                                                    name="input-10-1"
                                                                    label="Nhập mật khẩu mới của bạn"
                                                                    hint="At least 8 characters"
                                                                    counter
                                                                    @click:append="changePassword.showNewPass1 =
                                                                    !changePassword.showNewPass2"
                                                            ></v-text-field>
                                                        </v-flex>
                                                        <v-flex xs12>
                                                            <v-text-field
                                                                    v-model="changePassword.newPassword2"
                                                                    :append-icon="changePassword.showNewPass2 ?
                                                                    'visibility_off'
                                                                    : 'visibility'"
                                                                    :type="changePassword.showNewPass2 ? 'text' :
                                                                    'password'"
                                                                    name="input-10-1"
                                                                    label="Nhập lại mật khẩu mới của bạn"
                                                                    hint="At least 8 characters"
                                                                    counter
                                                                    @click:append="changePassword.showNewPass2 =
                                                                    !changePassword.showNewPass2"
                                                            ></v-text-field>
                                                        </v-flex>

                                                    </v-layout>
                                                </v-container>
                                            </v-card-text>
                                            <v-card-actions>
                                                <v-spacer></v-spacer>
                                                <v-btn color="blue darken-1" flat @click="changePassword.dialog =
                                                false">Hủy
                                                </v-btn>
                                                <v-btn color="blue darken-1" flat @click="submitChangePassword()">Lưu
                                                    lại
                                                </v-btn>
                                            </v-card-actions>
                                        </v-card>
                                    </v-dialog>
                                </div>
                            </div>
                            <div class="col-lg-4 order-lg-1">
                                <div class="card-profile-stats d-flex justify-content-center">
                                    <div>
                                        <span class="heading">22</span>
                                        <span class="description">Số lớp đang tham gia</span>
                                    </div>
                                    <div>
                                        <span class="heading">10</span>
                                        <span class="description">Số lớp đã tham gia</span>
                                    </div>

                                </div>
                            </div>
                        </div>
                        <div class="text-center mt-5">
                            <h3>{{ profile.fullname }}
                                <!--<span class="font-weight-light">, 27</span>-->
                            </h3>
                            <div class="h6 font-weight-300"><i class="ni location_pin mr-2"></i> {{
                                profile.phone_number }}
                            </div>
                            <div class="h6 font-weight-300"><i class="ni location_pin mr-2"></i> {{
                                getName(profile.group) }}
                            </div>
                            <div class="h6 mt-4"><i class="ni business_briefcase-24 mr-2"></i>{{ profile.unit }}
                            </div>
                            <div><i class="ni education_hat mr-2"></i>Đại Học Công Nghệ - ĐHQGHN</div>
                        </div>
                        <div class="mt-5 py-5 border-top text-center">
                            <div class="row justify-content-center">
                                <div class="col-lg-9">

                                </div>
                            </div>
                        </div>
                    </div>
                </card>
            </div>
        </section>
    </div>
</template>
<script>
    import BACKEND_URL from "@/backendServer";


    export default {
        name: "profile",
        data() {
            return {
                notExist: true,
                currentUserId: this.$ls.get('user'),
                profileUserId: this.$route.params.id,
                profile: Object,
                editProfile: {
                    dialog: false,
                },
                changePassword: {
                    dialog: false,
                    showCurrentPass: false,
                    showNewPass1: false,
                    showNewPass2: false,
                    currentPassword: '',
                    newPassword1: '',
                    newPassword2: '',

                }
            }
        },
        components: {},
        created() {
            this.getProfile();
        },
        methods: {
            getProfile: function () {
                let self = this;
                let token = self.$ls.get('token');
                let config = {
                    headers: {
                        "Authorization": "Token " + token.toString()
                    }
                };
                let data = {
                    'token': token,
                    'format': 'json',
                    'profile_id': this.profileUserId,
                };
                this.axios.post(BACKEND_URL + '/api/user/detail/', data, config).then((res) => {
                    console.log(res.data);
                    if (res.data.success) {
                        self.notExist = false;
                        self.profile = res.data.profile;
                    }
                    else {
                        self.notExist = true;
                        self.$swal({
                            type: 'error',
                            title: 'Người dùng không tồn tại',
                            showConfirmButton: false,
                            timer: 3000
                        });
                        self.$router.go(-1);
                    }
                }).catch((res) => {

                })
            },
            imageUrl: function (path) {
                return BACKEND_URL + path;
            },
            getName: function (group) {
                if (group == "lecturer_group") {
                    return "Giảng viên";
                }
                else if (group == "student_group") {
                    return "Sinh viên";
                }
                else if (group == "admin_group") {
                    return "Quản trị viên";
                }
            },
            submitChangePassword: function () {
                let self = this;
                if (this.changePassword.newPassword2 == '' || this.changePassword.newPassword1 == '' ||
                    this.changePassword.currentPassword == '') {
                    this.$swal({
                        type: 'error',
                        title: 'Không được để trống trường nào',
                        showConfirmButton: false,
                        timer: 1500
                    });
                }
                else if (this.changePassword.newPassword2 != this.changePassword.newPassword1) {
                    this.$swal({
                        type: 'error',
                        title: 'Hai mật khẩu mới của bạn không trùng khớp',
                        showConfirmButton: false,
                        timer: 1500
                    });
                }
                else if (this.changePassword.newPassword2.length < 8) {
                    this.$swal({
                        type: 'error',
                        title: 'Mật khẩu mới chưa đủ 8 kí tự',
                        showConfirmButton: false,
                        timer: 1500
                    });
                }
                else {
                    let token =self.$ls.get('token');
                    let config = {
                    headers: {
                        "Authorization": "Token " + token.toString()
                    }
                };
                    let data = {
                    'token': token,
                    'format': 'json',
                    'old_password' : this.changePassword.currentPassword,
                    'new_password': this.changePassword.newPassword1,
                };
                this.axios.post(BACKEND_URL + '/api/user/change-password', data, config).then((res) => {
                    console.log(res.data);
                });
  
                }
            }
        }
    };
</script>
<style scoped>
    .profile-page .card-profile .card-profile-image img {
        max-width: 250px;
    }
</style>
