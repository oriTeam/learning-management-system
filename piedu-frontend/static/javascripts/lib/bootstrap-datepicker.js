var BootstrapDatepicker = function () {
    var t;
    t = mUtil.isRTL() ? {
        leftArrow: '<i class="la la-angle-right"></i>',
        rightArrow: '<i class="la la-angle-left"></i>'
    } : {leftArrow: '<i class="la la-angle-left"></i>', rightArrow: '<i class="la la-angle-right"></i>'};
    return {
        init: function () {
            $("#start_datepicker, #end_datepicker").datepicker({
                rtl: mUtil.isRTL(),
                todayBtn: "linked",
                clearBtn: !0,
                todayHighlight: !0,
                templates: t
            });
        }
    }
}();
jQuery(document).ready(function () {
    BootstrapDatepicker.init()
});