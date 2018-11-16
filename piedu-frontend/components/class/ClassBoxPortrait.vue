<template>
    <div class="col-lg-4 p-0">
        <div class="m-portlet m-portlet--bordered-semi m-portlet--full-height m-portlet--rounded-force p-3 mt-2 mx-1">
            <div class="course-item-pic-text row h-100">
                <div class="course-pic relative-position col-sm-12">
                    <img :src="avatarPath" alt="" class=".img-thumbnail">
                </div>
                <div class="course-item-text col-sm-12 course-text">
                    <div class="course-title m--padding-top-10 headline m--padding-bottom-15 relative-position">
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
                    <div class="row btn-row">
                        <div class="col-6 course-viewer ul-li d-inline-block">
                            <ul>
                                <li><p class="m-0"><i class="fas fa-user"></i> Sĩ số: {{ studentCount }}</p></li>
                                <!--<li><p><i class="fas fa-comment-dots"></i> 1.015</p></li>-->
                                <!--<li><p class="m-0">Tuần 8</p></li>-->
                            </ul>
                        </div>
                        <div class="col-6">
                            <button class="btn btn-sm btn-success m--pull-right">Xem chi tiết</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        props: ['avatarPath', 'category', 'lecturer', 'code', 'className', 'shortDescription', 'studentCount'],
    }
</script>

<style lang="scss">
    .course-text {
        min-height: 200px;
    }
</style>
