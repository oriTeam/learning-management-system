var breadcrumb = '<ul class="bread-crumb px-0">\n' +
    '  <li><a href="/"><span class="fa fa-home"> </span> Trang chủ</a></li>\n' +
    '  <li><a href="/help">Trợ giúp</a></li>\n' +
    '  </ul>';
var search = '<form action="">\n' +
    '                    <div class="inner-form">\n' +
    '                        <div class="input-field">\n' +
    '                            <button class="btn-search" type="button">\n' +
    '                                <i class="fa fa-search"></i>\n' +
    '                            </button>\n' +
    '                            <input id="search" class="form-control" type="text" placeholder="" value="Tìm kiếm câu hỏi ...">\n' +
    '                        </div>\n' +
    '                    </div>\n' +
    '                </form>\n';
var innerContent = '';
var menuSide = '';

Vue.component('breadcrumb', {template: breadcrumb });
Vue.component('search', {template: search });

new Vue({
    el: '#help-body',
})