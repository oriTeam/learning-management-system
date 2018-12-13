<template>
    <div class="row mx-0">
        <div class="col-lg-12 p-1">
            <div class="card p-3 mr-lg-3 mx-sm-3">
                <div class="row mx-0 justify-center" v-if="preloader">
                    <v-progress-circular :size="50" color="green" indeterminate class="mb-5"/>
                </div>
                <div v-if="!preloader" class="row m--margin-bottom-25">
                    <div class="col-lg-6 col-sm-12">
                        <img :src="imgUrl(classDetail.avatar_path)" alt="" width="100%">
                    </div>
                    <div class="col-lg-6 col-sm-12">
                        <h2 class="course-title m--margin-top-10-mobile">{{ classDetail.name}}</h2>
                        <p class="m--regular-font-size-lg2"><i class="fa fa-user"></i> Giảng viên: <a href="#">
                            {{ lecturer[0].name }}
                        </a></p>
                        <p class="m--regular-font-size-lg2"><i class="fa fa-qrcode"></i> Mã lớp học: {{
                            classDetail.code }}
                        </p>
                        <p class="m--regular-font-size-lg2"><i class="fa fa-tag"></i> Môn học: <a
                                href="#">{{ classDetail.subject }}</a></p>
                        <!--<button v-show="isStudent()" class="btn m-btn btn-success">Tham gia Khóa học</button>-->
                        <enroll-btn :class_id="classDetail.id"></enroll-btn>
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
                            <!--Danh sách học sinh ({{ this.students_list.body.length }})-->
                            Danh sách học sinh
                            <v-icon>chrome_reader_mode</v-icon>
                        </v-tab>

                        <v-tab>
                            <!--Danh sách xin vào lớp ({{ this.enroll_request_list.body.length }})-->
                            Danh sách xin vào lớp
                            <v-icon>toc</v-icon>
                        </v-tab>

                        <v-tab-item>
                            <v-card flat>
                                <!--<v-card-text>Thời gian biểu</v-card-text>-->
                                <time-line></time-line>
                            </v-card>
                        </v-tab-item>

                        <v-tab-item>
                            <v-card flat>
                                <v-data-table
                                        :headers="students_list.title"
                                        :items="students_list.body"
                                        class="elevation-1"
                                        loading
                                >
                                    <template slot="items" slot-scope="props">
                                        <td>{{ props.item.code }}</td>
                                        <td class="text-xs-left">{{     props.item.fullname }}</td>
                                        <td class="text-xs-left">{{ props.item.username }}</td>
                                        <td class="">{{ props.item.gender }}</td>
                                        <td class="">{{ props.item.phone_number }}</td>
                                        <!--<td class="">{{ props.item.personal_page }}</td>-->
                                        <td class="justify-center layout px-0">
                                            <v-icon
                                                    small
                                                    @click=""
                                            >
                                                delete
                                            </v-icon>
                                        </td>
                                    </template>
                                </v-data-table>
                            </v-card>
                        </v-tab-item>
                        <v-tab-item>
                            <v-card flat>
                                <v-data-table
                                        :headers="enroll_request_list.title"
                                        :items="enroll_request_list.body"
                                        class="elevation-1"
                                        loading
                                >
                                    <template slot="items" slot-scope="props">
                                        <td>{{ props.item.code }}</td>
                                        <td class="text-xs-left">{{ props.item.fullname }}</td>
                                        <td class="text-xs-left">{{ props.item.username }}</td>
                                        <td class="">{{ props.item.gender }}</td>
                                        <td class="">{{ props.item.phone_number }}</td>
                                        <!--<td class="">{{ props.item.personal_page }}</td>-->
                                        <td class="justify-center layout px-0">
                                            <v-icon
                                                    small
                                                    @click=""
                                            >
                                                delete
                                            </v-icon>
                                        </td>
                                    </template>
                                </v-data-table>

                            </v-card>
                        </v-tab-item>

                    </v-tabs>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    import AsideLecturer from "@/components/class/AsideLecturer";
    import EnrollButton from "@/components/class/EnrollButton";
    import TimeLine from "@/components/class/TimeLine";
    import BACKEND_URL from "@/backendServer";
    import ajax from "@/request"

    export default {
        name: "inner-class",
        data() {
            return {
                students_list: {
                    title: [
                        {
                            text: 'MSV',
                            align: 'left',
                            sortable: false,
                            value: 'code'
                        },
                        {text: 'Họ và tên', value: 'fullname'},
                        {text: 'Tên tài khoản', value: 'username'},
                        {text: 'Giới tính', value: 'gender'},
                        {text: 'Số điện thoại', value: 'phone'},
                        // {text: 'Trang cá nhân', value: 'page'},
                        {text: 'Xóa khỏi lớp', value: 'delete', sortable: false}
                    ],
                    body: [
                        {
                            "code": "000",
                            "fullname": "Chưa có dữ liệu",
                            "username": "",
                            "gender": "",
                            "phone_number": "",
                            "personal_page": ""
                        },
                        {
                            "code": "000",
                            "fullname": "Chưa có dữ liệu",
                            "username": "",
                            "gender": "",
                            "phone_number": "",
                            "personal_page": ""
                        },
                    ]
                },
                enroll_request_list: {
                    title: [
                        {
                            text: 'MSV',
                            align: 'left',
                            sortable: false,
                            value: 'code'
                        },
                        {text: 'Họ và tên', value: 'fullname'},
                        {text: 'Tên tài khoản', value: 'username'},
                        {text: 'Giới tính', value: 'gender'},
                        {text: 'Số điện thoại', value: 'phone'},
                        // {text: 'Trang cá nhân', value: 'page'},
                        {text: 'Hành động', value: 'delete', sortable: false}
                    ],
                    body: [
                        {
                            "code": "000",
                            "fullname": "Chưa có dữ liệu",
                            "username": "",
                            "gender": "",
                            "phone_number": "",
                            "personal_page": ""
                        },
                        {
                            "code": "000",
                            "fullname": "Chưa có dữ liệu",
                            "username": "",
                            "gender": "",
                            "phone_number": "",
                            "personal_page": ""
                        },
                    ]
                },
                preloader: true,
                classDetail: Object,
            }
        },
        components: {
            'sidebar': AsideLecturer,
            'enroll-btn': EnrollButton,
            'time-line': TimeLine
        },
        created() {
            let self = this;
            let class_id = this.$route.params.id;
            this.axios.get(BACKEND_URL + `/api/class/detail/${class_id}/?format=json`).then((response) => {
                self.classDetail = response.data[0];
                self.students_list.body = response.data[2].student;
                self.lecturer = response.data[1].lecturer;
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
                this.enroll_request_list.body = response.data;
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