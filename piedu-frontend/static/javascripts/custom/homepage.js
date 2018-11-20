$(function() {
    "use strict";
    /*-----------------------------------
     * FIXED  MENU - HEADER
     *-----------------------------------*/
    function menuscroll() {
        var $navmenu = $('.nav-menu');
        if ($(window).scrollTop() > 50) {
            $navmenu.addClass('is-scrolling');
        } else {
            $navmenu.removeClass("is-scrolling");
        }
    }
    menuscroll();
    $(window).on('scroll', function() {
        menuscroll();
    });
    /*
     * NAVBAR TOGGLE BG
     *-----------------*/
    var siteNav = $('#navbar');
    siteNav.on('show.bs.collapse', function(e) {
        $(this).parents('.nav-menu').addClass('menu-is-open');
    })
    siteNav.on('hide.bs.collapse', function(e) {
        $(this).parents('.nav-menu').removeClass('menu-is-open');
    })
     /*-----------------------------------
     * OWL CAROUSEL
     *-----------------------------------*/
    var $galleryDiv = $('.img-gallery');
    if ($galleryDiv.length && $.fn.owlCarousel) {
        $galleryDiv.owlCarousel({
            nav: false,
            center: true,
            loop: true,
            autoplay: true,
            dots: true,
            navText: ['<span class="ti-arrow-left"></span>', '<span class="ti-arrow-right"></span>'],
            responsive: {
                0: {
                    items: 1
                },
                768: {
                    items: 3
                }
            }
        });
    }

}); /* End Fn */
"use strict";

// const axios = require('axios');
// import axios from 'axios';
$(document).ready(function () {
    
    $('.count').each(function() {
		$(this).prop('Counter', 0).animate({
			counter: $(this).text()}, {duration: 10000, easing:'swing',step: function(now) {
				$(this).text(Math.ceil(now));
			}
		});
    });
    $(document).on('click touch','#test',function(){
        let subject_id = 10;
        axios.get('/api/class/a'+subject_id)
        .then(function(response){
            console.log(response.data);
        })
        .catch(function(error){
            alert(error);
        });
    })
    
})
