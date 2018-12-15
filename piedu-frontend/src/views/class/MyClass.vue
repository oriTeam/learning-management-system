<template>
    <div>
        <div v-if="isAdmin()" class="row m-3 alert alert-info"
             key="emptyCurrentClass">
            <strong>Bạn là admin</strong>
        </div>
        <div v-else>
            <section>
                <v-tabs class="w-100 px-3 br-4"
                        centered
                        color="#5e72e4"
                        dark
                        icons-and-text
                        grow>
                    <v-tabs-slider color="yellow"></v-tabs-slider>

                    <v-tab>
                        Lớp học đang diễn ra
                        <v-icon>timeline</v-icon>
                    </v-tab>

                    <v-tab>
                        Lớp học sắp tới
                        <v-icon>chrome_reader_mode</v-icon>
                    </v-tab>

                    <v-tab>
                        Lớp học đã kết thúc
                        <v-icon>toc</v-icon>
                    </v-tab>

                    <v-tab-item>
                        <div class="row mt-3 justify-center" v-if="currentClass.preloader">
                            <v-progress-circular :size="50" color="green" indeterminate class="mb-5"/>
                        </div>
                        <transition-group name="classbox" v-if="currentClass.classDisplay">
                            <div v-if="currentClass.classList.length == 0" class="row mt-3 mx-0 alert alert-warning"
                                 key="emptyCurrentClass">
                                <strong>Danh sách trống. </strong>
                            </div>
                            <div v-else key="currentClass" class="row my-3">
                                <class-box-portrait v-for="class_obj in currentClass.classList"
                                                    :id="class_obj.id"
                                                    :avatar-path="class_obj.avatar_path"
                                                    :category="class_obj.subject"
                                                    :lecturer="class_obj.lecturer[0]"
                                                    :class-name="class_obj.name"
                                                    :student-count="class_obj.students"
                                                    :code="class_obj.code"
                                                    :short-description="getShortDescription(class_obj.description)"
                                                    :key="class_obj.code + ' 2'"></class-box-portrait>
                            </div>
                        </transition-group>
                        <v-layout row wrap>
                            <v-flex xs12 class="text-xs-center">
                                <v-pagination
                                        v-model="currentClass.pagination.page"
                                        :length="currentClass.pagination.pageTotal"
                                        @input="next"
                                        v-if="currentClass.classList.length >= 9"
                                ></v-pagination>
                            </v-flex>
                        </v-layout>
                    </v-tab-item>
                    <v-tab-item>
                        <div class="row mt-3 justify-center" v-if="futureClass.preloader">
                            <v-progress-circular :size="50" color="green" indeterminate class="mb-5"/>
                        </div>
                        <transition-group name="classbox" v-if="futureClass.classDisplay">
                            <div v-if="futureClass.classList.length == 0" class="row mt-3 mx-0 alert alert-warning"
                                 key="emptyFutureClass">
                                <strong>Danh sách trống. </strong>
                            </div>
                            <div v-else class="row mt-3 my-3" key="futureClass">
                                <class-box-portrait v-for="class_obj in futureClass.classList"
                                                    :id="class_obj.id"
                                                    :avatar-path="class_obj.avatar_path"
                                                    :category="class_obj.subject"
                                                    :lecturer="class_obj.lecturer[0]"
                                                    :class-name="class_obj.name"
                                                    :student-count="class_obj.students"
                                                    :code="class_obj.code"
                                                    :short-description="getShortDescription(class_obj.description)"
                                                    :key="class_obj.code + ' 2'"></class-box-portrait>
                            </div>
                        </transition-group>
                        <v-layout row wrap>
                            <v-flex xs12 class="text-xs-center">
                                <v-pagination
                                        v-model="futureClass.pagination.page"
                                        :length="futureClass.pagination.pageTotal"
                                        @input="next"
                                        v-if="futureClass.classList.length >= 9"
                                ></v-pagination>
                            </v-flex>
                        </v-layout>
                    </v-tab-item>
                    <v-tab-item>
                        <div class="row mt-3 justify-center" v-if="pastClass.preloader">
                            <v-progress-circular :size="50" color="green" indeterminate class="mb-5"/>
                        </div>
                        <transition-group name="classbox" v-if="pastClass.classDisplay">
                            <div v-if="pastClass.classList.length == 0" class="row mt-3 mx-0 alert alert-warning"
                                 key="emptyPastClass">
                                <strong>Danh sách trống. </strong>
                            </div>
                            <div v-else class="row mt-3 my-3" key="pastClass">
                                <class-box-portrait v-for="class_obj in pastClass.classList"
                                                    :id="class_obj.id"
                                                    :avatar-path="class_obj.avatar_path"
                                                    :category="class_obj.subject"
                                                    :lecturer="class_obj.lecturer[0]"
                                                    :class-name="class_obj.name"
                                                    :student-count="class_obj.students"
                                                    :code="class_obj.code"
                                                    :short-description="getShortDescription(class_obj.description)"
                                                    :key="class_obj.code + ' 2'"></class-box-portrait>
                            </div>
                        </transition-group>
                        <v-layout row wrap>
                            <v-flex xs12 class="text-xs-center">
                                <v-pagination
                                        v-model="pastClass.pagination.page"
                                        :length="pastClass.pagination.pageTotal"
                                        @input="next"
                                        v-if="currentClass.classList.length >= 9"
                                ></v-pagination>
                            </v-flex>
                        </v-layout>
                    </v-tab-item>
                </v-tabs>
            </section>
            <!--<hr>-->
            <!--<section>-->
            <!--<div class="row mr-0">-->
            <!--<div class="col-lg-10 col-md-8 col-sm-12">-->
            <!--<h2 class="section-title"><span>Các lớp học sắp tới</span></h2>-->
            <!--</div>-->
            <!--<div class="view-switch col-lg-2 col-md-4 col-sm-12">-->
            <!--<div class="onoffswitch pull-right">-->
            <!--<input type="checkbox" name="onoffswitch" class="onoffswitch-checkbox"-->
            <!--id="myonoffswitch"-->
            <!--checked>-->
            <!--<label class="onoffswitch-label" for="myonoffswitch"-->
            <!--@click="futureClass.landscapeDisplay = !futureClass.landscapeDisplay">-->
            <!--<span class="onoffswitch-inner"></span>-->
            <!--<span class="onoffswitch-switch"></span>-->
            <!--</label>-->
            <!--</div>-->
            <!--</div>-->
            <!--</div>-->

            <!--<div class="row mx-0 justify-center" v-if="futureClass.preloader">-->
            <!--<v-progress-circular :size="50" color="green" indeterminate class="mb-5"/>-->
            <!--</div>-->
            <!--<transition-group name="classbox" v-if="futureClass.classDisplay">-->
            <!--<div v-if="futureClass.classList.length == 0" class="row m-3 alert alert-warning"-->
            <!--key="emptyFutureClass">-->
            <!--<strong>Danh sách trống. </strong>-->
            <!--</div>-->
            <!--<div v-else class="row mx-0 my-3" key="futureClass">-->
            <!--<class-box-portrait v-for="class_obj in futureClass.classList"-->
            <!--:id="class_obj.id"-->
            <!--:avatar-path="class_obj.avatar_path"-->
            <!--:category="class_obj.subject"-->
            <!--lecturer="Hoàng Xuân Tùng"-->
            <!--:class-name="class_obj.name"-->
            <!--:student-count="class_obj.students"-->
            <!--:code="class_obj.code"-->
            <!--:short-description="getShortDescription(class_obj.description)"-->
            <!--:key="class_obj.code + ' 2'"></class-box-portrait>-->
            <!--</div>-->
            <!--</transition-group>-->
            <!--<v-layout row wrap>-->
            <!--<v-flex xs12 class="text-xs-center">-->
            <!--<v-pagination-->
            <!--v-model="futureClass.pagination.page"-->
            <!--:length="futureClass.pagination.pageTotal"-->
            <!--@input="next"-->
            <!--v-if="futureClass.classList.length >= 9"-->
            <!--&gt;</v-pagination>-->
            <!--</v-flex>-->
            <!--</v-layout>-->
            <!--</section>-->
            <!--<hr>-->
            <!--<section>-->
            <!--<div class="row mr-0">-->
            <!--<div class="col-lg-10 col-md-8 col-sm-12">-->
            <!--<h2 class="section-title"><span>Các lớp đã kết thúc</span></h2>-->
            <!--</div>-->

            <!--</div>-->

            <!--<div class="row mx-0 justify-center" v-if="pastClass.preloader">-->
            <!--<v-progress-circular :size="50" color="green" indeterminate class="mb-5"/>-->
            <!--</div>-->
            <!--<transition-group name="classbox" v-if="pastClass.classDisplay">-->
            <!--<div v-if="pastClass.classList.length == 0" class="row m-3 alert alert-warning"-->
            <!--key="emptyPastClass">-->
            <!--<strong>Danh sách trống. </strong>-->
            <!--</div>-->
            <!--<div v-else class="row mx-0 my-3" key="pastClass">-->
            <!--<class-box-portrait v-for="class_obj in pastClass.classList"-->
            <!--:id="class_obj.id"-->
            <!--:avatar-path="class_obj.avatar_path"-->
            <!--:category="class_obj.subject"-->
            <!--lecturer="Hoàng Xuân Tùng"-->
            <!--:class-name="class_obj.name"-->
            <!--:student-count="class_obj.students"-->
            <!--:code="class_obj.code"-->
            <!--:short-description="getShortDescription(class_obj.description)"-->
            <!--:key="class_obj.code + ' 2'"></class-box-portrait>-->
            <!--</div>-->
            <!--</transition-group>-->
            <!--<v-layout row wrap>-->
            <!--<v-flex xs12 class="text-xs-center">-->
            <!--<v-pagination-->
            <!--v-model="pastClass.pagination.page"-->
            <!--:length="pastClass.pagination.pageTotal"-->
            <!--@input="next"-->
            <!--v-if="currentClass.classList.length >= 9"-->
            <!--&gt;</v-pagination>-->
            <!--</v-flex>-->
            <!--</v-layout>-->
            <!--</section>-->
        </div>
    </div>
</template>
<script>
    import ClassBoxPortrait from '@/components/class/ClassBoxPortrait.vue'
    import BACKEND_URL from "@/backendServer";
    import Search from "@/components/class/Search";
    import Sidebar from "@/components/class/Aside";


    export default {
        name: "MyClass",
        data() {
            return {
                currentClass: {
                    classList: [],
                    preloader: true,
                    classDisplay: false,
                    landscapeDisplay: true,
                    pagination: {
                        itemTotal: 0,
                        page: 1,
                        pageTotal: 0,
                        itemPerPage: 6
                    }
                },
                pastClass: {
                    classList: [],
                    preloader: true,
                    classDisplay: false,
                    landscapeDisplay: true,
                    pagination: {
                        itemTotal: 0,
                        page: 1,
                        pageTotal: 0,
                        itemPerPage: 6
                    }
                },
                futureClass: {
                    classList: [],
                    preloader: true,
                    classDisplay: false,
                    landscapeDisplay: true,
                    pagination: {
                        itemTotal: 0,
                        page: 1,
                        pageTotal: 0,
                        itemPerPage: 6
                    }
                },
            }
        },
        components: {
            'class-box-portrait': ClassBoxPortrait,
            'search': Search,
            'sidebar': Sidebar,
        },
        created: function () {
            let self = this;
            let token = self.$ls.get('token');
            let config = {
                headers: {
                    "Authorization": "Token " + token.toString()
                }
            };
            let data = {
                'token': token,
                'format': 'json',
            };
            this.axios.post(BACKEND_URL + '/api/class/all/', data, config).then((response) => {
                this.currentClass.pagination.itemTotal = response.data.length;
                this.currentClass.pagination.pageTotal = Math.round(this.currentClass.pagination.itemTotal /
                    this.currentClass.pagination.itemPerPage);
            }).catch((response) => {
                console.log(response);
            });
        },
        mounted() {
            this.getShowClass(1);
        },
        methods: {
            getShortDescription: function (description) {
                if (description != null && description.length > 75) {
                    return description.substring(0, 74) + ' ...';
                }
                return description;
            },
            getShowClass: function (page) {
                let self = this;
                let token = self.$ls.get('token');
                let config = {
                    headers: {
                        "Authorization": "Token " + token.toString()
                    }
                };
                let data = {
                    'format': "json",
                    'token': token
                }
                this.axios.post(BACKEND_URL + `/api/user/get_current_class`, data, config).then((res) => {
                    if (res.data.empty == true) {
                        self.currentClass.preloader = false;
                        self.currentClass.classDisplay = true;
                    }
                    else {
                        self.currentClass.classList = res.data;
                        self.currentClass.preloader = false;
                        self.currentClass.classDisplay = true;
                        self.currentClass.pagination.itemTotal = res.data.length;
                        self.currentClass.pagination.pageTotal = Math.round(self.currentClass.pagination.itemTotal / self.currentClass.pagination.itemPerPage);
                    }
                });
                this.axios.post(BACKEND_URL + `/api/user/get_future_class`, data, config).then((res) => {
                    if (res.data.empty == true) {
                        self.futureClass.preloader = false;
                        self.futureClass.classDisplay = true;
                    }
                    else {
                        self.futureClass.classList = res.data;
                        self.futureClass.preloader = false;
                        self.futureClass.classDisplay = true;
                        self.futureClass.pagination.itemTotal = res.data.length;
                        self.futureClass.pagination.pageTotal = Math.round(self.futureClass.pagination.itemTotal /
                            self.futureClass.pagination.itemPerPage);
                    }
                });
                this.axios.post(BACKEND_URL + `/api/user/get_past_class`, data, config).then((res) => {
                    if (res.data.empty == true) {
                        self.pastClass.preloader = false;
                        self.pastClass.classDisplay = true;
                    }
                    else {
                        self.pastClass.classList = res.data;
                        self.pastClass.preloader = false;
                        self.pastClass.classDisplay = true;
                        self.pastClass.pagination.itemTotal = res.data.length;
                        self.pastClass.pagination.pageTotal = Math.round(self.pastClass.pagination.itemTotal /
                            self.pastClass.pagination.itemPerPage);
                    }
                });

            },
            next: function (page) {
                this.getShowClass(page);
            },
            openSidebar: function () {
                document.querySelector("#myside").style.width = "270px";
            },
            closeSidebar: function () {
                document.querySelector("#myside").style.width = "0";
            },
            isAdmin: function () {
                return this.$ls.get("group") == "admin_group";
            }

        }
    }
</script>
<style lang="scss">

    /*.classbox-enter-active, .classbox-leave-active {*/
    /*transition: opacity .05s;*/
    /*}*/

    /*.classbox-enter, .classbox-leave-to {*/
    /*opacity: 0;*/
    /*}*/

    /* base */
    .class-box {
        backface-visibility: hidden;
        z-index: 1;
    }

    /* moving */
    .classbox-move {
        transition: all 200ms ease-in-out 50ms;
    }

    /* appearing */
    .classbox-enter-active {
        transition: all 100ms ease-out;
    }

    /* disappearing */
    .classbox-leave-active {
        transition: all 50ms ease-in;
        position: absolute;
        z-index: 0;
    }

    /* appear at / disappear to */
    .classbox-enter,
    .classbox-leave-to {
        opacity: 0;
    }

    .theme--light.v-pagination .v-pagination__item--active {
        color: #fff;
        background-color: #36a3f7;
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

    @media (max-width: 992px) {
        #myside {
            /*display: none;*/
            height: 100%; /* 100% Full-height */
            width: 0; /* 0 width - change this with JavaScript */
            position: fixed; /* Stay in place */
            z-index: 1200; /* Stay on top */
            top: 0; /* Stay at the top */
            left: 0;
            padding: 0;
            background-color: #fff; /* Black*/
            overflow-x: hidden; /* Disable horizontal scroll */
            padding-top: 60px; /* Place content 60px from the top */
            transition: 0.5s; /* 0.5 second transition effect to slide in the sidenav */
        }
    ;

    }

    @media (min-width: 992px) {
        #myside {
            .closebtn {
                display: none;
            }
        }
    ;
        inner-menu {
            display: none !important;
        }
    }

    .section-myclass-cover {
        height: 450px;
        background-size: cover;
        background-position: center center;
    }

    #myside {
        .closebtn {
            position: absolute;
            top: 0;
            right: 25px;
            font-size: 36px;
            margin-left: 50px;
        }
    }

    @media (max-width: 768px) {
        .view-switch {
            display: none !important;
        }
    }

    h2.section-title {
        position: relative;
        z-index: 1;
        padding-left: 50px;

        &:after {
            border-top: 2px solid #dfdfdf;
            content: "";
            margin: 0 auto; /* this centers the line to the full width specified */
            position: absolute; /* positioning must be absolute here, and relative positioning must be applied to the parent */
            top: 50%;
            left: 0;
            right: 0;
            bottom: 0;
            width: 95%;
            z-index: -1;
        }

        span {
            /* to hide the lines from behind the text, you have to set the background color the same as the container */
            background: #fff;
            padding: 0 15px;
        }
    }

</style>
