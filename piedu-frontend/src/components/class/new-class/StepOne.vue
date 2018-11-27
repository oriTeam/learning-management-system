<template>
    <div style="padding: 2rem 3rem; text-align: left;">
        <v-layout row wrap>
            <v-flex lg6 sm12 px-3 my-sm-2>
                <div class="field">
                    <label class="label">Thể loại</label>
                    <div class="control">
                        <div :class="['select', 'w-100', ($v.form.selected_category.$error) ? 'is-danger' : '']">
                            <select v-model="form.selected_category" class="w-100" @change="getSubjects">
                                <option v-for="category in categories" :value="category.id"
                                        :key="category.id">{{ category.name }}
                                </option>
                            </select>
                        </div>
                    </div>
                    <p v-if="$v.form.selected_category.$error" class="help is-danger">Loại môn học không hợp lệ</p>
                </div>
            </v-flex>
            <v-flex lg6 sm12 px-3 my-sm-2>
                <div class="field">
                    <label class="label">Môn học</label>
                    <div class="control">
                        <div :class="['select', 'w-100', ($v.form.selected_subject.$error) ? 'is-danger' : '']">
                            <select v-model="form.selected_subject" class="w-100">
                                <option v-for="subject in subjects" :value="subject.id" :key="subject.id">{{
                                    subject.name }}
                                </option>
                            </select>
                        </div>
                    </div>
                    <p v-if="$v.form.selected_subject.$error" class="help is-danger">Môn học không hợp lệ</p>
                </div>
            </v-flex>
        </v-layout>
        <v-layout row wrap>
            <v-flex xs12 px-3 my-2>
                <div class="field">
                    <label class="label">Mô tả</label>
                    <div class="control">
                        <textarea :class="['textarea', 'w-100', ($v.form.description.$error) ? 'is-danger' : '']"
                                  placeholder="Mô tả lớp học"
                                  v-model="form.description"></textarea>
                    </div>
                </div>
            </v-flex>
        </v-layout>
    </div>
</template>
<style>
</style>

<script>
    import {validationMixin} from "vuelidate";
    import {required} from "vuelidate/lib/validators";

    export default {
        props: ["clickedNext", "currentStep"],
        mixins: [validationMixin],
        data() {
            return {
                categories: [],
                subjects: ["Bạn phải chọn Loại lớp học trước"],
                form: {
                    selected_category: "",
                    selected_subject: "",
                    description: ""
                }
            };
        },
        validations: {
            form: {
                selected_category: {
                    required
                },
                selected_subject: {
                    required
                },
                description: {
                    required
                }
            }
        },
        watch: {
            $v: {
                handler: function (val) {
                    if (!val.$invalid) {
                        this.$emit("can-continue", {value: true});
                    } else {
                        this.$emit("can-continue", {value: false});
                    }
                },
                deep: true
            },
            clickedNext(val) {
                if (val === true) {
                    this.$v.form.$touch();
                }
            },
            form: {
                handler: function () {
                    this.$emit("form", this.form)
                },
                deep: true,
            }
        },
        mounted() {
            if (!this.$v.$invalid) {
                this.$emit("can-continue", {value: true});
            } else {
                this.$emit("can-continue", {value: false});
            }
        },
        created() {
            this.getAllCategory();
        },
        methods: {
            getAllCategory: function () {
                self = this;
                this.axios.get('/api/course_category/list?format=json').then((response) => {
                    self.categories = response.data;
                }).catch((response) => {
                    console.log(response);
                })
            },
            getSubjects: function () {
                self = this;
                this.axios.get(`/api/course_category/${self.form.selected_category}/get_subject?format=json`).then((response) => {
                    self.subjects = response.data;
                }).catch((response) => {
                    console.log(response);
                })

            }
        }
    };
</script>
