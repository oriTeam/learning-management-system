<template>
    <div class="card border-0 shadow h-100">
        <div class="card-body py-5"><div class="icon icon-shape mb-4 icon-shape-primary rounded-circle"><i class="ni ni-check-bold"></i></div><h6 class="text-primary text-uppercase">Download Argon</h6><p class="description mt-3">Argon is a great free UI package based on Bootstrap 4
                                    that includes the most important components and features.</p><div><span class="badge badge-primary badge-pill">design</span><span class="badge badge-primary badge-pill">system</span><span class="badge badge-primary badge-pill">creative</span></div><a type="" class="btn mt-4 btn-primary" href="#"><!----><!----><!---->
                                    Learn more
                                </a></div>
    </div>

    <!--<v-navigation-drawer permanent class="card border-0 card-lift&#45;&#45;hover shadow">-->
        <!--<v-toolbar flat>-->
            <!--<v-list>-->
                <!--<v-list-tile>-->
                    <!--<v-list-tile-title class="title">-->
                        <!--Application-->
                    <!--</v-list-tile-title>-->
                <!--</v-list-tile>-->
            <!--</v-list>-->
        <!--</v-toolbar>-->

        <!--<v-divider></v-divider>-->

        <!--<v-list dense class="pt-0">-->
            <!--<v-list-tile-->
                    <!--v-for="item in items"-->
                    <!--:key="item.title"-->
                    <!--@click=""-->
            <!--&gt;-->
                <!--<v-list-tile-action>-->
                    <!--<v-icon>{{ item.icon }}</v-icon>-->
                <!--</v-list-tile-action>-->

                <!--<v-list-tile-content>-->
                    <!--<router-link :to="item.to">{{ item.title }}</router-link>-->
                <!--</v-list-tile-content>-->
            <!--</v-list-tile>-->
        <!--</v-list>-->
    <!--</v-navigation-drawer>-->
</template>
<script>
    export default {
        data() {
            return {
                items: [
                    {title: 'Home', icon: 'dashboard', to: '/class/all'},
                    {title: 'About', icon: 'question_answer', to: '/class/my'}
                ],
                right: null
            }
        }
    }
</script>
<style>
    aside {
        /*box-shadow: 0 15px 8px rgba(50, 50, 93, 0.1), 0 5px 15px rgba(0, 0, 0, 0.07) !important;*/
    }
</style>