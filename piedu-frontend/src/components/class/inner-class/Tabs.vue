<template>
    <v-tabs centered
            color="cyan"
            dark
            icons-and-text>
        <v-tabs-slider color="yellow"></v-tabs-slider>

        <v-tab href="#tab-1">
            Thời gian biểu
            <v-icon>phone</v-icon>
        </v-tab>

        <v-tab href="#tab-2">
            Danh sách học sinh
            <v-icon>favorite</v-icon>
        </v-tab>

        <v-tab href="#tab-3">
            Danh sách xin vào lớp
            <v-icon>account_box</v-icon>
        </v-tab>

        <v-tab-item
                v-for="i in 3"
                :id="'tab-' + i"
                :key="i">
            <v-card flat>
                <v-card-text>{{ text }}</v-card-text>
            </v-card>
        </v-tab-item>
    </v-tabs>
</template>
<script>
    export default {
        name: 'tabs',
        data() {
            return {
                text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'
            }
        },
        methods: {
            isStudent: function () {
                if(this.$ls.get('group')=='student_group') {
                    return true;
                }
                return false;
            },
            isLecturer: function () {
                if(this.$ls.get('group')=='lecturer_group') {
                    return true;
                }
                return false;
            }
        }
    }
</script>
