<template>
    <div class="col-lg-4 col-md-6 col-sm-12 pb-3 px-3">
        <router-link :to="{name:'inner-class', params:{id:id}}" class="card border-0 shadow h-100">
            <img class="card-img-top class-avatar-portrait" v-lazy="avatarUrl(avatarPath)"/>
            <div class="card-body py-3 px-3">
                <h6 class="text-primary text-uppercase">{{ className }}</h6>
                <p class="description mt-3">Giảng viên: {{ lecturer }}</p>
                <div><div class="badge badge-primary badge-pill">#{{ code }}</div></div>
                <div><div
                        class="badge badge-primary badge-pill">#{{ category }}</div></div>

                <!--<div class="col-6 course-viewer ul-li d-inline-block">-->
                            <!--<ul>-->
                                <!--<li><p class="m-0"><i class="fas fa-user"></i> Sĩ số: {{ studentCount }}</p></li>-->
                            <!--</ul>-->
                        <!--</div>-->
                <div class="btn mt-4 btn-success btn-sm">
                    <i class="fas fa-user"></i> Sĩ số: {{ studentCount }}
                </div>
            </div>
        </router-link>
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
