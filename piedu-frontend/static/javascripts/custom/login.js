toastr.options = {
  "closeButton": false,
  "debug": false,
  "newestOnTop": false,
  "progressBar": false,
  "positionClass": "toast-top-right",
  "preventDuplicates": false,
  "onclick": null,
  "showDuration": "300",
  "hideDuration": "1000",
  "timeOut": "5000",
  "extendedTimeOut": "1000",
  "showEasing": "swing",
  "hideEasing": "linear",
  "showMethod": "fadeIn",
  "hideMethod": "fadeOut"
};

$(document).ready(function () {
    // TEST AJAX REST
    // $('#test').click(function (e) {
    //     e.preventDefault();
    //     let csrftoken = getCookie("csrftoken");
    //     let data = [];
    //     data.push({
    //         name: "name",
    //         value: "NDVKOjsv"
    //     });
    //     data.push({
    //         name: "csrfmiddlewaretoken",
    //         value: csrftoken
    //     });
    //
    //     let url = "/api/course_category/create";
    //     ajax_request(false, true, "POST", "json", url, null, data, add_sector_success_callback, error_callback);
    //
    // });
    // function add_sector_success_callback() {
    //
    // }
    // function error_callback() {
    //
    // }
});

