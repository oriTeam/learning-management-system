<template>
    <div>
        <section class="section section-profile-cover section-shaped my-0">
            <div class="shape shape-style-1 shape-primary shape-skew alpha-4">
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
            </div>
        </section>
        <section class="section section-skew">
            <div class="container">
                <div class="card mt--300 p-4 inner-class-box">
                    <class-info></class-info>
                    <hr/>
                    <div class="row mx-0 mt-3">
                        <div class="course-menu-nav">
                            <tab-header></tab-header>
                            <tab-content></tab-content>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>
<script>
    import TabHeader from './TabHeader.vue'
    import TabContent from './TabContent.vue'
    import ClassInfo from './ClassInfo.vue'

    export default {
        name: "inner-class",
        data: function () {
            return {}
        },
        components: {
            'class-info': ClassInfo,
            'tab-header': TabHeader,
            'tab-content': TabContent,
        }
    }
</script>
<style>
    .inner-class-box{
        margin-top: -300px;
    }
</style>