    // // var fixmeTop = $('#m_aside_left').offset().top;
    // // $(window).scroll(function() {
    // //     var currentScroll = $(window).scrollTop() + 65;
    // //     if (currentScroll >= fixmeTop && Math.max(document.documentElement.clientWidth, window.innerWidth || 0) >= 1025) {
    // //         $('#m_aside_left').addClass('fixed-aside');
    // //         // document.getElementById('m_aside_left').style.setProperty("width", "305px", "important");
    // //     } else {
    // //         $('#m_aside_left').removeClass('fixed-aside');
    // //     }
    // // });
    //
    // let el = document.getElementById('m_aside_left');
    // let rect = el.getBoundingClientRect();
    // let fixmeTop= rect.top + document.body.scrollTop;
    // window.addEventListener('scroll', function () {
    //
    //             let currentScroll = window.scrollY + 65;
    //             if (currentScroll >= fixmeTop && Math.max(document.documentElement.clientWidth, window.innerWidth || 0) >= 1025) {
    //                 // $('#m_aside_left').addClass('fixed-aside');
    //                 // document.getElementById('m_aside_left').style.setProperty("width", "305px", "important");
    //                 if (el.classList)
    //                     el.classList.add('fixed-aside');
    //                 else
    //                     el.className += ' ' + 'fixed-aside';
    //             } else {
    //                 // $('#m_aside_left').removeClass('fixed-aside');
    //                 if (el.classList)
    //                     el.classList.remove('fixed-aside');
    //                 else
    //                     el.className = el.className.replace(new RegExp('(^|\\b)' + 'fixed-aside'.split(' ').join('|') + '(\\b|$)', 'gi'), ' ');
    //             }
    //         });
