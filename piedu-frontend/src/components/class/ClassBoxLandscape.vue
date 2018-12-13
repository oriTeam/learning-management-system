<template>
    <div class="col-lg-12 p-1">
        <div class="card border-0 shadow p-3 my-2 mx-3">
            <div class="course-item-pic-text row">
                <div class="course-pic relative-position col-md-5 col-sm-12">
                    <img v-lazy="avatarUrl(avatarPath)" class="card-img"/>
                </div>
                <div class="course-item-text col-md-7 col-sm-12">
                    <div class="course-title m--padding-top-10-tablet-and-mobile headline m--padding-bottom-15 relative-position">
                        <h2 class="mt-0">
                            {{ className }}
                        </h2>
                        <div class="course-meta">
                            <span class="mr-0"><p class="font-weight-bold">{{ code }}</p></span>
                            <span class="course-author bold-font"><a
                                    href="#">{{ lecturer }}</a></span>
                            <span class="course-category bold-font"><a href="#">{{ category }}</a></span>
                        </div>
                        <p class="m--margin-bottom-10">{{ shortDescription }}</p>
                    </div>
                    <div class="row btn-row" >
                        <div class="col-6 course-viewer ul-li d-inline-block">
                            <ul>
                                <li><p class="m-0"><i class="fas fa-user"></i> Sĩ số: {{ studentCount }}</p></li>
                            </ul>
                        </div>
                        <div class="col-6">
                            <router-link :to="{name:'inner-class', params:{id:id}}"
                                         class="btn btn-sm btn-success pull-right h-100 px-3 pt-2">Xem
                                chi
                                tiết</router-link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import BACKEND_URL from "@/backendServer"

    export default {
        props: ['id', 'avatarPath', 'category', 'lecturer', 'code', 'className', 'shortDescription', 'studentCount'],
        methods: {
            avatarUrl: function (path) {
                return BACKEND_URL + path;
            }
        }
    }
</script>

<style lang="scss">
    .course-pic {
        border-radius: 4px;
        height: 200px;
        overflow: hidden;
        display: flex;
    }

    .relative-position {
        position: relative;
    }

    .course-pic img {
        -webkit-transition: .3s all ease-in-out;
        -o-transition: .3s all ease-in-out;
        transition: .3s all ease-in-out;
        width: 100%;
    }

    .course-meta {
        display: inline-block;
        width: 100%;
    }

    .course-meta .course-category a, .latest-events .course-meta .course-author {
        color: #17d0cf !important;
    }

    .course-meta span {
        float: left;
        font-size: 14px;
        margin-right: 24px;
        position: relative;
    }

    .bold-font {
        font-weight: 700;
    }

    .course-meta .course-author {
        color: #333333;
    }

    .ul-li ul {
        margin: 0;
        padding: 0;
    }

    .ul-li ul li {
        list-style: none;
        display: inline-block;
    }

    .course-title h3 {
        color: #333333;
        font-size: 22px;
        font-weight: 500;
        line-height: 30px;
        -webkit-transition: .3s all ease-in-out;
        -o-transition: .3s all ease-in-out;
        transition: .3s all ease-in-out;
    }

    .course-title h3 span {
        top: -6px;
        color: #fff;
        padding: 5px;
        font-size: 11px;
        border-radius: 3px;
        position: relative;
        background-color: #ff5c26;
    }

    .course-viewer li {
        color: #989898;
        font-size: 14px;
        padding: 5px 15px;
        border-radius: 3px;
        background-color: #f7f7f7;
    }

    .course-title h2 {
        font-size: 1.75rem;
    }

    .course-meta span {
        padding-right: 10px;
        border-right: 2px solid;
        margin-right: 10px !important;
        margin-bottom: 0;
    }

    .course-meta span p {
        margin-bottom: 0 !important;
    }

    .course-meta span:last-child {
        border-right: none !important;
    }
    @media (min-width: 767px) {
        .course-item-text {
            position: relative;
            .btn-row {
                position: absolute;
                bottom: 0;
                width: 100% !important;
            }
        }
    }

</style>
