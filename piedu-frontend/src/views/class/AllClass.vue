<template>
    <div>
        <!--<section class="section section-allclass-cover section-shaped my-0">-->
        <!-- <search></search> -->
        <!--<div class="shape shape-style-1 shape-primary alpha-4">-->
        <!--<span></span>-->
        <!--<span></span>-->
        <!--<span></span>-->
        <!--<span></span>-->
        <!--<span></span>-->
        <!--<span></span>-->
        <!--<span></span>-->
        <!--</div>-->
        <!--</section>-->
        <!--<section>-->
        <!--<div class="container">-->
        <!--<div class="row">-->
        <!--<div class="col-lg-3" id="allside">-->
        <!--<a href="javascript:void(0)" class="closebtn" @click="closeSidebar">&times;</a>-->
        <!--<sidebar></sidebar>-->
        <!--</div>-->
        <!--<div class="col-lg-9 col-sm-12 p-0">-->
        <!--<div class="row mt-3 view-switch">-->
        <!--<div class="col-md-8 col-sm-12"></div>-->
        <!--<div class="col-md-4 col-sm-12">-->
        <!--<div class="onoffswitch pull-right">-->
        <!--<input type="checkbox" name="onoffswitch" class="onoffswitch-checkbox"-->
        <!--id="myonoffswitch"-->
        <!--checked>-->
        <!--<label class="onoffswitch-label" for="myonoffswitch"-->
        <!--@click="landscapeDisplay = !landscapeDisplay">-->
        <!--<span class="onoffswitch-inner"></span>-->
        <!--<span class="onoffswitch-switch"></span>-->
        <!--</label>-->
        <!--</div>-->
        <!--</div>-->
        <!--</div>-->

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
                <v-card flat ref="presentTab">
                    <div class="row mt-5 justify-center" v-if="presentClass.preloader">
                        <v-progress-circular :size="30" color="green" indeterminate class="mb-5"/>
                                                <!--<v-progress-linear :indeterminate="true"></v-progress-linear>-->

                    </div>
                    <section v-else>
                        <section v-if="presentClass.classList.length == 0">
                            <div class="w-100 my-3 mx-0 alert alert-warning"
                                 key="emptyFutureClass">
                                <strong>Danh sách trống. </strong>
                            </div>
                        </section>
                        <section v-else>
                            <transition-group name="classbox" class="row mt-3" v-if="presentClass.classDisplay">
                                <class-box-portrait v-for="class_obj in presentClass.classList"
                                                    :id="class_obj.id"
                                                    :avatar-path="class_obj.avatar_path"
                                                    :category="class_obj.subject"
                                                    :lecturer="class_obj.lecturer[0]"
                                                    :class-name="class_obj.name"
                                                    :student-count="class_obj.students"
                                                    :code="class_obj.code"
                                                    :short-description="getShortDescription(class_obj.description)"
                                                    :key="class_obj.code + ' 2'"></class-box-portrait>
                            </transition-group>
                            <v-layout row wrap>
                                <v-flex xs6></v-flex>
                                <v-flex xs6 class="text-xs-right">
                                    <v-pagination
                                            v-model="presentClass.pagination.page"
                                            :length="presentClass.pagination.pageTotal"
                                            @input="presentClassNext"
                                    ></v-pagination>
                                </v-flex>
                            </v-layout>
                        </section>
                    </section>
                </v-card>
            </v-tab-item>
            <v-tab-item>
                <v-card flat>
                    <div class="row mx-0 justify-center" v-if="futureClass.preloader">
                        <v-progress-circular :size="50" color="green" indeterminate class="mb-5"/>
                    </div>
                    <section v-else>
                        <section v-if="futureClass.classList.length == 0">
                            <div class="w-100 my-3 mx-0 alert alert-warning"
                                 key="emptyFutureClass">
                                <strong>Danh sách trống. </strong>
                            </div>
                        </section>
                        <section v-else>
                            <transition-group name="classbox" class="row mt-3" v-if="futureClass.classDisplay">
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
                            </transition-group>
                            <v-layout row wrap>
                                <v-flex xs6></v-flex>
                                <v-flex xs6 class="text-xs-right">
                                    <v-pagination
                                            v-model="futureClass.pagination.page"
                                            :length="futureClass.pagination.pageTotal"
                                            @input="futureClassNext"
                                    ></v-pagination>
                                </v-flex>
                            </v-layout>
                        </section>
                    </section>
                </v-card>
            </v-tab-item>
            <v-tab-item>
                <v-card flat>
                    <v-card flat>
                        <div class="row mt-3 justify-center" v-if="pastClass.preloader">
                            <v-progress-circular :size="50" color="green" indeterminate class="mb-5"/>
                        </div>
                        <section v-else>
                            <section v-if="pastClass.classList.length == 0">
                                <div class="w-100 my-3 mx-0 alert alert-warning"
                                     key="emptyFutureClass">
                                    <strong>Danh sách trống. </strong>
                                </div>
                            </section>
                            <section v-else>
                                <transition-group name="classbox" class="row mt-3" v-if="pastClass.classDisplay">
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
                                </transition-group>
                                <v-layout row wrap>
                                    <v-flex xs6></v-flex>
                                    <v-flex xs6 class="text-xs-right">
                                        <v-pagination
                                                v-model="pastClass.pagination.page"
                                                :length="pastClass.pagination.pageTotal"
                                                @input="pastClassNext"
                                        ></v-pagination>
                                    </v-flex>
                                </v-layout>
                            </section>
                        </section>
                    </v-card>
                </v-card>
            </v-tab-item>
        </v-tabs>


        <!--<div class="row mx-0 justify-center" v-if="presentClass.preloader">-->
        <!--<v-progress-circular :size="50" color="green" indeterminate class="mb-5"/>-->
        <!--</div>-->

        <!--<transition-group name="classbox" class="row mx-0" v-if="presentClass.classDisplay">-->
        <!--&lt;!&ndash;<class-box-landscape class="class-box" v-show="landscapeDisplay"&ndash;&gt;-->
        <!--&lt;!&ndash;v-for="class_obj in classList"&ndash;&gt;-->
        <!--&lt;!&ndash;:id="class_obj.id"&ndash;&gt;-->
        <!--&lt;!&ndash;:avatar-path="class_obj.avatar_path"&ndash;&gt;-->
        <!--&lt;!&ndash;:category="class_obj.subject"&ndash;&gt;-->
        <!--&lt;!&ndash;lecturer="Hoàng Xuân Tùng"&ndash;&gt;-->
        <!--&lt;!&ndash;:class-name="class_obj.name"&ndash;&gt;-->
        <!--&lt;!&ndash;:student-count="class_obj.students"&ndash;&gt;-->
        <!--&lt;!&ndash;:code="class_obj.code"&ndash;&gt;-->
        <!--&lt;!&ndash;:short-description="getShortDescription(class_obj.description)"&ndash;&gt;-->
        <!--&lt;!&ndash;:key="class_obj.code + ' 1'"></class-box-landscape>&ndash;&gt;-->
        <!--<class-box-portrait v-for="class_obj in presentClass.classList"-->
        <!--:id="class_obj.id"-->
        <!--:avatar-path="class_obj.avatar_path"-->
        <!--:category="class_obj.subject"-->
        <!--lecturer=""-->
        <!--:class-name="class_obj.name"-->
        <!--:student-count="class_obj.students"-->
        <!--:code="class_obj.code"-->
        <!--:short-description="getShortDescription(class_obj.description)"-->
        <!--:key="class_obj.code + ' 2'"></class-box-portrait>-->
        <!--</transition-group>-->
        <!--<v-layout row wrap>-->
        <!--<v-flex xs6></v-flex>-->
        <!--<v-flex xs6 class="text-xs-right">-->
        <!--<v-pagination-->
        <!--v-model="presentClass.pagination.page"-->
        <!--:length="presentClass.pagination.pageTotal"-->
        <!--@input="presentClassNext"-->
        <!--&gt;</v-pagination>-->
        <!--</v-flex>-->
        <!--</v-layout>-->
        <!--</div>-->
        <!--</div>-->
        <!--</div>-->
        <!--</section>-->
        <!--<div @click="openSidebar" id="all-open-menu">-->
        <!--Open-->
        <!--</div>-->
    </div>
</template>
<script>
    import ClassBoxPortrait from '@/components/class/ClassBoxPortrait.vue';
    import BACKEND_URL from "@/backendServer";
    import Search from "@/components/class/Search"
    import Sidebar from "@/components/class/Aside"


    export default {
        name: "AllClass",
        data() {
            return {
                presentClass: {
                    classList: [],
                    preloader: true,
                    classDisplay: false,
                    landscapeDisplay: true,
                    pagination: {
                        itemTotal: 0,
                        page: 1,
                        pageTotal: 0,
                        itemPerPage: 12
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
                        itemPerPage: 12
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
                        itemPerPage: 12
                    }
                }
            }
        },
        components: {
            'class-box-portrait': ClassBoxPortrait,
            'search': Search,
            'sidebar': Sidebar,
        },
        beforeCreate: function () {
            let self = this;
            let token = self.$ls.get('token');
            let config = {
                headers: {
                    "Authorization": "Token " + token.toString()
                }
            };
            let presentData = {
                'token': token,
                'format': 'json',
                'time': 'present'
            };
            this.axios.post(BACKEND_URL + '/api/class/all/', presentData, config).then((response) => {
                this.presentClass.pagination.itemTotal = response.data.length;
                this.presentClass.pagination.pageTotal = Math.round(this.presentClass.pagination.itemTotal / this.presentClass.pagination.itemPerPage);
                console.log(this.presentClass.pagination.itemTotal);
            }).catch((response) => {
                console.log(response);
            });

            let futureData = {
                'token': token,
                'format': 'json',
                'time': 'future'
            };
            this.axios.post(BACKEND_URL + '/api/class/all/', futureData, config).then((response) => {
                this.futureClass.pagination.itemTotal = response.data.length;
                this.futureClass.pagination.pageTotal = Math.round(this.futureClass.pagination.itemTotal / this.futureClass.pagination.itemPerPage);
                console.log(this.futureClass.pagination.itemTotal);
            }).catch((response) => {
                console.log(response);
            });

            let pastData = {
                'token': token,
                'format': 'json',
                'time': 'past'
            };
            this.axios.post(BACKEND_URL + '/api/class/all/', pastData, config).then((response) => {
                this.pastClass.pagination.itemTotal = response.data.length;
                this.pastClass.pagination.pageTotal = Math.round(this.pastClass.pagination.itemTotal /
                    this.pastClass.pagination.itemPerPage);
                console.log(this.pastClass.pagination.itemTotal);
            }).catch((response) => {
                console.log(response);
            })

        },
        mounted() {
            this.getShowPresentClass(1);
            this.getShowFutureClass(1);
            this.getShowPastClass(1);

        },
        methods: {
            getShortDescription: function (description) {
                if (description != null && description.length > 75) {
                    return description.substring(0, 74) + ' ...';
                }
                return description;
            },
            getShowPresentClass: function (page) {
                let self = this;
                let token = self.$ls.get('token');
                let config = {
                    headers: {
                        "Authorization": "Token " + token.toString()
                    }
                };
                let data = {
                    'token': self.$ls.get('token'),
                    'format': 'json',
                    'page': page,
                    'time': "present",
                };

                this.axios.post(BACKEND_URL + '/api/class/all/', data, config).then((response) => {
                    self.presentClass.classList = response.data;
                    self.presentClass.preloader = false;
                    self.presentClass.classDisplay = true;

                })
            },
            getShowFutureClass: function (page) {
                let self = this;
                let token = self.$ls.get('token');
                let config = {
                    headers: {
                        "Authorization": "Token " + token.toString()
                    }
                };
                let data = {
                    'token': self.$ls.get('token'),
                    'format': 'json',
                    'page': page,
                    'time': "future",
                };

                this.axios.post(BACKEND_URL + '/api/class/all/', data, config).then((response) => {
                    self.futureClass.classList = response.data;
                    self.futureClass.preloader = false;
                    self.futureClass.classDisplay = true;

                })
            },
            getShowPastClass: function (page) {
                let self = this;
                let token = self.$ls.get('token');
                let config = {
                    headers: {
                        "Authorization": "Token " + token.toString()
                    }
                };
                let data = {
                    'token': self.$ls.get('token'),
                    'format': 'json',
                    'page': page,
                    'time': "past",
                };

                this.axios.post(BACKEND_URL + '/api/class/all/', data, config).then((response) => {
                    self.pastClass.classList = response.data;
                    self.pastClass.preloader = false;
                    self.pastClass.classDisplay = true;

                })
            },
            presentClassNext: function (page) {
                this.getShowPresentClass(page);
                this.$nextTick(() => {
                    this.$refs.presentTab.scrollTop = 0;
                });
            },
            futureClassNext: function (page) {
                this.getShowFutureClass(page);
            },
            pastClassNext: function (page) {
                this.getShowPastClass(page);
            },
            openSidebar: function () {
                document.querySelector("#allside").style.width = "270px";
            },
            closeSidebar: function () {
                document.querySelector("#allside").style.width = "0";
            },

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
        .view-switch {
            display: none;
        }
        #allside {
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

    @media screen and (min-width: 992px) {
        #allside {
            .closebtn {
                display: none;
            }
        }
    ;
        #all-open-menu {
            display: none;
        }
    }

    .section-allclass-cover {
        height: 450px;
        background-size: cover;
        background-position: center center;
    }

    #allside {
        .closebtn {
            position: absolute;
            top: 0;
            right: 25px;
            font-size: 36px;
            margin-left: 50px;
        }
    }

    #all-open-menu {
        position: fixed;
        bottom: 70%;
        right: 0px;
        font-size: 15px;
        z-index: 1200;
    }
</style>
<style>
    .v-tabs__bar {
        -webkit-border-radius: 4px;
        -moz-border-radius: 4px;
        border-radius: 4px;
    }
</style>
