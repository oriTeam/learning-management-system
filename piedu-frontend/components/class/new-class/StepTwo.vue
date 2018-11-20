<template>
    <div style="padding: 2rem 3rem; text-align: left;">
        <v-layout row wrap>
            <v-flex lg6 sm12 px-3 my-2>
                <div class="input-group date">
                    <label class="label col-12 px-0">Ngày bắt đầu</label>
                    <datetime class="col-12 px-0" input-class="input" v-model="start_date">
                    </datetime>
                </div>
            </v-flex>
            <v-flex lg6 sm12 px-3 my-2>
                <div class="input-group date">
                    <label class="label col-12 px-0">Ngày kết thúc</label>
                    <datetime class="col-12 px-0" input-class="input" v-model="end_date">
                    </datetime>
                </div>
            </v-flex>
            <v-flex sm12 px-3 my-2>
                <hr class="w-100">
            </v-flex>
        </v-layout>

        <v-layout row wrap>
            <v-flex sm12 px-3><h4>Lịch học lý thuyết</h4></v-flex>
            <v-flex lg2 sm12 px-3 my-2>
                <div class="field">
                    <label class="label">Thứ trong tuần</label>
                    <div class="control">
                        <div :class="['select', 'w-100', ($v.main_schedule.day_of_week.$error) ? 'is-danger' : '']">
                            <select v-model="main_schedule.day_of_week" class="w-100">
                                <option v-for="day in 6" :value="day + 1"
                                        :key="day">{{ day + 1 }}
                                </option>
                            </select>
                        </div>
                    </div>
                    <p v-if="$v.main_schedule.day_of_week.$error" class="help is-danger">Không được để trống Thứ</p>
                </div>
            </v-flex>
            <v-flex lg5 sm12 px-3 my-2>
                <div class="input-group date">
                    <label class="label col-12 px-0">Giờ bắt đầu</label>
                    <datetime type="time" class="col-12 px-0" input-class="input" v-model="main_schedule.start_session">
                    </datetime>
                </div>
            </v-flex>
            <v-flex lg5 sm12 px-3 my-2>
                <div class="input-group date">
                    <label class="label col-12 px-0">Giờ kết thúc</label>
                    <datetime type="time" class="col-12 px-0" input-class="input" v-model="main_schedule.end_session">
                    </datetime>
                </div>
            </v-flex>
            <v-flex sm12 px-3 my-2>
                <hr class="w-100">
            </v-flex>
        </v-layout>
        <v-layout row wrap v-show="!subScheduleShow">
            <v-flex class="text-xs-center">
                <v-btn color="btn-primary"
                       class="white--text" @click="subScheduleShow=true">
                    Thêm lịch học thực hành
                </v-btn>
            </v-flex>
        </v-layout>

        <transition name="subSchedule">
            <v-layout row wrap v-show="subScheduleShow">

                <v-flex lg8 sm12 px-3 text-left><h4>Lịch học Bài tập/Thực hành</h4></v-flex>
                <v-flex lg4 sm12 px-3 text-right>
                    <v-btn color="warning" dark @click="hideSubSchedule()">
                        Xóa lịch thực hành
                    </v-btn>
                </v-flex>
                <v-flex lg2 sm12 px-3 my-2>
                    <div class="field">
                        <label class="label">Thứ trong tuần</label>
                        <div class="control">
                            <div :class="['select', 'w-100']">
                                <select v-model="sub_schedule.day_of_week" class="w-100">
                                    <option v-for="day in 6" :value="day + 1"
                                            :key="day">{{ day + 1 }}
                                    </option>
                                </select>
                            </div>
                        </div>
                        <!--<p v-if="$v.sub_schedule.day_of_week.$error" class="help is-danger">Không được để trống
                        Thứ</p>-->
                    </div>
                </v-flex>
                <v-flex lg5 sm12 px-3 my-2>
                    <div class="input-group date">
                        <label class="label col-12 px-0">Giờ bắt đầu</label>
                        <datetime type="time" class="col-12 px-0" input-class="input"
                                  v-model="sub_schedule.start_session">
                        </datetime>
                    </div>
                </v-flex>
                <v-flex lg5 sm12 px-3 my-2>
                    <div class="input-group date">
                        <label class="label col-12 px-0">Giờ kết thúc</label>
                        <datetime type="time" class="col-12 px-0" input-class="input"
                                  v-model="sub_schedule.end_session">
                        </datetime>
                    </div>
                </v-flex>
                <v-flex sm12 px-3 my-2>
                    <hr class="w-100">
                </v-flex>
            </v-layout>
        </transition>

    </div>
</template>
<script>
    import {Datetime} from 'vue-datetime';
    import 'vue-datetime/dist/vue-datetime.css'
    import {Settings} from 'luxon'
    import {validationMixin} from "vuelidate";
    import {required} from "vuelidate/lib/validators";

    Settings.defaultLocale = 'vi'

    export default {
        props: ["clickedNext", "currentStep"],
        mixins: [validationMixin],
        data() {
            return {
                start_date: '',
                end_date: '',
                subScheduleShow: false,
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
        },
        components: {
            'datetime': Datetime
        },
        validations: {
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
                    this.$v.$touch();
                }
            }
        },
        mounted() {
            if (!this.$v.$invalid) {
                this.$emit("can-continue", {value: true});
            } else {
                this.$emit("can-continue", {value: false});
            }
        },
        methods: {
            hideSubSchedule: function () {
                this.subScheduleShow=false;
                this.sub_schedule.day_of_week = '';
                this.sub_schedule.start_session = '';
                this.sub_schedule.end_session = '';
            }
        }
    }

</script>

<style>
    .subSchedule-enter-active, .subSchedule-leave-active {
        transition: opacity .1s;
    }

    .subSchedule-enter, .subSchedule-leave-to {
        opacity: 0;
    }
    .warning {
        background-color: #ffc107 !important;
    }
</style>
