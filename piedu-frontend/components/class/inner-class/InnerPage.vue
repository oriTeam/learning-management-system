<template>
    <div class="m-portlet p-4">
        <class-info></class-info>
        <hr/>
        <div class="row mx-0 mt-3">
            <div class="course-menu-nav">
                <tab-header></tab-header>
                <tab-content></tab-content>
            </div>
        </div>
    </div>
</template>
<script>
    import TabHeader from './TabHeader.vue'
    import TabContent from './TabContent.vue'
    import ClassInfo from './ClassInfo.vue'

    export default {
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
