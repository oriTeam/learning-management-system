<template>
    <div style="padding: 2rem 3rem; text-align: left;">
        <v-layout row wrap>
            <v-flex lg6 sm12 px-3 my-sm-2>
                <div class="field">
                    <label class="label">Thể loại</label>
                    <div class="control">
                        <div :class="['select', 'w-100', ($v.form.selected_category.$error) ? 'is-danger' : '']">
                            <select v-model="form.selected_category" class="w-100">
                                <option value="1">Select dropdown</option>
                                <option value="2">With options</option>
                            </select>
                        </div>
                    </div>
                    <p v-if="$v.form.selected_category.$error" class="help is-danger">Loại môn học không hợp lệ</p>
                </div>
            </v-flex>
            <v-flex lg6 sm12 px-3 my-sm-2>
                <div class="field">
                    <label class="label">Môn học</label>
                    <div class="control">
                        <div :class="['select', 'w-100', ($v.form.selected_subject.$error) ? 'is-danger' : '']">
                            <select v-model="form.selected_subject" class="w-100">
                                <option>Select dropdown</option>
                                <option>With options</option>
                            </select>
                        </div>
                    </div>
                    <p v-if="$v.form.selected_subject.$error" class="help is-danger">Môn học không hợp lệ</p>
                </div>
            </v-flex>
        </v-layout>
        <v-layout row wrap>
            <v-flex lg7 sm12 px-3 my-2>
                <div class="field">
                    <label class="label">Tên lớp học</label>
                    <div class="control">
                        <input :class="['input', 'w-100', ($v.form.className.$error) ? 'is-danger' : '']" type="text"
                               placeholder="Tên lớp học"
                               v-model="form.className">
                    </div>
                    <p v-if="$v.form.className.$error" class="help is-danger">Không được để trống tên lớp học</p>
                </div>
            </v-flex>
            <v-flex lg5 sm12 px-3 my-2>
                <div class="field">
                    <label class="label">Mã lớp học</label>
                    <div class="control">
                        <input :class="['input', 'w-100', ($v.form.classCode.$error) ? 'is-danger' : '']" type="text"
                               placeholder="Mã lớp học" v-model="form.classCode">
                    </div>
                    <p v-if="$v.form.classCode.$error" class="help is-danger">Ma</p>
                </div>
            </v-flex>
        </v-layout>
        <div class="field">
            <label class="label">Message</label>
            <div class="control">
                <textarea :class="['textarea', ($v.form.message.$error) ? 'is-danger' : '']" placeholder="Textarea"
                          v-model="form.message"></textarea>
            </div>
        </div>
    </div>
</template>
<style>
</style>

<script>
    import {validationMixin} from "vuelidate";
    import {required} from "vuelidate/lib/validators";

    export default {
  props: ["clickedNext", "currentStep"],
  mixins: [validationMixin],
  data() {
    return {
      form: {
        categories: [],
        selected_category: "",
        subjects: ["Bạn phải chọn Loại lớp học trước"],
        selected_subject: "",
        className: "",
        classCode: "",
        description: ""
      }
    };
  },
  validations: {
    form: {
      selected_category: {
        required
      },
      selected_subject: {
        required
      },
      className: {
        required
      },
      classCode: {
        required
      },
      description: {
        required
      }
    }
  },
  watch: {
    $v: {
      handler: function(val) {
        if (!val.$invalid) {
          this.$emit("can-continue", { value: true });
        } else {
          this.$emit("can-continue", { value: false });
        }
      },
      deep: true
    },
    clickedNext(val) {
      if (val === true) {
        this.$v.form.$touch();
      }
    }
  },
  mounted() {
    if (!this.$v.$invalid) {
      this.$emit("can-continue", { value: true });
    } else {
      this.$emit("can-continue", { value: false });
    }
  },
  methods: {
    updateCategory: function(e) {
      if (e.target.options.selectedIndex > -1) {
        console.log(e);
      }
    },
    updateSuject: function(e) {
      if (e.target.options.selectedIndex > -1) {
        console.log(e);
      }
    }
  }
};
</script>
