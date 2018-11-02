// var breadcrum = require('./contact')


let breadcrumb = '<ul class="bread-crumb px-0">\n' +
    '  <li><a href="/"><span class="fa fa-home"> </span> Trang chủ</a></li>\n' +
    '  <li><a href="/my-course">Khóa học của tôi</a></li>\n' +
    '  </ul>';
let search = '<div class="col-12 pb-3">\n' +
    '            <div class="row justify-content-center mx-0 text-center m--padding-top-30-desktop m--padding-top-20-mobile pb-4">\n' +
    '                <h2>Tìm kiếm khóa học của tôi</h2>\n' +
    '            </div>\n' +
    '            <div class="row mx-0 justify-content-center">\n' +
    '                <div class="col-lg-7 col-sm-12">\n' +
    '                    <form action="">\n' +
    '                        <div class="inner-form">\n' +
    '                            <div class="input-field">\n' +
    '                                <button type="button" class="btn-search"><i class="fa fa-search"></i></button>\n' +
    '                                <input id="search" type="text" placeholder="" value="Tìm kiếm khóa học ..."\n' +
    '                                       class="form-control"></div>\n' +
    '                        </div>\n' +
    '                    </form>\n' +
    '                </div>\n' +
    '            </div>\n' +
    '        </div>';
let innerContent = '';
let menuSide = '';
let mainContent = '';

Vue.component('breadcrumb', {template: breadcrumb });
Vue.component('search', {template: search });

new Vue({
    el: '#my-course-body',
    // components: {
    //     'breadcrumb': breadcrumb,
    //     'search': search
    // }
})