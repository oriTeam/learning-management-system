<template>
    <div id="create-user">
  <v-app id="inspire">
    <v-form ref="form" v-model="valid" lazy-validation>
     
      <v-text-field
        v-model="firstname"
        :rules="nameRules"
        :counter="20"
        label="Firstname"
        required
      ></v-text-field>
      <v-text-field
        v-model="lastname"
        :rules="nameRules"
        :counter="20"
        label="Lastname"
        required
      ></v-text-field>
      <v-text-field
        v-model="phone_number"
        :rules="nameRules"
        :counter="15"
        label="Phonenumber"
      
      ></v-text-field>
      <v-text-field
        v-model="unit"
        
        
        label="Đơn vị"
      
      ></v-text-field>
      <select v-model="gender" class="w-100" >
                                    <option v-for="gender in genders" :value="gender.id"
                                            :key="gender.id">{{ gender.name }}
                                    </option>
                                </select>
       <v-text-field
        v-model="code"
        :rules="nameRules"
        :counter="15"
        label="Mã số"
        required
      ></v-text-field>
       <v-text-field
        v-model="username"
        :rules="nameRules"
        :counter="20"
        label="Username"
        required
      ></v-text-field>
      <v-text-field
        v-model="password"
        :type="'password'"
        :rules="nameRules"
        :counter="20"
        label="Password"
        required
      ></v-text-field>
      <v-text-field
        v-model="email"
        :rules="emailRules"
        label="E-mail"
        required
      ></v-text-field>
      
      <select v-model="group" class="w-100" >
                                    <option v-for="group in groups" :value="group.id"
                                            :key="group.id">{{ group.name }}
                                    </option>
                                </select>
     
                    <div class="input-group date">
                        <label class="label col-12 px-0">Ngày sinh</label>
                        <datetime class="col-12 px-0" input-class="input" v-model="date">
                        </datetime>
                    </div>
                
     <v-text-field
        v-model="address"
    
        label="Adrress"
        
      ></v-text-field> 
  
      <v-btn
        :disabled="!valid"
        @click="submit"
      >
        submit
      </v-btn>
      <v-btn @click="clear">clear</v-btn>
    </v-form>
  </v-app>
</div>
</template>
<script>
import VueSelect from "../../../node_modules/vue-select/src/components/Select";
import BACKEND_URL from "@/backendServer";
import {Datetime} from 'vue-datetime';
import 'vue-datetime/dist/vue-datetime.css'
import {Settings} from 'luxon';
Settings.defaultLocale = 'vi';

    
export default {
  data: () => ({
    valid: true,
    username: '',
    lastname :'',
    firstname :'',
    password :'',
    phone_number :'',
    address :'',
    email: '',
    select: null,
    group : "0",
    gender : "0",
    date :'',
    unit :'',
    code :'',
    nameRules: [
      v => !!v || 'Field is required',
      v => (v && v.length <= 20) || 'String must be less than 20 characters'
    ],
    
    emailRules: [
      v => !!v || 'E-mail is required',
      v => /.+@.+/.test(v) || 'E-mail must be valid'
    ],
    
    groups : [
                    {
                        id : "0",
                        name : "Chức danh"
                    },
                    
                    {
                        id : "5",
                        name : "Giảng viên"
                    },
                    {
                        id : "6",
                        name : "Sinh viên"
                    }
                    ],
                    genders : [
                    {
                        id : "0",
                        name : "Giới tính"
                    },
                    
                    {
                        id : "Male",
                        name : "Nam"
                    },
                    {
                        id : "Female",
                        name : "Nữ"
                    }
                    ],
    
  }),
    components: {
            "v-select": VueSelect,
            'datetime': Datetime,
            
        },
  methods: {
    submit :function() {
      if (this.$refs.form.validate()) {
        let self = this;
                let token = self.$ls.get('token');
                let config = {
                    headers: {
                        "Authorization": "Token " + token.toString()
                    }
                };
        let data= {
          "first_name" :this.firstname ,
          "last_name" :this.lastname ,
          "phone_number" :this.phone_number ,
          "gender" : this.gender,
          "username" :this.username ,
          "password" :this.password ,
          "email" :this.email ,
          "group" : this.group,
          "adrress" : this.address,
          "birthday": this.date,
          "unit" : this.unit,
          "code" : this.code,
          'format': "json",
          'token': token
        };
        console.log(data);
        this.axios.post(BACKEND_URL + '/api/user/create', data, config).then((res) => {
                    console.log(res.data);
                    alert("Done");
                })
      }
    },
    clear () {
      this.$refs.form.reset()
    }
  }
} 
</script>>