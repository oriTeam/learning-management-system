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