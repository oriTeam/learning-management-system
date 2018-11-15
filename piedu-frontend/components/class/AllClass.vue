<template>
    <div class="col-12 p-0">
        <button @click="landscapeDisplay = !landscapeDisplay" class="btn btn-outline-warning"></button>
        <div class="row mx-0" v-show="preloader">
            <div class="m-loader m-loader--success"
                 style="width: 30px; display: inline-block;"></div>
        </div>
        <div class="row mx-0" v-if="classDisplay">
            <class-box-landscape v-show="landscapeDisplay" v-for="class_obj in classList"
                                 :avatar-path="class_obj.avatar_path"
                                 :category="class_obj.subject"
                                 lecturer="Hoàng Xuân Tùng"
                                 :class-name="class_obj.name"
                                 :student-count="class_obj.students"
                                 :code="class_obj.code"
                                 :short-description="getShortDescription(class_obj.description)"
                                 :key="class_obj.code"></class-box-landscape>

            <class-box-portrait v-show="!landscapeDisplay" v-for="class_obj in classList"
                                 :avatar-path="class_obj.avatar_path"
                                 :category="class_obj.subject"
                                 lecturer="Hoàng Xuân Tùng"
                                 :class-name="class_obj.name"
                                 :student-count="class_obj.students"
                                 :code="class_obj.code"
                                 :short-description="getShortDescription(class_obj.description)"
                                 :key="class_obj.code"></class-box-portrait>
        </div>
        <paginate
                :container-class="'pagination'"
                :page-count="20"
                :prev-text="'Prev'"
                :next-text="'Next'">
        </paginate>
    </div>
</template>
<script>
    import ClassBoxPortrait from './ClassBoxPortrait.vue'
    import ClassBoxLandscape from './ClassBoxLanscape.vue'
    import Paginate from 'vuejs-paginate'

    export default {
        data() {
            return {
                classList: [],
                preloader: true,
                classDisplay: false,
                landscapeDisplay: true
            }
        },
        components: {
            'class-box-portrait': ClassBoxPortrait,
            'class-box-landscape': ClassBoxLandscape,
            'paginate': Paginate
        },
        beforeCreate: function() {
            this.axios.get('/api/class/all').then((response) => {
                this.classList = response.data;
                this.preloader = false;
                this.classDisplay = true;
            }).catch((response) => {
                console.log(response);
            })
        },
        mounted() {
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
