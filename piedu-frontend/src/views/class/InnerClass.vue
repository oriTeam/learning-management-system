<template>
    <div class="row mx-0">
        <div class="col-lg-12 px-1">
            <div class="card border-0 shadow h-100 p-3 mr-lg-3 mx-sm-3">
                <div class="row mx-0 justify-center" v-if="preloader">
                    <v-progress-circular :size="30" color="green" indeterminate class="mb-5"/>
                </div>
                <div v-if="!preloader" class="row m--margin-bottom-25">
                    <div class="col-lg-6 col-sm-12">
                        <img class="rounded" :src="imgUrl(classDetail.avatar_path)" alt="" width="100%">
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
                        <enroll-btn :class_id="classDetail.id" :own_lecturers="this.lecturer"></enroll-btn>
                    </div>
                </div>
                <hr/>
                <div v-if="!preloader" class="row mx-0">
                    <v-tabs class="w-100"
                            centered
                            color="#5e72e4"
                            dark
                            icons-and-text
                            grow>
                        <v-tabs-slider color="yellow"></v-tabs-slider>

                        <v-tab>
                            Thời gian biểu
                            <v-icon>timeline</v-icon>
                        </v-tab>

                        <v-tab>
                            Danh sách học sinh ({{ this.students_list.body.length }})
                            <!--Danh sách học sinh-->
                            <v-icon>chrome_reader_mode</v-icon>
                        </v-tab>

                        <v-tab>
                            Danh sách xin vào lớp ({{ this.enroll_request_list.body.length }})
                            <!--Danh sách xin vào lớp-->
                            <v-icon>toc</v-icon>
                        </v-tab>

                        <v-tab-item >
                            <v-card flat v-if="this.status == 1">
                                <!--<v-card-text>Thời gian biểu</v-card-text>-->
                                <time-line :own_lecturers="this.lecturer"></time-line>
                            </v-card>
                            <div v-else class="w-100 my-3 mx-0 alert alert-info"
                                         key="emptyFutureClass">
                                        <strong>Bạn chưa enroll </strong>
                                    </div>
                        </v-tab-item>

                        <v-tab-item>
                            <v-card flat v-if="this.status == 1">
                                <section v-if="students_list.body.length == 0">
                                    <div class="w-100 my-3 mx-0 alert alert-warning"
                                         key="emptyFutureClass">
                                        <strong>Danh sách trống. </strong>
                                    </div>
                                </section>
                                <v-data-table v-else
                                              :headers="students_list.title"
                                              :items="students_list.body"
                                              class="elevation-1"
                                              loading
                                >
                                    <template slot="items" slot-scope="props">
                                        <td>{{ props.item.code }}</td>
                                        <td class="text-xs-left">
                                            <router-link :to="{ name: 'profile', params: { id:
                                        props.item.id}}"> {{ props.item.fullname }}
                                            </router-link>
                                        </td>
                                        <td class="text-xs-left">{{ props.item.username }}</td>
                                        <td class="">{{ props.item.gender }}</td>
                                        <td class="">{{ props.item.phone_number }}</td>
                                        <!--<td class="">{{ props.item.personal_page }}</td>-->
                                        <td class="justify-center layout px-0">
                                            <base-button v-if="isOwnLecturer()"
                                                         @click="deleteStudentFromClass(props.item.id,
                                            props.item.fullname)"
                                                         size="sm"
                                                         type="warning" class="h-75 mt-1">
                                                <v-icon color="#fff"
                                                        small
                                                >
                                                    delete
                                                </v-icon>
                                            </base-button>
                                            <!--<base-button v-else disabled size="sm"-->
                                                         <!--type="warning" class="h-75 mt-1">-->
                                                <!--<v-icon color="#fff"-->
                                                        <!--small-->
                                                <!--&gt;-->
                                                    <!--delete-->
                                                <!--</v-icon>-->
                                            <!--</base-button>-->
                                        </td>
                                    </template>
                                </v-data-table>
                            </v-card>
                            <div v-else class="w-100 my-3 mx-0 alert alert-info"
                                         key="emptyFutureClass">
                                        <strong>Bạn chưa enroll </strong>
                                    </div>
                        </v-tab-item>
                        <v-tab-item>
                            <v-card flat v-if="this.status == 1">
                                <section v-if="enroll_request_list.body.length == 0">
                                    <div class="w-100 my-3 mx-0 alert alert-warning"
                                         key="emptyFutureClass">
                                        <strong>Danh sách trống. </strong>
                                    </div>


                                </section>
                                <v-data-table v-else
                                              :headers="enroll_request_list.title"
                                              :items="enroll_request_list.body"
                                              class="elevation-1"
                                              loading
                                >
                                    <template slot="items" slot-scope="props">
                                        <td>{{ props.item.code }}</td>
                                        <td class="text-xs-left">
                                            <router-link :to="{ name: 'profile', params: { id:
                                        props.item.id}}"> {{ props.item.fullname}}
                                            </router-link>
                                        </td>
                                        <td class="text-xs-left">{{ props.item.username }}</td>
                                        <td class="">{{ props.item.gender }}</td>
                                        <td class="">{{ props.item.phone_number }}</td>
                                        <!--<td class="">{{ props.item.personal_page }}</td>-->
                                        <td class="justify-xs-center layout px-0">
                                            <span v-if="isOwnLecturer()">
                                                <base-button @click="addStudentIntoClass(props.item.id)"
                                                             type="success"
                                                             size="sm" class="h-75 mt-1"><i class="fa fa-check"></i>
                                                </base-button>
                                                <base-button @click="deleteEnrollRequest(props.item.id,
                                                props.item.fullname)" size="sm" type="warning"
                                                             class="h-75 mt-1">
                                                    <v-icon color="#fff"
                                                            small
                                                    >
                                                        delete
                                                    </v-icon>
                                                </base-button>
                                            </span>
                                        </td>
                                    </template>
                                </v-data-table>

                            </v-card>
                            <div v-else class="w-100 my-3 mx-0 alert alert-info"
                                         key="emptyFutureClass">
                                        <strong>Bạn chưa enroll </strong>
                                    </div>
                        </v-tab-item>

                    </v-tabs>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    import Aside from "@/components/class/Aside";
    import ClassButton from "@/components/class/ClassButton";
    import TimeLine from "@/components/class/TimeLine";
    import BACKEND_URL from "@/backendServer";
    import ajax from "@/request"

    export default {
        name: "inner-class",
        data() {
            return {
                classId: this.$route.params.id,
                students_list: {
                    title: [
                        {
                            text: 'MSV',
                            align: 'left',
                            value: 'code'
                        },
                        {text: 'Họ và tên', value: 'fullname'},
                        {text: 'Tên tài khoản', value: 'username'},
                        {text: 'Giới tính', value: 'gender'},
                        {text: 'Số điện thoại', value: 'phone'},
                        // {text: 'Trang cá nhân', value: 'page'},
                        {text: 'Hành động', value: 'delete', sortable: false}
                    ],
                    body: []
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
                    body: []
                },
                preloader: true,
                classDetail: Object,
                lecturer: [],
                status: Number,
            }
        },
        components: {
            'sidebar': Aside,
            'enroll-btn': ClassButton,
            'time-line': TimeLine
        },
        created() {
            this.getData();
            this.check_status();
        },
        methods: {
            getData: function () {
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
            deleteStudentFromClass: function (student_id, name) {
                let self = this;
                self.$swal({
                    title: `Bạn muốn xóa sinh viên ${name} khỏi lớp ?`,
                    type: 'warning',
                    showCancelButton: true,
                    confirmButtonColor: '#d33',
                    cancelButtonColor: '#3085d6',
                    confirmButtonText: 'Có',
                    cancelButtonText: 'Hủy'
                }).then((result) => {
                    if (result.value) {
                        let self = this;
                        let token = self.$ls.get('token');
                        let config = {
                            headers: {
                                "Authorization": "Token " + token.toString()
                            }
                        };
                        let data = {
                            'class_id': self.classId,
                            'token': self.$ls.get('token'),
                            'student_id': student_id
                        };
                        this.axios.post(BACKEND_URL + '/api/class-student/delete/', data, config).then((res) => {
                            this.getData();
                        });
                        self.$swal({
                            title: 'Đã xóa',
                            type: 'success'
                        }).catch((res) => {
                            self.$swal({
                                title: 'Đã xảy ra lỗi. Vui lòng thử lại',
                                type: 'error'
                            })
                        });
                    }
                })
            },
            addStudentIntoClass: function (student_id) {
                let self = this;
                let token = self.$ls.get('token');
                let config = {
                    headers: {
                        "Authorization": "Token " + token.toString()
                    }
                };
                let data = {
                    'class_id': self.classId,
                    'token': self.$ls.get('token'),
                    'student_id': student_id
                };
                this.axios.post(BACKEND_URL + '/api/class-student/add/', data, config).then((res) => {
                    this.getData();
                    self.$swal({
                        title: 'Thêm thành công',
                        type: 'success'
                    })
                }).catch((res) => {
                    self.$swal({
                        title: 'Đã xảy ra lỗi. Vui lòng thử lại',
                        type: 'error'
                    })
                });

            },
            deleteEnrollRequest: function (student_id, name) {
                let self = this;
                self.$swal({
                    title: `Bạn muốn xóa sinh viên ${name} khỏi danh sách xin vào lớp ?`,
                    type: 'warning',
                    showCancelButton: true,
                    confirmButtonColor: '#d33',
                    cancelButtonColor: '#3085d6',
                    confirmButtonText: 'Có',
                    cancelButtonText: 'Hủy'
                }).then((result) => {
                    if (result.value) {
                        let self = this;
                        let token = self.$ls.get('token');
                        let config = {
                            headers: {
                                "Authorization": "Token " + token.toString()
                            }
                        };
                        let data = {
                            'class_id': self.classId,
                            'token': self.$ls.get('token'),
                            'student_id': student_id
                        };
                        this.axios.post(BACKEND_URL + '/api/enroll_request/delete/', data, config).then((res) => {
                            this.getData();
                            self.$swal({
                                title: 'Đã xóa',
                                type: 'success'
                            })
                        }).catch((res) => {
                            self.$swal({
                                title: 'Đã xảy ra lỗi. Vui lòng thử lại',
                                type: 'error'
                            })
                        });

                    }
                })
            },
            apply_syllabus: function () {
                let self = this;
                let token = self.$ls.get('token');
                let config = {
                    headers: {
                        "Authorization": "Token " + token.toString()
                    }
                };
                let data = {
                    'class_id': this.classId,
                    'token': self.$ls.get('token'),
                    'template_class_id': 816
                };
                this.axios.post(BACKEND_URL + '/api/syllabus_template/add', data, config).then((res) => {
                    console.log("apply success");
                });
            },
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
                if (response.data.success) {
                    this.enroll_request_list.body = response.data.students;
                }
                else {
                    this.enroll_request_list.body = []
                }

            },
            get_enroll_request_error: function (response) {
                console.log(response);
            },
            imgUrl: function (path) {
                return BACKEND_URL + path;
            },
            isOwnLecturer: function () {
                let user_id = this.$ls.get('user');
                if(this.$ls.get('group') == 'student_group') {
                    return false
                }
                else {
                    let own_lecturer = [];
                    for (let lecturer of this.lecturer) {
                        own_lecturer.push(lecturer.id.toString())
                    }
                    if (own_lecturer.includes(user_id.toString())) {
                        return true;
                    }
                    else {
                        return false;
                    }

                }
            },
            check_status: function () {
                if(this.$ls.get('group') == 'lecturer_group' || this.$ls.get('group') == 'admin_group') {
                    this.status = 1;
                }
                else {
                    let self = this;
                    let token = self.$ls.get('token');
                    let config = {
                        headers: {
                            "Authorization": "Token " + token.toString()
                        }
                    };
                    let data = {
                        'own_class': self.classId,
                        'student': self.$ls.get('user'),
                        'token': self.$ls.get('token'),
                        'format': "json"
                    };
                    this.axios.get(BACKEND_URL + '/api/class/student_status', {params: data}, config).then((res) => {
                        self.status = res.data.code;
                    })
                }
            },
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