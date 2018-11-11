var BootstrapTimepicker = {
    init: function () {
        $("#session_start_timepicker, #session_end_timepicker").timepicker({
            minuteStep: 1,
            defaultTime: "",
            showSeconds: !0,
            showMeridian: !1,
            snapToStep: !0
        });
    }
};
jQuery(document).ready(function () {
    BootstrapTimepicker.init()
});