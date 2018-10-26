let breadcrumb = '<ul class="bread-crumb px-0">\n' +
    '  <li><a href="/"><span class="fa fa-home"> </span> Trang chủ</a></li>\n' +
    '  <li><a href="/course">Tất cả khóa học</a></li>\n' +
    '  </ul>';
let search = '<form action="">\n' +
    '                    <div class="inner-form">\n' +
    '                        <div class="input-field">\n' +
    '                            <button class="btn-search" type="button">\n' +
    '                                <i class="fa fa-search"></i>\n' +
    '                            </button>\n' +
    '                            <input id="search" class="form-control" type="text" placeholder="" value="Tìm kiếm khóa học ...">\n' +
    '                        </div>\n' +
    '                    </div>\n' +
    '                </form>\n';
let innerContent = '';
let menuSide = '';

Vue.component('breadcrumb', {template: breadcrumb });
Vue.component('search', {template: search });

new Vue({
    el: '#all-course-body',
})