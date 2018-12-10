<template>
    <div class="m-portlet w-100">
        <new-class-stepper locale="vi" @basic="basicData" @time="timeData" :steps="newClassSteps"
                           @completed-step="completeStep"
                           @active-step="isStepActive" @stepper-finished="submit">
        </new-class-stepper>
    </div>
</template>
<style>

</style>
<script>
    import BACKEND_URL from "@/backendServer";
    import HorizontalStepper from '@/components/class/HorizontalStepper.vue';
    import StepOne from '@/components/class/StepOne.vue';
    import StepTwo from '@/components/class/StepTwo.vue';
    import Review from '@/components/class/Review.vue';

    export default {
        data() {
            return {
                newClassSteps: [
                    {
                        icon: 'info',
                        name: 'basic',
                        title: 'Thông tin cơ bản',
                        subtitle: '',
                        component: StepOne,
                        completed: false

                    },
                    {
                        icon: 'alarm',
                        name: 'time',
                        title: 'Thời gian',
                        subtitle: '',
                        component: StepTwo,
                        completed: false
                    },
                    {
                        icon: 'rate_review',
                        name: 'review',
                        title: 'Xác nhận tạo mới lớp học',
                        subtitle: '',
                        component: Review,
                        completed: false
                    }
                ],
                basic: {},
                time: {}
            }
        },
        methods: {
            // Executed when @completed-step event is triggered
            completeStep(payload) {
                this.newClassSteps.forEach((step) => {
                    if (step.name === payload.name) {
                        step.completed = true;
                    }
                })
            },
            // Executed when @active-step event is triggered
            isStepActive(payload) {
                this.newClassSteps.forEach((step) => {
                    if (step.name === payload.name) {
                        if (step.completed === true) {
                            step.completed = false;
                        }
                    }
                })
            },
            // Executed when @stepper-finished event is triggered
            submit(payload) {
                alert('end');
                let self = this;
                let token = self.$ls.get('token');
                let config = {
                    headers: {
                        "Authorization": "Token " + token.toString()
                    }
                };
                let data = {
                    "subject": this.form.selected_subject,
                    "description": this.form.description,
                    "time_start" : this.form.start_date,
                    "time_end" : this.form.end_date,
                    "session_start" : this.form.main_schedule.start_session,
                    "session_end" : this.form.main_schedule.end_session,
                    "day_of_week" : this.form.main_schedule.day_of_week,
                    'format': "json",
                    'token': token
                };
                console.log(data);
                this.axios.post(BACKEND_URL + '/api/class/validated', data, config).then((res) => {
                    console.log(res.data);
                })

            },
            basicData: function (e) {
                this.basic = e;
            },
            timeData: function (e) {
                this.time = e;
            },

        },
        components: {
            'new-class-stepper': HorizontalStepper,
            'step-one': StepOne,
            'step-two': StepTwo,
            'review': Review,
        }
    }
</script>
