<template>

    <!-- <div id="app_search">
        <h1>Tìm kiếm lớp học,giảng viên, học sinh</h1>
        <v-select :options="options" label="name">
            <template slot="option" slot-scope="option">
                {{ option.name }}
            </template>
          </v-select> -->
    <form action="" class="row justify-content-center class-search">
        <div class="col-lg-7 col-sm-12">
            <div class="form-group row justify-content-center">
                <div class="col-lg-10 col-sm-12" id="app_search">
                    <!--<div id="app_search"> -->
                    <!--<h1>Tìm kiếm lớp học,giảng viên, học sinh</h1>-->
                    <v-select :options="options" label="name">
                        <template slot="option" slot-scope="option">
                            {{ option.name }}
                        </template>
                    </v-select>
                    <!-- </div> -->
                </div>
                <!--<div class="col-lg-2 col-sm-10 px-3 text-center mt-lg-0 mt-sm-3">-->
                <!--<base-button type="white">Tìm kiếm</base-button>-->
                <!--</div>-->
            </div>
        </div>
    </form>
    <!-- </div>     -->
</template>

<style lang="scss">

    h1, .muted {
        color: azure;
    }

    h1 {
        font-size: 26px;
        font-weight: 600;
        text-rendering: optimizelegibility;
        -moz-osx-font-smoothing: grayscale;
        -moz-text-size-adjust: none;
    }

    .v-select {
        width: 100% !important;
    }

    /*!*#app_search {*!*/
    /*!*max-width: 50em;*!*/
    /*!*margin: auto;*!*/
    /*}*/

    #app_search {
        .dropdown {
            li {
                border-bottom: 1px solid rgba(112, 128, 144, 0.1);
                a {
                    padding: 10px 20px;
                    display: flex;
                    width: 100%;
                    align-items: center;
                    font-size: 0.875rem;
                    .fa {
                        padding-right: 0.5em;
                    }
                }
            }
            li:last-child {
                border-bottom: none;
            }
        }
        .dropdown-toggle {
            background-color: #fff;
            input {
                padding: 0 20px;
            }
        }
    }

    /*
    #app_search .dropdown li:last-child {
      border-bottom: none;
    }
    */

    /*#app_search .dropdown li a {*/
    /*padding: 10px 20px;*/
    /*display: flex;*/
    /*width: 100%;*/
    /*align-items: center;*/
    /*font-size: 0.875rem;*/
    /*}*/

    #app_search .dropdown li a .fa {
        padding-right: 0.5em;
    }

</style>
<style lang="scss">
    .class-search {
        padding-top: 150px;
    }

    @media (max-width: 992px) {
        .class-search {
            padding-left: 10%;
            padding-right: 10%;
            button {
                margin-top: 10px
            }
        }
    }
</style>

<script>
    import VueSelect from "../../../node_modules/vue-select/src/components/Select";
    import BACKEND_URL from "@/backendServer";

    export default {
        name: "search",
        data() {
            return {options: []}
        },
        components: {
            "v-select": VueSelect,
        },
        created() {
            this.getData()
        },
        methods: {
            getData: function () {
                let sefl = this;
                this.axios.get(BACKEND_URL + '/api/get-data?format=json').then((response) => {
                    sefl.options = response.data;
                    // alert(response.data["data"])
                })
            }
        }

    }
</script>