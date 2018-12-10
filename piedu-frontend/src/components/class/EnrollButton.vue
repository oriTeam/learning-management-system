<template>
    <div>
        <button v-if="this.status==0" @click="enroll()" type="button" class="btn btn-icon btn-primary"><span
                class="btn-inner--icon"><i
            class="ni ni-bag-17"></i></span> <span class="btn-inner--text">Tham gia lớp học</span></button>
        <button v-else-if="this.status==2" type="button" class="btn btn-icon btn-light disabled">Đang chờ xác nhận
            ...</button>
    </div>
</template>
<script>
    import BACKEND_URL from "@/backendServer";
    export default {
        name: 'enroll-btn',
        data() {
            return {
                status: Number,
                classId : this.class_id
            }
        },
        props : [
            'class_id'
        ],
        created() {
            this.check_status()
        },
        methods: {
           enroll : function () {
               let self = this;
               let token = self.$ls.get('token');
               let config = {
                   headers : {
                       "Authorization": "Token " +  token.toString()
                   }
               };
               let data = {
                   'own_class': self.classId,
                   'student': self.$ls.get('user'),
                   'token': self.$ls.get('token')
               };
               this.axios.post(BACKEND_URL + '/api/enroll_request/create', data, config).then((res) => {
                   console.log("enroll success");
               });
               this.check_status();
           },
           check_status: function () {
               let self = this;
               let token = self.$ls.get('token');
               let config = {
                   headers : {
                       "Authorization": "Token " +  token.toString()
                   }
               };
               let data = {
                   'own_class': self.classId,
                   'student': self.$ls.get('user'),
                   'token': self.$ls.get('token'),
                   'format': "json"
               };
               this.axios.get(BACKEND_URL + '/api/class/student_status', {params: data}, config).then((res) => {
                   self.status = res.data.code;
               })
           }
        }
    }
</script>