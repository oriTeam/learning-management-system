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
        <!--<div class="flex-column flex-md-row"><div class="nav-wrapper"><ul role="tablist" class="nav nav-pills nav-fill"><li class="nav-item"><a data-toggle="tab" role="tab" href="#undefined" class="nav-link active" aria-selected="true"><div><span><i class="ni ni-cloud-upload-96">-->
        <!--Home-->
        <!--</i></span></div></a></li><li class="nav-item"><a data-toggle="tab" role="tab" href="#Profile" class="nav-link"><div><span><i class="ni ni-bell-55 mr-2">-->
        <!--Profile-->
        <!--</i></span></div></a></li><li class="nav-item"><a data-toggle="tab" role="tab" href="#undefined" class="nav-link"><div><span><i class="ni ni-calendar-grid-58">-->
        <!--Messages-->
        <!--</i></span></div></a></li></ul></div> <div class="tab-content"><div class="card shadow">&lt;!&ndash;&ndash;&gt; <div class="card-body"><div class="tab-pane fade active show" aria-expanded="true" style=""> <p class="description">Raw denim you probably haven't heard of them jean shorts-->
        <!--Austin. Nesciunt tofu stumptown aliqua, retro synth master cleanse. Mustache-->
        <!--cliche tempor, williamsburg carles vegan helvetica. Reprehenderit butcher retro-->
        <!--keffiyeh dreamcatcher synth.</p></div> <div class="tab-pane fade" style="display: none;"> <p class="description">Cosby sweater eu banh mi, qui irure terry richardson ex-->
        <!--squid. Aliquip placeat salvia cillum iphone. Seitan aliquip quis cardigan-->
        <!--american apparel, butcher voluptate nisi qui.</p></div> <div class="tab-pane fade" style="display: none;"> <p class="description">Raw denim you probably haven't heard of them jean shorts-->
        <!--Austin. Nesciunt tofu stumptown aliqua, retro synth master cleanse. Mustache-->
        <!--cliche tempor, williamsburg carles vegan helvetica. Reprehenderit butcher retro-->
        <!--keffiyeh dreamcatcher synth.</p></div></div> &lt;!&ndash;&ndash;&gt; &lt;!&ndash;&ndash;&gt;</div></div></div>-->
        <!--<tabs>-->
        <!--<tab name="First tab">-->
        <!--First tab content-->
        <!--</tab>-->
        <!--<tab name="Second tab">-->
        <!--Second tab content-->
        <!--</tab>-->
        <!--<tab name="Third tab">-->
        <!--Third tab content-->
        <!--</tab>-->
        <!--</tabs>-->
        <div class="row mx-0">
            <ul role="tablist" class="nav nav-pills nav-fill">
                <li class="nav-item"><a data-toggle="tab" role="tab" href="#UI/UX Design" class="nav-link">
                    <div>UI/UX Design</div>
                </a></li>
                <li class="nav-item"><a data-toggle="tab" role="tab" href="#Programming" class="nav-link active"
                                        aria-selected="true">
                    <div>Programming</div>
                </a></li>
                <li class="nav-item"><a data-toggle="tab" role="tab" href="#Graphic" class="nav-link">
                    <div>Graphic</div>
                </a></li>
            </ul>
        </div>

        <div class="row mx-0 justify-center" v-if="preloader">
            <v-progress-circular :size="50" color="green" indeterminate class="mb-5"/>
        </div>

        <transition-group name="classbox" class="row mx-0" v-if="classDisplay">
            <!--<class-box-landscape class="class-box" v-show="landscapeDisplay"-->
            <!--v-for="class_obj in classList"-->
            <!--:id="class_obj.id"-->
            <!--:avatar-path="class_obj.avatar_path"-->
            <!--:category="class_obj.subject"-->
            <!--lecturer="Hoàng Xuân Tùng"-->
            <!--:class-name="class_obj.name"-->
            <!--:student-count="class_obj.students"-->
            <!--:code="class_obj.code"-->
            <!--:short-description="getShortDescription(class_obj.description)"-->
            <!--:key="class_obj.code + ' 1'"></class-box-landscape>-->
            <class-box-portrait v-for="class_obj in classList"
                                :id="class_obj.id"
                                :avatar-path="class_obj.avatar_path"
                                :category="class_obj.subject"
                                lecturer="Hoàng Xuân Tùng"
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
                        v-model="pagination.page"
                        :length="pagination.pageTotal"
                        @input="next"
                ></v-pagination>
            </v-flex>
        </v-layout>
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
    import ClassBoxLandscape from '@/components/class/ClassBoxLandscape.vue';
    import BACKEND_URL from "@/backendServer";
    import Search from "@/components/class/Search"
    import Sidebar from "@/components/class/AsideLecturer"


    export default {
        name: "AllClass",
        data() {
            return {
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
        },
        components: {
            'class-box-portrait': ClassBoxPortrait,
            'class-box-landscape': ClassBoxLandscape,
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
            let data = {
                'token': self.$ls.get('token'),
                'format': 'json',
            };
            this.axios.post(BACKEND_URL + '/api/class/all/', data, config).then((response) => {
                this.pagination.itemTotal = response.data.length;
                this.pagination.pageTotal = Math.round(this.pagination.itemTotal / this.pagination.itemPerPage);
                console.log(this.pagination.itemTotal);
            }).catch((response) => {
                console.log(response);
            })
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
                    'token': self.$ls.get('token'),
                    'format': 'json',
                    'page': page,
                };

                this.axios.post(BACKEND_URL + '/api/class/all/', data, config).then((response) => {
                    self.classList = response.data;
                    self.preloader = false;
                    self.classDisplay = true;

                })
            },
            next: function (page) {
                this.getShowClass(page);
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
