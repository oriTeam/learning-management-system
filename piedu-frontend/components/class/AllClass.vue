<template>
    <div class="col-12 p-0">
        <!--<button @click="landscapeDisplay = !landscapeDisplay" class="btn btn-outline-warning"></button>-->
        <div class="row mt-3">
            <div class="col-md-8 col-sm-12"></div>
            <div class="col-md-4 col-sm-12">
                <div class="onoffswitch m--pull-right">
                    <input type="checkbox" name="onoffswitch" class="onoffswitch-checkbox" id="myonoffswitch" checked>
                    <label class="onoffswitch-label" for="myonoffswitch" @click="landscapeDisplay = !landscapeDisplay">
                        <span class="onoffswitch-inner"></span>
                        <span class="onoffswitch-switch"></span>
                    </label>
                </div>
            </div>
        </div>

        <div class="row mx-0" v-show="preloader">
            <div class="m-loader m-loader--success"
                 style="width: 30px; display: inline-block;"></div>
        </div>
        <transition-group name="classbox" class="row mx-0" v-if="classDisplay">
            <class-box-landscape v-show="landscapeDisplay" v-for="class_obj in classList"
                                 :avatar-path="class_obj.avatar_path"
                                 :category="class_obj.subject"
                                 lecturer="Hoàng Xuân Tùng"
                                 :class-name="class_obj.name"
                                 :student-count="class_obj.students"
                                 :code="class_obj.code"
                                 :short-description="getShortDescription(class_obj.description)"
                                 :key="class_obj.code + ' 1'"></class-box-landscape>
            <class-box-portrait v-show="!landscapeDisplay" v-for="class_obj in classList"
                                :avatar-path="class_obj.avatar_path"
                                :category="class_obj.subject"
                                lecturer="Hoàng Xuân Tùng"
                                :class-name="class_obj.name"
                                :student-count="class_obj.students"
                                :code="class_obj.code"
                                :short-description="getShortDescription(class_obj.description)"
                                :key="class_obj.code + ' 2'"></class-box-portrait>
        </transition-group>
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
<style lang="scss">

    .classbox-enter-active, .classbox-leave-active {
        transition: opacity .5s;
    }

    .classbox-enter, .classbox-leave-to {
        opacity: 0;
    }

    .onoffswitch {
        position: relative;
        width: 113px;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
    }

    .onoffswitch-checkbox {
        display: none;
    }

    .onoffswitch-label {
        display: block;
        overflow: hidden;
        cursor: pointer;
        border: 2px solid #EAEBE4;
        border-radius: 4px;
    }

    .onoffswitch-inner {
        display: block;
        width: 200%;
        margin-left: -100%;
        transition: margin 0.3s ease-in 0s;
    }

    .onoffswitch-inner:before, .onoffswitch-inner:after {
        display: block;
        float: left;
        width: 50%;
        height: 34px;
        padding: 0;
        line-height: 34px;
        font-size: 16px;
        color: white;
        font-family: Muli, Arial, sans-serif;
        font-weight: bold;
        box-sizing: border-box;
    }

    .onoffswitch-inner:before {
        content: "Ngang";
        padding-left: 15px;
        background-color: #34A7C1;
        color: #FFFFFF;
    }

    .onoffswitch-inner:after {
        content: "Dọc";
        padding-right: 15px;
        background-color: #EEEEEE;
        color: #999999;
        text-align: right;
    }

    .onoffswitch-switch {
        display: block;
        width: 21px;
        margin: 9.5px;
        background: #FFFFFF;
        position: absolute;
        top: 0;
        bottom: 0;
        right: 75px;
        border: 2px solid #EAEBE4;
        border-radius: 4px;
        transition: all 0.3s ease-in 0s;
        height: 18px;
    }

    .onoffswitch-checkbox:checked + .onoffswitch-label .onoffswitch-inner {
        margin-left: 0;
    }

    .onoffswitch-checkbox:checked + .onoffswitch-label .onoffswitch-switch {
        right: 0px;
    }
</style>
