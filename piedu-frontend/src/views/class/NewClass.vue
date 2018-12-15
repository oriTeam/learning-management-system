<template>
    <section class="card">
        <div style="padding: 2rem 3rem; text-align: left;">
            <v-layout row wrap>
                <v-flex lg6 sm12 px-3 my-sm-2>
                    <div class="field">
                        <label class="label">Thể loại</label>
                        <div class="control">
                            <div :class="['select', 'w-100', ($v.basic.selected_category.$error) ? 'is-danger' : '']">
                                <select v-model="basic.selected_category" class="w-100" @change="getSubjects">
                                    <option v-for="category in categories" :value="category.id"
                                            :key="category.id">{{ category.name }}
                                    </option>
                                </select>
                            </div>
                        </div>
                        <p v-if="$v.basic.selected_category.$error" class="help is-danger">Loại môn học không hợp lệ</p>
                    </div>
                </v-flex>
                <v-flex lg6 sm12 px-3 my-sm-2>
                    <div class="field">
                        <label class="label">Môn học</label>
                        <div class="control">
                            <div :class="['select', 'w-100', ($v.basic.selected_subject.$error) ? 'is-danger' : '']">
                                <select v-model="basic.selected_subject" class="w-100">
                                    <option v-for="subject in subjects" :value="subject.id" :key="subject.id">{{
                                        subject.name }}
                                    </option>
                                </select>
                            </div>
                        </div>
                        <p v-if="$v.basic.selected_subject.$error" class="help is-danger">Môn học không hợp lệ</p>
                    </div>
                </v-flex>
            </v-layout>
            <v-layout row wrap>
                <v-flex xs12 px-3 my-2>
                    <div class="field">
                        <label class="label">Mô tả</label>
                        <div class="control">
                        <textarea :class="['textarea', 'w-100', ($v.basic.description.$error) ? 'is-danger' : '']"
                                  placeholder="Mô tả lớp học"
                                  v-model="basic.description"></textarea>
                        </div>
                    </div>
                </v-flex>
            </v-layout>
            <v-layout row wrap>
                <v-flex lg6 sm12 px-3 my-2>
                    <div class="input-group date">
                        <label class="label col-12 px-0">Ngày bắt đầu</label>
                        <datetime class="col-12 px-0" input-class="input" v-model="time.start_date">
                        </datetime>
                    </div>
                </v-flex>
                <v-flex lg6 sm12 px-3 my-2>
                    <div class="input-group date">
                        <label class="label col-12 px-0">Ngày kết thúc</label>
                        <datetime class="col-12 px-0" input-class="input" v-model="time.end_date">
                        </datetime>
                    </div>
                </v-flex>
            </v-layout>

            <v-layout row wrap>
                <!--<v-flex sm12 px-3><h4>Lịch học lý thuyết</h4></v-flex>-->
                <v-flex lg2 sm12 px-3 my-2>
                    <div class="field">
                        <label class="label">Thứ trong tuần</label>
                        <div class="control">
                            <div :class="['select', 'w-100', ($v.time.main_schedule.day_of_week.$error) ? 'is-danger' :
                        '']">
                                <select v-model="time.main_schedule.day_of_week" class="w-100">
                                    <option v-for="day in 6" :value="day + 1"
                                            :key="day"> Thứ {{ day + 1 }}
                                    </option>
                                </select>
                            </div>
                        </div>
                        <p v-if="$v.time.main_schedule.day_of_week.$error" class="help is-danger">Không được để trống
                            Thứ</p>
                    </div>
                </v-flex>
                <v-flex lg5 sm12 px-3 my-2>
                    <div class="input-group date">
                        <label class="label col-12 px-0">Giờ bắt đầu</label>
                        <div class="control col-12 px-0">
                            <div :class="['select', 'w-100', ($v.time.main_schedule.start_session.$error) ? 'is-danger' :
                        '']">
                                <select v-model="time.main_schedule.start_session" class="w-100">
                                    <option v-for="session in 12" :value="session"
                                            :key="session">{{ session + 6 }}:00
                                    </option>
                                </select>
                            </div>
                        </div>
                        <p v-if="$v.time.main_schedule.start_session.$error" class="help is-danger">Không được để trống
                            giờ bắt đầu buổi học</p>

                        <!--<datetime type="time" class="col-12 px-0" input-class="input"-->
                        <!--v-model="time.main_schedule.start_session">-->
                        <!--</datetime>-->
                    </div>
                </v-flex>
                <v-flex lg5 sm12 px-3 my-2>
                    <div class="input-group date">
                        <label class="label col-12 px-0">Giờ kết thúc</label>
                        <div class="control col-12 px-0">
                            <div :class="['select', 'w-100', ($v.time.main_schedule.end_session.$error) ? 'is-danger' :
                        '']">
                                <select v-model="time.main_schedule.end_session" class="w-100">
                                    <option v-for="session in 12" :value="session"
                                            :key="session">{{ session + 6 }}:50
                                    </option>
                                </select>
                            </div>
                        </div>
                        <p v-if="$v.time.main_schedule.end_session.$error" class="help is-danger">Không được để trống
                            giờ kết thúc buổi học</p>
                        <!--<datetime type="time" class="col-12 px-0" input-class="input"-->
                        <!--v-model="time.main_schedule.end_session">-->
                        <!--</datetime>-->
                    </div>
                </v-flex>
                <v-flex sm12 px-3 my-2>
                    <hr class="w-100">
                </v-flex>
            </v-layout>
            <v-layout>
                <button class="btn btn-primary" @click="submit"> Kiểm tra và tạo lớp</button>
            </v-layout>
        </div>

    </section>
</template>

<script>
    import {validationMixin} from "vuelidate";
    import {required} from "vuelidate/lib/validators";
    import BACKEND_URL from "@/backendServer";
    import {Datetime} from 'vue-datetime';
    import 'vue-datetime/dist/vue-datetime.css'
    import {Settings} from 'luxon';

    Settings.defaultLocale = 'vi';

    export default {
        mixins: [validationMixin],
        data() {
            return {
                categories: [],
                subjects: ["Bạn phải chọn Loại lớp học trước"],
                basic: {
                    selected_category: "",
                    selected_subject: "",
                    description: ""
                },
                time: {
                    start_date: '',
                    end_date: '',
                    main_schedule: {
                        day_of_week: '',
                        start_session: '',
                        end_session: ''
                    },
                    sub_schedule: {
                        day_of_week: '',
                        start_session: '',
                        end_session: ''
                    },
                }
            };
        },
        components: {
            'datetime': Datetime,
        },
        validations: {
            basic: {
                selected_category: {
                    required
                },
                selected_subject: {
                    required
                },
                description: {
                    required
                }
            },
            time: {
                start_date: {
                    required
                },
                end_date: {
                    required
                },
                main_schedule: {
                    day_of_week: {
                        required
                    },
                    start_session: {
                        required
                    },
                    end_session: {
                        required
                    }
                }
            }
        },
        name: 'new-class',
        beforeCreate() {
            if(this.$ls.get('group') == 'student_group') {
                this.$router.push('/class/my');
                this.$swal({
                    type: 'error',
                    title: 'Bạn không phải có quyền truy cập Trang này ',
                    showConfirmButton: false,
                    timer: 1500
                });
            }
        },
        created() {
            this.getAllCategory();
        },
        methods: {
            getAllCategory: function () {
                let self = this;
                this.axios.get(BACKEND_URL + '/api/course_category/list?format=json').then((response) => {
                    self.categories = response.data;
                }).catch((response) => {
                    console.log(response);
                })
            },
            getSubjects: function () {
                let self = this;
                this.axios.get(BACKEND_URL
                    + `/api/course_category/${self.basic.selected_category}/get_subject?format=json`).then((response) => {
                    self.subjects = response.data;
                }).catch((response) => {
                    console.log(response);
                })

            },
            submit(payload) {
                // alert('end');
                let self = this;
                let token = self.$ls.get('token');
                let config = {
                    headers: {
                        "Authorization": "Token " + token.toString()
                    }
                };
                let data = {
                    "subject": this.basic.selected_subject,
                    "description": this.basic.description,
                    "time_start": this.time.start_date,
                    "time_end": this.time.end_date,
                    "session_start": this.time.main_schedule.start_session,
                    "session_end": this.time.main_schedule.end_session,
                    "day_of_week": this.time.main_schedule.day_of_week,
                    'format': "json",
                    'token': token
                };
                console.log(data);
                this.axios.post(BACKEND_URL + '/api/class/validated', data, config).then((res) => {
                    // alert(res.data.success);
                    if(res.data.success) {
                        self.$swal({
                            position: 'top-end',
                            type: 'success',
                            title: 'Tạo lớp thành công',
                            showConfirmButton: false,
                            timer: 1000
                        });
                        this.$router.push(`/class/${res.data.class_id}`);
                    }
                    else {
                        self.$swal({
                            type: 'error',
                            title: 'Lớp học bị trùng lịch hoặc thời gian không hợp lệ. Vui lòng kiểm tra lại',
                            showConfirmButton: false,
                            timer: 1000
                        });
                    }
                }).catch((res) => {
                    self.$swal({
                        title: 'Đã xảy ra lỗi. Vui lòng thử lại',
                        type: 'error'
                    })
                });

            },
        }
    }
</script>
<style scoped>
    .input, .select {
        font-size: 1rem;
    }
</style>