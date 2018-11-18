<template>
    <div class="m-portlet w-100">
        <new-class-stepper :steps="newClassSteps" @completed-step="completeStep"
                            @active-step="isStepActive" @stepper-finished="alert">
        </new-class-stepper>
    </div>
</template>
<style>

</style>
<script>
    import HorizontalStepper from 'vue-stepper';
    import StepOne from './StepOne.vue'
    import StepTwo from './StepTwo.vue'
    import Review from './Review.vue'

    export default {
        data(){
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
                ]
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
                        if(step.completed === true) {
                            step.completed = false;
                        }
                    }
                })
            },
            // Executed when @stepper-finished event is triggered
            alert(payload) {
                alert('end')
            }
        },
        components: {
            'new-class-stepper': HorizontalStepper,
            'step-one': StepOne,
            'step-two': StepTwo,
            'review': Review,
        }
    }
</script>
