<template>
    <div>
        <section v-if="isStudent()">
            <button v-if="this.status==0" @click="enroll()" type="button" class="btn btn-icon btn-primary"><span
                    class="btn-inner--icon"><i
                    class="ni ni-bag-17"></i></span> <span class="btn-inner--text">Tham gia lớp học</span></button>
            <button v-else-if="this.status==2" type="button" class="btn btn-icon btn-light disabled">Đang chờ xác nhận
                ...
            </button>
        </section>
        <section v-else-if="isOwnLecturer()">
            <button @click="save_syllabus()" type="button" class="btn btn-icon btn-primary"><span
                    class="btn-inner--icon"><i
                    class="ni ni-bag-17"></i></span>
                <span class="btn-inner--text">Lưu mẫu Đề cương môn học</span></button>

        </section>
    </div>
</template>
<script>
    import BACKEND_URL from "@/backendServer";

    export default {
        name: 'enroll-btn',
        data() {
            return {
                status: Number,
                classId: this.class_id,
                lecturers: this.own_lecturers
            }
        },
        props: [
            'class_id',
            'own_lecturers'
        ],
        created() {
            this.check_status()
        },
        methods: {
            enroll: function () {
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
                    'token': self.$ls.get('token')
                };
                this.axios.post(BACKEND_URL + '/api/enroll_request/create', data, config).then((res) => {
                    console.log("enroll success");
                    this.check_status();

                });
                // this.check_status();
            },
            check_status: function () {
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
            },
            save_syllabus: function () {
                let self = this;
                let token = self.$ls.get('token');
                let config = {
                    headers: {
                        "Authorization": "Token " + token.toString()
                    }
                };
                let data = {
                    'class_id': self.classId,
                    'format': "json",
                    'token': token
                };
                this.axios.post(BACKEND_URL + '/api/syllabus_template/save', data, config).then((res) => {
                    if (res.data.success) {
                        self.$swal({
                            position: 'top-end',
                            type: 'success',
                            title: 'Lưu thành công',
                            showConfirmButton: false,
                            timer: 1000
                        })
                    }
                    else {
                        self.$swal({
                            position: 'top-end',
                            type: 'error',
                            title: "Mẫu này đã tồn tại",
                            showConfirmButton: false,
                            timer: 1000
                        })
                    }

                })
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
            isOwnLecturer: function () {
                let user_id = this.$ls.get('user');
                if(this.$ls.get('group') == 'student_group') {
                    return false
                }
                else if(this.$ls.get('group') == 'admin_group') {
                    return true
                }
                else {
                    let own_lecturer = [];
                    for (let lecturer of this.lecturers) {
                        own_lecturer.push(lecturer.id.toString())
                    }
                    console.log(own_lecturer);

                    if (own_lecturer.includes(user_id.toString())) {
                        return true;
                    }
                    else {
                        return false;
                    }

                }
            }
        }
    }
</script>