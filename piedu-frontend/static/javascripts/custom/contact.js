
$(document).ready(function(){
    $(".m-input").focus(function(){
        $(this).css("background-color", "#E6E6E6");
    });
    $(".m-input").blur(function(){
        $(this).css("background-color", "#ffffff");
        var value = $(this).val();
        if (value.trim().length == 0) {
            $(this).css("border", "1px solid red");
            }
        else {
            $(this).css("border", "");
            $(this).css("opacity","");
        }
    });
});
