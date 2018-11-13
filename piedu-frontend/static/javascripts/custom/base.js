
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        var cookies = document.cookie.split(";");
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function formdata_to_dict(formdata) {
    let data = {};
    for (var pair of formdata.entries()) {
        data[pair[0]] = pair[1]
    }
    return data;
}

function print_response(response) {
    console.log(response);
}
