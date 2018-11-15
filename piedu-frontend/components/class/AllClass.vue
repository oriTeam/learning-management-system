<template>
    <div class="col-12 p-0">
        <div class="row mx-0" v-show="preloader">
            <div class="m-loader m-loader--success"
                 style="width: 30px; display: inline-block;"></div>
        </div>
        <div class="row mx-0" v-if="classDisplay">
            <class-box v-for="class_obj in classList" :avatar-path="class_obj.avatar_path" :category="class_obj.subject"
                       lecturer="Hoàng Xuân Tùng"
                       :class-name="class_obj.name"
                       :student-count="class_obj.students"
                       :code="class_obj.code"
                       :short-description="getShortDescription(class_obj.description)"
                       :key="class_obj.code"></class-box>
        </div>
    </div>
</template>
<script>
    import ClassBox from './ClassBox.vue'
    export default {
        data() {
            return {
                classList: [],
                preloader: true,
                classDisplay: false
            }
        },
        components: {
            'class-box': ClassBox
        },
        beforeCreate: function() {
            this.axios.get('/api/class/all', null).then((response) => {
                alert('done');
                this.classList = response.data;
                this.preloader = false;
                this.classDisplay = true;
            }).catch((response) => {
                console.log(response);
            })
        },
        methods: {
            getShortDescription: function (description) {
                if (description != null && description.length > 75) {
                    return description.substring(0, 74) + ' ...';
                }
                return description;
            },
        }
    }
</script>
