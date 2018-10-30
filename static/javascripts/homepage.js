$.fn.isOnViewport = function() {
	let wind = $(window);
	let viewport = {
		top : wind.scrollTop(),
		left : wind.scrollLeft()
	};
	viewport.right = viewport.left + wind.width();
	viewport.bottom = viewport.top + wind.height();

	let bounds = this.offset();
	bounds.right = bounds.left + this.outerWidth();
	bounds.bottom = bounds.top + this.outerHeight();

	return (!(viewport.right < bounds.left || viewport.left > bounds.right || viewport.bottom < bounds.top || viewport.top > bounds.bottom));
};

$(document).ready(function(){

    $('.navbar-toggler').click(function() {
    	if(!$(window).scrollTop()) {
    		$('#navi-bar').toggleClass('navbar__over');
    	}
    });

	// $(window).resize(function(){
	// 	let height = $(window).height() - $('#navibar').height();
	// 	$('.home__view').css({'height': height});
	// });
	$(window).on('scroll', function() {
		if($(window).scrollTop()) {
			$('#navi-bar').addClass('navbar__over');
		}
		else {
			$('#navi-bar').removeClass('navbar__over');
		};
		// if($('.showlater').isOnViewport()) {
		// 	$('.showlater').show().addClass('animated bounceInRight');
		// };
		// if($('#carousel-id').isOnViewport()) {
		// 	$('#carousel-id').addClass('animated bounceInLeft');
		// };
		// if($('.main-function').isOnViewport()) {
		// 	$('.main-function').addClass('animated flipInX');
		// };
		// if($('.count').isOnViewport()){}

	});

	// $('.count').each(function() {
	// 	$(this).prop('Counter', 0).animate({
	// 		counter: $(this).text()}, {duration: 10000, easing:'swing',step: function(now) {
	// 			$(this).text(Math.ceil(now));
	// 		}
	// 	});
	// });


	$(document).on('click touch',"#test",function(){
		let data = {
			"course_id" : "1",
		};
		let url = '/api/course/course_info';
		ajax_request(false,true,"GET","json",url,null,data,success_callback,error_callback);
	});
	function success_callback(){
		alert("OK!");
	}
	function error_callback(){
		alert("Failed!");
	}
});