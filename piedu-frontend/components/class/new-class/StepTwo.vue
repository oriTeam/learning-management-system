<template>
    <div style="padding: 2rem 3rem; text-align: left;">
        <v-layout row wrap>
            <v-flex lg6 sm12 px-3 my-2>
                <div class="input-group date">
                    <label class="label col-12">Ngày bắt đầu</label>
                    <datetime class="col-12" input-class="input" v-model="start_date">
                    </datetime>
                </div>
            </v-flex>
            <v-flex lg6 sm12 px-3 my-2>
                <div class="input-group date">
                    <label class="label col-12">Ngày kết thúc</label>
                    <datetime class="col-12" input-class="input" v-model="end_date">
                    </datetime>
                </div>
            </v-flex>
            <v-flex sm12 px-3 my-2>
                <hr class="w-100">
            </v-flex>
        </v-layout>

        <v-layout row wrap v-for="(schedule, index) in schedules" :key="index">
            <v-flex sm12 px-3
                    text-center><h4>Lịch học buổi {{ index + 1 > 1 ? index + 1 + ' (nếu có)' : index + 1}}</h4></v-flex>
            <v-flex lg6 sm12 px-3 my-2>
                <div class="input-group date">
                    <label class="label col-12">Giờ bắt đầu</label>
                    <datetime type="time" class="col-12" input-class="input" v-model="schedule.start_session">
                    </datetime>
                </div>
            </v-flex>
            <v-flex lg6 sm12 px-3 my-2>
                <div class="input-group date">
                    <label class="label col-12">Giờ kết thúc</label>
                    <datetime type="time" class="col-12" input-class="input" v-model="schedule.end_session">
                    </datetime>
                </div>
            </v-flex>
            <v-flex sm12 px-3 my-2>
                <hr class="w-100">
            </v-flex>
        </v-layout>


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
                schedules: [
                    {
                        start_session: '',
                        end_session: ''
                    },
                    {
                        start_session: '',
                        end_session: ''
                    }
                ],
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
            }
        },
        mounted() {
            if (!this.$v.$invalid) {
                this.$emit("can-continue", {value: true});
            } else {
                this.$emit("can-continue", {value: false});
            }
        },
    }

</script>

<style>

</style>
