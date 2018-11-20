<template>
    <div style="padding: 2rem 3rem; text-align: left;">
        <v-layout row wrap>
            <v-flex sm12 text-center px-3 my-2>
                <h2>Xem lại thông tin lớp học</h2>
            </v-flex>
        </v-layout>
        <v-layout row wrap mx-0>
            <v-flex sm12 my-2>
                <h4>Thời gian diễn ra</h4>
            </v-flex>
            <v-flex lg6 sm12 my-2>
                <p class="font-weight-medium">Ngày bắt đầu: {{ new Date(startDate).toLocaleDateString() }}</p>
            </v-flex>
            <v-flex lg6 sm12 my-2>
                <p class="font-weight-medium">Ngày kết thúc: {{ new Date(endDate).toLocaleDateString() }}</p>
            </v-flex>
        </v-layout>
        <hr>
        <v-layout row wrap mx-0>
            <v-flex sm12 my-2>
                <h4>Lịch học lý thuyết</h4>
            </v-flex>
            <v-flex lg4 sm12 my-2>
                <p class="font-weight-medium">Thứ: {{ mainDayOfWeek }}</p>
            </v-flex>
            <v-flex lg4 sm12 my-2>
                <p class="font-weight-medium">Giờ bắt đầu buổi học: {{ mainStartSession + 6 }}:00</p>
            </v-flex>
            <v-flex lg4 sm12 my-2>
                <p class="font-weight-medium">Giờ kết thúc buổi học: {{ mainEndSession + 6 }}:50</p>
            </v-flex>
        </v-layout>
        <hr>
        <v-layout v-show="subDayOfWeek!='' && subStartSession!='' && subEndSession!=''" row wrap mx-0>
            <v-flex sm12 my-2>
                <h4>Lịch học thực hành</h4>
            </v-flex>
            <v-flex lg4 sm12 my-2>
                <p class="font-weight-medium">Thứ: {{ subDayOfWeek }}</p>
            </v-flex>
            <v-flex lg4 sm12 my-2>
                <p class="font-weight-medium">Giờ bắt đầu buổi học: {{ subStartSession + 6 }}:00</p>
            </v-flex>
            <v-flex lg4 sm12 my-2>
                <p class="font-weight-medium">Giờ kết thúc buổi học: {{ subEndSession + 6 }}:50</p>
            </v-flex>
        </v-layout>
    </div>
</template>
<script>
    export default {
        data: function() {
            return {
                'day_of_week': this.subDayOfWeek,
                'start_session': this.subStartSession,
                'end_session': this.subEndSession
            }
        },
        props: ['startDate', 'endDate', 'mainDayOfWeek', 'mainStartSession', 'mainEndSession',
            'subDayOfWeek', 'subStartSession', 'subEndSession'],
        mounted() {
            this.$emit("can-continue", {value: true});
        },
        methods: {
            checkEmptySubSchedule: function () {
                // if(this.$props.sub_day_of_week != '' && )
                if(this.day_of_week != '' && this.start_session != '' && this.end_session != '') return true
                else return false
            },
        }
    }
</script>
<style>

</style>
