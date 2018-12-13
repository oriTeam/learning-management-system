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
                                    <base-button type="info" size="sm" class="mr-4">Connect</base-button>
                                    <base-button type="default" size="sm" class="float-right">Message</base-button>
                                </div>
                            </div>
                            <div class="col-lg-4 order-lg-1">
                                <div class="card-profile-stats d-flex justify-content-center">
                                    <div>
                                        <span class="heading">22</span>
                                        <span class="description">Friends</span>
                                    </div>
                                    <div>
                                        <span class="heading">10</span>
                                        <span class="description">Photos</span>
                                    </div>
                                    <div>
                                        <span class="heading">89</span>
                                        <span class="description">Comments</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="text-center mt-5">
                            <h3>{{ profile.fullname }}
                                <!--<span class="font-weight-light">, 27</span>-->
                            </h3>
                            <div class="h6 font-weight-300"><i class="ni location_pin mr-2"></i> {{
                                getName(profile.group)
                                }}
                            </div>
                            <div class="h6 mt-4"><i class="ni business_briefcase-24 mr-2"></i>{{ profile.unit }}
                            </div>
                            <div><i class="ni education_hat mr-2"></i>University of Computer Science</div>
                        </div>
                        <div class="mt-5 py-5 border-top text-center">
                            <div class="row justify-content-center">
                                <div class="col-lg-9">
                                    <p>An artist of considerable range, Ryan — the name taken by Melbourne-raised,
                                        Brooklyn-based Nick Murphy — writes, performs and records all of his own music,
                                        giving it a warm, intimate feel with a solid groove structure. An artist of
                                        considerable range.</p>
                                    <a href="#">Show more</a>
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
            }
        }
    };
</script>
<style scoped>
    .profile-page .card-profile .card-profile-image img {
        max-width: 250px;
    }
</style>
