<template>
    <div class="col-lg-4 col-md-6 col-sm-12 mb-3 pr-0 pl-3">
        <div class="card border-0 card-lift--hover shadow h-100">
            <img class="card-img-top class-avatar-portrait" v-lazy="avatarUrl(avatarPath)"/>
            <div class="card-body py-3 px-3">
                <h6 class="text-primary text-uppercase">{{ className }}</h6>
                <p class="description mt-3">{{ lecturer }}</p>
                <div><span class="badge badge-primary badge-pill">{{ code }}</span><span
                        class="badge badge-primary badge-pill">{{ category }}</span></div>
                <router-link type="" class="btn mt-4 btn-success btn-sm" :to="{name:'inner-class', params:{id:id}}" >
                    Xem chi tiết
                </router-link>
            </div>
        </div>
    </div>
</template>

<script>
    import {VueClazyLoad} from 'vue-clazy-load'
    import BACKEND_URL from "@/backendServer"

    export default {
        props: ['id','avatarPath', 'category', 'lecturer', 'code', 'className', 'shortDescription', 'studentCount'],
        components: {
            'clazy-load': VueClazyLoad,
        },
        methods: {
            avatarUrl: function (path) {
                return BACKEND_URL + path;
            }
        }
    }
</script>

<style lang="scss">
    .course-text {
        min-height: 200px;
    }
    .class-avatar-portrait {
        height: 10rem;
    }
</style>
