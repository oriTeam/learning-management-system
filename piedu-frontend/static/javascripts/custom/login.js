var SnippetLogin = function () {
    var e = $("#login-background"), i = function (e, i, a) {
        var l = $('<div class="m-alert m-alert--outline alert alert-' + i + ' alert-dismissible" role="alert">\t\t\t<button type="button" class="close" data-dismiss="alert" aria-label="Close"></button>\t\t\t<span></span>\t\t</div>');
        e.find(".alert").remove(), l.prependTo(e), mUtil.animateClass(l[0], "fadeIn animated"), l.find("span").html(a)
    }, a = function () {
        e.removeClass("m-login--forget-password"), e.removeClass("m-login--signup"), e.addClass("m-login--signin"), mUtil.animateClass(e.find(".m-login__signin")[0], "flipInX animated")
    }, l = function () {
        $("#m_login_forget_password").click(function (i) {
            i.preventDefault(), e.removeClass("m-login--signin"), e.removeClass("m-login--signup"), e.addClass("m-login--forget-password"), mUtil.animateClass(e.find(".m-login__forget-password")[0], "flipInX animated")
        }), $("#m_login_forget_password_cancel").click(function (e) {
            e.preventDefault(), a()
        })
    };
    return {
        init: function () {
            l(), $("#m_login_forget_password_submit").click(function (l) {
                l.preventDefault();
                var t = $(this), r = $(this).closest("form");
                r.validate({
                    rules: {
                        email: {
                            required: !0,
                            email: !0
                        }
                    }
                }), r.valid() && (t.addClass("m-loader m-loader--right m-loader--light").attr("disabled", !0), r.ajaxSubmit({
                    url: "",
                    success: function (l, s, n, o) {
                        setTimeout(function () {
                            t.removeClass("m-loader m-loader--right m-loader--light").attr("disabled", !1), r.clearForm(), r.validate().resetForm(), a();
                            var l = e.find(".m-login__signin form");
                            l.clearForm(), l.validate().resetForm(), i(l, "success", "Cool! Password recovery instruction has been sent to your email.")
                        }, 2e3)
                    }
                }))
            })
        }
    }
}();

toastr.options = {
  "closeButton": false,
  "debug": false,
  "newestOnTop": false,
  "progressBar": false,
  "positionClass": "toast-top-right",
  "preventDuplicates": false,
  "onclick": null,
  "showDuration": "300",
  "hideDuration": "1000",
  "timeOut": "5000",
  "extendedTimeOut": "1000",
  "showEasing": "swing",
  "hideEasing": "linear",
  "showMethod": "fadeIn",
  "hideMethod": "fadeOut"
};

function login_success_redirect(response) {
    console.log(response);
    let login_error_dom = $("#login_errors");
	if (response.success == true) {
		window.location.href = 'http://' + response.redirectTo.toString();
	} else {
	    toastr.error("Bạn đã nhập sai tài khoản hoặc mật khẩu. Vui lòng kiểm tra lại ...");
	    // let list_error = message_to_html(response);
		// login_error_dom.append(list_error);
		// $('#login_errors').removeClass('d-none');
	}
}

function message_to_html(message) {
	let list_error = "";
	$.each(message, function (field, errors) {
		list_error += field + " :<ul>";
		$.each(errors, function (code, error) {
			list_error += "<li>" + error.message + "</li>";
		});
		list_error += "</ul>";
	});
	return list_error;
}

$(document).ready(function () {
    SnippetLogin.init();
    $('#login-form').submit(function (e) {
        // alert('click');
        e.preventDefault();
        let csrftoken = getCookie("csrftoken");
		let data = $(this).serializeArray();
		data.push({
			name: "csrfmiddlewaretoken",
			value: csrftoken
		});
		let url = "/api/auth";
		ajax_request(false, true, "POST", "json", url, null, data, login_success_redirect, print_response);
    });

    // TEST AJAX REST
    // $('#test').click(function (e) {
    //     e.preventDefault();
    //     let csrftoken = getCookie("csrftoken");
    //     let data = [];
    //     data.push({
    //         name: "name",
    //         value: "NDVKOjsv"
    //     });
    //     data.push({
    //         name: "csrfmiddlewaretoken",
    //         value: csrftoken
    //     });
    //
    //     let url = "/api/course_category/create";
    //     ajax_request(false, true, "POST", "json", url, null, data, add_sector_success_callback, error_callback);
    //
    // });
    // function add_sector_success_callback() {
    //
    // }
    // function error_callback() {
    //
    // }
});

