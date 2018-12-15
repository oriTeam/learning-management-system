<template>
    <ul class="timeline">
        <li class="timeline-item" v-if="getSyllabusSuccess" if v-for="syllabus in syllabuses" :key="syllabus.id">
            <div class="timeline-badge ">{{ syllabus.week }}</div>
            <div class="timeline-panel">
                <div class="timeline-heading">
                    <h4 class="timeline-title"> {{ syllabus.title }}</h4>
                    <div class="timeline-panel-controls">
                        <div class="controls">
                            <v-dialog v-if="isOwnLecturer()" v-model="syllabus.dialog" persistent max-width="600px">
                                <button slot="activator" class="btn btn-sm btn-link"><i class="fas fa-edit"></i> Chỉnh sửa</button>
                                <v-card>
                                    <v-card-title>
                                        <span class="headline">Chỉnh sửa Syllabus</span>
                                    </v-card-title>
                                    <v-card-text>
                                        <v-container grid-list-md>
                                            <v-layout wrap>
                                                <v-flex xs12 sm6>
                                                    <v-text-field label="Tiêu đề" required v-model="syllabus.title"
                                                                  :value="syllabus.title"></v-text-field>
                                                </v-flex>
                                                <v-flex xs12 sm6>
                                                    <v-text-field label="Nội dung tuần học" v-model="syllabus.content"
                                                                  :value="syllabus.content"></v-text-field>
                                                </v-flex>
                                                <v-flex xs12 v-for="material in syllabus.materials"
                                                     :key="material.id" :id="'material-' + material.id">
                                                    <a :href="material_url(material.file)" target="_blank">{{ material.name }}</a>
                                                    <base-button @click="deleteMaterial(material.id)" type="warning"
                                                                 size="sm"
                                                                 class="pull-right">Xóa tài
                                                        liệu
                                                    </base-button>
                                                </v-flex>
                                                <v-flex xs12>
                                                    <v-text-field type="file"
                                                            label=""
                                                            v-model="syllabus.file"
                                                    ></v-text-field>
                                                </v-flex>


                                            </v-layout>
                                        </v-container>
                                    </v-card-text>
                                    <v-card-actions>
                                        <v-spacer></v-spacer>
                                        <v-btn color="blue darken-1" flat @click="syllabus.dialog = false">Hủy</v-btn>
                                        <v-btn color="blue darken-1" flat @click="saveSyllabus(syllabus.id,
                                        syllabus.title, syllabus.content, syllabus.file)">Lưu
                                            lại</v-btn>
                                    </v-card-actions>
                                </v-card>
                            </v-dialog>
                            <!--<button class="btn btn-sm btn-link"><i class="fas fa-trash-alt"></i> Xóa</button>-->
                        </div>
                        <div class="timestamp">
                            <small class="text-muted">24. Sep 17:03</small>
                        </div>
                    </div>
                </div>
                <div class="timeline-body">
                    <p><i>
                        {{ syllabus.content }}
                    </i></p>
                    <a :href="material_url(material.file)" target="_blank" v-for="material in syllabus.materials">
                        {{ material.name }}
                    </a>
                </div>
            </div>

        </li>
    </ul>
</template>

<script>
    import BACKEND_URL from "@/backendServer";

    export default {
        name: "time-line",
        props: ['own_lecturers'],
        data() {
            return {
                getSyllabusSuccess: false,
                syllabuses: Object,
                dialog: false,
                lecturers: this.own_lecturers
            }
        },
        created() {
            this.get_syllabus();
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
            get_syllabus: function () {
                let self = this;
                let token = self.$ls.get('token');
                let classId = self.$route.params.id;
                let config = {
                    headers: {
                        "Authorization": "Token " + token.toString()
                    }
                };
                let data = {
                    'token': self.$ls.get('token')
                };
                this.axios.get(BACKEND_URL+ `/api/class/${classId}/get_syllabus`, {params: data}, config).then((res) => {
                    if(res.data.errors) {}
                    else {
                        self.getSyllabusSuccess = true;
                        self.syllabuses = res.data;
                    }
                })
            },
            material_url: function (path) {
                return BACKEND_URL + path;
            },
            saveWeekkSyllabus: function () {
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
                    if (own_lecturer.includes(user_id.toString())) {
                        return true;
                    }
                    else {
                        return false;
                    }

                }
            },
            deleteMaterial: function (material_id) {
                let self = this;
                self.$swal({
                    title: `Bạn muốn xóa tài liệu này ?`,
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
                            'token': self.$ls.get('token'),
                            'material_id': material_id
                        };
                        this.axios.post(BACKEND_URL + '/api/material/delete/', data, config).then((res) => {
                            if(res.data.success) {
                                // alert('a');
                                let id = "material-" + material_id;
                                document.getElementById(id).style.display = "none";
                                self.$swal({
                                    title: 'Đã xóa',
                                    type: 'success'
                                });

                            }
                        }).catch((res) => {
                            self.$swal({
                                title: 'Đã xảy ra lỗi. Vui lòng thử lại',
                                type: 'error'
                            })
                        });

                    }
                })
            },
            saveSyllabus: function (syllabus_id, title, content, file) {
                let self = this;
                let token = self.$ls.get('token');
                let config = {
                    headers: {
                        "Authorization": "Token " + token.toString()
                    }
                };
                let data = {
                    'syllabus_id': syllabus_id,
                    'title': title,
                    'token': self.$ls.get('token'),
                    'content': content
                };
                this.axios.post(BACKEND_URL + '/api/class/edit-syllabus', data, config).then((res) => {
                    self.$swal({
                        title: 'Sửa thành công',
                        type: 'success'
                    })
                }).catch((res) => {
                    self.$swal({
                        title: 'Đã xảy ra lỗi. Vui lòng thử lại',
                        type: 'error'
                    })
                });

                let fileconfig = {
                    headers: {
                        "Authorization": "Token " + token.toString(),
                        'Content-Type': 'multipart/form-data'
                    }
                };
                let filedata = {
                    'token': self.$ls.get('token'),
                    'file': file
                };
                this.axios.post(BACKEND_URL + '/api/syllabus/add-material', filedata, config).then((res) => {
                    self.$swal({
                        title: 'Sửa thành công',
                        type: 'success'
                    })
                }).catch((res) => {
                    self.$swal({
                        title: 'Đã xảy ra lỗi. Vui lòng thử lại',
                        type: 'error'
                    })
                });
            }
        },
    }

</script>
<style lang="scss">
    .timeline {
        list-style: none;
        padding: 20px 0 20px;
        position: relative;

        &:before {
            background-color: #eee;
            bottom: 0;
            content: " ";
            left: 50px;
            margin-left: -1.5px;
            position: absolute;
            top: 0;
            width: 3px;
        }

        > li {
            margin-bottom: 20px;
            position: relative;

            &:before,
            &:after {
                content: " ";
                display: table;
            }

            &:after {
                clear: both;
            }

            > .timeline-panel {
                border-radius: 2px;
                border: 1px solid #d4d4d4;
                box-shadow: 0 1px 2px rgba(100, 100, 100, 0.2);
                margin-left: 100px;
                padding: 20px;
                position: relative;

                .timeline-heading {
                    .timeline-panel-controls {
                        position: absolute;
                        right: 8px;
                        top: 5px;

                        .timestamp {
                            display: inline-block;
                        }

                        .controls {
                            display: inline-block;
                            padding-right: 5px;
                            border-right: 1px solid #aaa;

                            a {
                                color: #999;
                                font-size: 11px;
                                padding: 0 5px;

                                &:hover {
                                    color: #333;
                                    text-decoration: none;
                                    cursor: pointer;
                                }
                            }
                        }

                        .controls + .timestamp {
                            padding-left: 5px;
                        }
                    }
                }
            }

            .timeline-badge {
                background-color: #999;
                border-radius: 50%;
                color: #fff;
                font-size: 1.4em;
                height: 50px;
                left: 50px;
                line-height: 52px;
                margin-left: -25px;
                position: absolute;
                text-align: center;
                top: 16px;
                width: 50px;
                z-index: 2;
            }

            .timeline-badge + .timeline-panel {
                &:before {
                    border-bottom: 15px solid transparent;
                    border-left: 0 solid #ccc;
                    border-right: 15px solid #ccc;
                    border-top: 15px solid transparent;
                    content: " ";
                    display: inline-block;
                    position: absolute;
                    left: -15px;
                    right: auto;
                    top: 26px;
                }

                &:after {
                    border-bottom: 14px solid transparent;
                    border-left: 0 solid #fff;
                    border-right: 14px solid #fff;
                    border-top: 14px solid transparent;
                    content: " ";
                    display: inline-block;
                    position: absolute;
                    left: -14px;
                    right: auto;
                    top: 27px;
                }
            }
        }
    }

    .timeline-badge {
        &.primary {
            background-color: #2e6da4 !important;
        }

        &.success {
            background-color: #3f903f !important;
        }

        &.warning {
            background-color: #f0ad4e !important;
        }

        &.danger {
            background-color: #d9534f !important;
        }

        &.info {
            background-color: #5bc0de !important;
        }
    }

    .timeline-title {
        margin-top: 0;
        color: inherit;
    }

    .timeline-body {
        > p,
        > ul {
            margin-bottom: 0;
        }

        > p + p {
            margin-top: 5px;
        }
    }
</style>