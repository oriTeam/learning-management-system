 <template>
  <div class="container-fluid">
    <section id="contact" class="contact-us m--margin-bottom-90 mt-5">
      <div class="contact-us-wrap">
        <div class="container-fluid">
          <div class="row">
            <div class="col-md-5">
              <div class="section-heading">
                <h3>Liên hệ với chúng tôi</h3>
                <p>PIEdu rất luôn sẵn sàng lắng nghe phản hồi từ bạn. Mọi ý kiến của các bạn đều
                  giúp chúng tôi hoàn thiện hơn hệ thống của mình</p>
              </div>
              <div class="footer-address">
                <h6>Văn phòng chính</h6>
                <ul>
                  <li><i class="fa fa-map-marker"></i> &nbsp; Phòng đào tạo: 104 - E3 - ĐHCN -
                    ĐHQGHN:
                  </li>
                  <li><i class="fa fa-phone"></i> &nbsp;<span>Phone: +1245643</span></li>
                  <li><i class="fa fa-envelope"></i> &nbsp;<span>Email : <a
                    href="mailto:piedu@gmail.com">piedu@gmail.com</a></span>
                  </li>
                </ul>
              </div>
            </div>
            <div class="col-md-7">
              <button id ="test" class="btn btn-primary" v-on:click="test">TestApi</button>

              <form action="#" method="post" class="contact-us-form" novalidate="novalidate">
                <h6>Hoặc liên hệ ngay với chúng tôi:</h6>
                <form id="contact-form" class="m-login__form m-form" action="">
                <!--{% csrf_token %}-->
                  <div class="alert alert-danger d-none" role="alert" id="contact_errors"></div>
                  <div class="row">
                    <div class="col-lg-6 col-sm-12">
                      <div class="form-group">
                        <input type="text" class="form-control" id="name"
                              placeholder="Tên của bạn ..." required="required">
                      </div>
                    </div>
                    <div class="col-lg-6 col-sm-12">
                      <div class="form-group">
                        <input type="email" class="form-control" id="email"
                              placeholder="Địa chỉ Email ..." required="required">
                      </div>
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-lg-6 col-sm-12">
                      <div class="form-group">
                        <input type="number" name="phone" value="" class="form-control"
                              id="phone" placeholder="Số điện thoại ...">
                      </div>
                    </div>
                    <div class="col-lg-6 col-sm-12">
                      <div class="form-group">
                        <input type="text" name="company" value="" size="40"
                              class="form-control" id="company" placeholder="Đơn vị ...">
                      </div>
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-sm-12">
                      <div class="form-group">
                        <textarea name="message" id="message" class="form-control" rows="10"
                           cols="25" placeholder="Phản hồi của bạn ..."></textarea>
                      </div>
                    </div>
                  </div>
                </form>
                <div class="row">
                  <div class="col-sm-12 m--margin-top-20 text-center">
                    <button @click="submit_form" type="button" class="btn softo-solid-btn" id="btnContactUs">
                      Gửi
                    </button>
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
function login_success_redirect(response) {
  if (response.success == true) {
    window.location.href = "http://" + response.redirectTo.toString();
  } else {
    toastr.error("Bạn đã nhập sai. Vui lòng kiểm tra lại ...");
  }
}

export default {
  methods: {

    test :function(){
        
        this.axios.get("/api/class/validated?day_of_week=Hai" ,{
          time_start : "ts",
          time_end  : "te",
          session_start : "ss",
          session_end : "se",
          
        })
        .then(alert("OK!"))
        .catch(alert("Faild!"))
    },
    submit_form: function() {
      let csrftoken = getCookie("csrftoken");
      let formdata = new FormData(document.querySelector("#contact-form"));
      formdata.append("csrfmiddlewaretoken", csrftoken);
      let data = formdata_to_dict(formdata);
      // let config = {
      //     headers: {
      //         'X-CSRFToken': csrftoken,
      //     }
      // }
      // console.log(config);
      this.axios
        .get("/contact", data)
        .then(function(response) {
          if (response.data.success == true) {
            window.location.href =
              "http://" + response.data.redirectTo.toString();
          } else {
            toastr.error("Bạn đã nhập sai. Vui lòng kiểm tra lại ...");
          }
        })
        .catch(function(response) {
          console.log(response.data);
        });
    }
  }
};
</script>
  