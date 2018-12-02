<template xmlns="http://www.w3.org/1999/html">
    <!--<div>-->
    <!--<section class="section section-profile-cover section-shaped my-0">-->
    <!--<div class="shape shape-style-1 shape-primary shape-skew alpha-4">-->
    <!--<span></span>-->
    <!--<span></span>-->
    <!--<span></span>-->
    <!--<span></span>-->
    <!--<span></span>-->
    <!--<span></span>-->
    <!--<span></span>-->
    <!--</div>-->
    <!--</section>-->
    <!--<section class="section section-skew">-->
    <!--<div class="container inner-content mt&#45;&#45;500">-->
    <!--<div class="row">-->
    <!--<div class="col-lg-3" id="innerside">-->
    <!--<a href="javascript:void(0)" class="closebtn" @click="closeSidebar">&times;</a>-->
    <!--<sidebar></sidebar>-->
    <!--</div>-->
    <!--<div class="col-lg-9 col-sm-12 card p-3">-->
    <div class="card p-3">
        <div class="row mx-0 justify-center" v-if="preloader">
            <v-progress-circular :size="50" color="green" indeterminate class="mb-5"/>
        </div>
        <div v-if="!preloader" class="row m--margin-bottom-25">
            <div class="col-lg-4 col-sm-12">
                <img :src="imgUrl(classDetail.avatar_path)" alt="" width="100%">
            </div>
            <div class="col-lg-8 col-sm-12">
                <h2 class="course-title m--margin-top-10-mobile">{{ classDetail.name}}</h2>
                <p class="m--regular-font-size-lg2"><i class="fa fa-user"></i> Giảng viên: <a href="#">
                    Hoàng Xuân Tùng
                </a></p>
                <p class="m--regular-font-size-lg2"><i class="fa fa-qrcode"></i> Mã lớp học: {{
                    classDetail.code }}
                </p>
                <p class="m--regular-font-size-lg2"><i class="fa fa-tag"></i> Môn học: <a
                        href="#">{{ classDetail.subject }}</a></p>
                <button v-show="isStudent()" class="btn m-btn btn-success">Tham gia Khóa học</button>
            </div>
        </div>
        <hr/>
        <div v-if="!preloader" class="row mx-0 mt-3">
            <v-tabs class="w-100"
                    centered
                    color="cyan"
                    dark
                    icons-and-text
                    grow>
                <v-tabs-slider color="yellow"></v-tabs-slider>

                <v-tab>
                    Thời gian biểu
                    <v-icon>timeline</v-icon>
                </v-tab>

                <v-tab>
                    Danh sách học sinh
                    <v-icon>chrome_reader_mode</v-icon>
                </v-tab>

                <v-tab>
                    Danh sách xin vào lớp
                    <v-icon>toc</v-icon>
                </v-tab>

                <v-tab-item>
                    <v-card flat>
                        <v-card-text>Thời gian biểu</v-card-text>

                    </v-card>
                </v-tab-item>

                <v-tab-item>
                    <v-card flat>
                        <v-card-text>Danh sách sinh viên</v-card-text>
                        <v-card-text v-for="student in students"
                                     :key="student.id">
                            {{ student }}
                        </v-card-text>
                    </v-card>
                </v-tab-item>
                <v-tab-item>
                    <v-card flat>
                        <v-card-text>Danh sách xin vào lớp</v-card-text>
                    </v-card>
                </v-tab-item>

                <!--<v-tab-item-->
                <!--v-for="i in 3"-->
                <!--:id="'tab-' + i"-->
                <!--:key="i">-->
                <!--<v-card flat>-->
                <!--<v-card-text>{{ text }}</v-card-text>-->
                <!--</v-card>-->
                <!--</v-tab-item>-->
            </v-tabs>
        </div>
    </div>
    <!--</div>-->
    <!--</div>-->
    <!--</div>-->
    <!--</section>-->
    <!--<div @click="openSidebar" id="inner-open-menu">-->
    <!--Open-->
    <!--</div>-->
    <!--</div>-->
</template>
<script>
    import AsideLecturer from "@/components/class/AsideLecturer";
    import BACKEND_URL from "@/backendServer";
    import ajax from "@/request"

    export default {
        name: "inner-class",
        data() {
            return {
                preloader: true,
                classDetail: Object,
                students: Object,
                enrollRequestStudents: Object,
                text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'
            }
        },
        components: {
            'sidebar': AsideLecturer,
        },
        created() {
            let self = this;
            let class_id = this.$route.params.id;
            this.axios.get(BACKEND_URL + `/api/class/detail/${class_id}/?format=json`).then((response) => {
                self.classDetail = response.data[0];
                self.students = response.data[1];
                self.preloader = false;
            }).catch((response) => {
                console.log(response);
            });
            ajax.send(this, 'get', `/api/class/${class_id}/get_enroll_request`, {}, this.get_enroll_request_success,
                this.get_enroll_request_error);
        },
        methods: {
            isStudent: function () {
                if (this.$ls.get('group') == 'student_group') {
                    return true;
                }
                else return false;
            },
            isLecturer: function () {
                if (this.$ls.get('group') == 'lecturer_group') {
                    return true;
                }
                return false;
            },
            get_enroll_request_success: function (response) {
                self.enrollRequestStudents = response.data;
            },
            get_enroll_request_error: function (response) {
                console.log(response);
            },
            imgUrl: function (path) {
                return BACKEND_URL + path;
            }
        }
    }
</script>
<style lang="scss">
    .inner-class-box {
        margin-top: -300px;
    }

    @media (max-width: 992px) {
        #innerside {
            /*display: none;*/
            height: 100%; /* 100% Full-height */
            width: 0; /* 0 width - change this with JavaScript */
            position: fixed; /* Stay in place */
            z-index: 1200; /* Stay on top */
            top: 0; /* Stay at the top */
            left: 0;
            padding: 0;
            background-color: #fff; /* Black*/
            overflow-x: hidden; /* Disable horizontal scroll */
            padding-top: 60px; /* Place content 60px from the top */
            transition: 0.5s; /* 0.5 second transition effect to slide in the sidenav */
        }
    ;
    }

    @media screen and (min-width: 992px) {
        #innerside {
            .closebtn {
                display: none;
            }
        }
    ;
        #inner-open-menu {
            display: none;
        }
    }

    .section-innerclass-cover {
        height: 450px;
        background-size: cover;
        background-position: center center;
    }

    #innerside {
        .closebtn {
            position: absolute;
            top: 0;
            right: 25px;
            font-size: 36px;
            margin-left: 50px;
        }
    }

    #inner-open-menu {
        position: fixed;
        bottom: 70%;
        right: 0px;
        font-size: 15px;
        z-index: 1200;
    }

    .inner-content {
        margin-top: -300px !important;
    }

    @media (min-width: 992px) {
        .mt--500 {
            margin-top: -500px !important;
        }
    }
</style>