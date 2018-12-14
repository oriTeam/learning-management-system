<template>

  
    <form action="" class="row justify-content-center class-search">
        <div class="col-lg-7 col-sm-12">
            <div class="form-group row justify-content-center">
                <div class="col-lg-10 col-sm-12" id="app_search">
                   <!-- <button class = "btn btn-primary"> Choice</button> -->
                    <!-- <dropdown :options="arrayOfObjects" :selected="object" v-on:updateOption="test"></dropdown> -->
                    <select v-model="basic.selected_type" class="w-100" @change="getData">
                                    <option v-for="item in items" :value="item.id"
                                            :key="item.id">{{ item.name }}
                                    </option>
                                </select>
                    <!-- <v-select :options="options" label="name" v-model="basic.seleted" v-on:change="redirect">
                        <template slot="option" slot-scope="option" :value ="option.id">
                            {{ option.name }}
                        </template>
                    </v-select> -->
                    <select v-model="basic.selected" class="w-100" @change="redirect">
                                    <option v-for="option in options" :value="option.id"
                                            :key="option.id">{{ option.name }}
                                    </option>
                                </select>
                    
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
    .w-100{
        background-color: azure;
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
            return {
                options: [],
                basic : {
                    selected_type : "",
                    selected : "",
                },
                items : [
                    {
                        id : "user",
                        name : "Giang vien, sinh vien"
                    },
                    {
                        id : "class",
                        name : "Lop hoc"
                    }
                    ]
            }
        },
        components: {
            "v-select": VueSelect,
            
        },
        created() {
            // this.getData()
        },
        methods: {
            
            getData: function () {
                let self = this;
                // alert(sefl.basic.selected_type);
            
                this.axios.get(BACKEND_URL + `/api/get-data?selected_type=${self.basic.selected_type}&format=json`).then((response) => {
                    self.options = response.data;
                    // alert(response.data["data"])
                })
            },
            redirect :function(){
                let self = this;
                
                if (self.basic.selected_type == "class") {
                    self.$router.push(`/class/${self.basic.selected}`);
                }
                else {
                    self.$router.push(`/user/${self.basic.selected}`);
                }
            }
        }

    }
</script>