<template>
    <div class="m-portlet w-100">
        <horizontal-stepper :steps="demoSteps" @completed-step="completeStep"
                            @active-step="isStepActive" @stepper-finished="alert">
        </horizontal-stepper>
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
                demoSteps: [
                    {
                        icon: 'mail',
                        name: 'first',
                        title: 'Sample title 1',
                        subtitle: 'Subtitle sample',
                        component: StepOne,
                        completed: false

                    },
                    {
                        icon: 'report_problem',
                        name: 'second',
                        title: 'Sample title 2',
                        subtitle: 'Subtitle sample',
                        component: StepTwo,
                        completed: false
                    }
                ]
            }
        },
        methods: {
            // Executed when @completed-step event is triggered
            completeStep(payload) {
                this.demoSteps.forEach((step) => {
                    if (step.name === payload.name) {
                        step.completed = true;
                    }
                })
            },
            // Executed when @active-step event is triggered
            isStepActive(payload) {
                this.demoSteps.forEach((step) => {
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
            'horizontal-stepper': HorizontalStepper,
            'step-one': StepOne,
            'step-two': StepTwo,
            'review': Review,
        }
    }
</script>
