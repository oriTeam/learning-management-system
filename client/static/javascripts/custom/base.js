(function($) {
	"use strict"

	// Preloader
	$(window).on('load', function() {
		$("#preloader").delay(600).fadeOut();
	});

	// Mobile Toggle Btn
	$('.navbar-toggle').on('click',function(){
	    $('#navbar').removeClass('collapse')
		$('#navi-bar').toggleClass('nav-collapser');
	});

})(jQuery);


function ajax_request(cache_, async_, type_, data_type_, url_, headers_, data_, success_, error_) {
    return $.ajax({
        cache: cache_,
        async: async_,
        type: type_,
        dataType: data_type_,
        headers: headers_,
        url: url_,
        data: data_,
        success: function (response) {
            success_ != null && success_(response);
        },
        error: function (response) {
            error_ != null && error_(response);
        }
    });
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        var cookies = document.cookie.split(";");
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function print_response(response) {
    console.log(response);
}

window.onscroll = function () {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        $("#gotop").css({display: "block"});
    }
    else $("#gotop").css({display: "none"});
};

$("#gotop").click(function () {
    $("html, body").animate({
        scrollTop: $("body").offset().top
        // document.documentElement.scrollTop = 0,
    }, 250);
});

let search = '<div class="col-12 pb-3">\n' +
    '            <div class="row justify-content-center mx-0 text-center m--padding-top-30-desktop m--padding-top-20-mobile pb-4">\n' +
    '                <h2>Tìm kiếm khóa học</h2>\n' +
    '            </div>\n' +
    '            <div class="row mx-0 justify-content-center">\n' +
    '                <div class="col-lg-7 col-sm-12">\n' +
    '                    <form action="">\n' +
    '                        <div class="inner-form">\n' +
    '                            <div class="input-field">\n' +
    '                                <button type="button" class="btn-search"><i class="fa fa-search"></i></button>\n' +
    '                                <input id="search" type="text" placeholder="Tìm kiếm khóa học ..."\n' +
    '                                       class="form-control"></div>\n' +
    '                        </div>\n' +
    '                    </form>\n' +
    '                </div>\n' +
    '            </div>\n' +
    '        </div>';
