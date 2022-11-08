$(document).ready(function () {

  function handleError(){

    $("#error").text("Sorry your creadentials are bad")
    alert("Sorry")
  }

  function postForm(path, params, method) {
    method = method || "post";

    var form = document.createElement("form");
    form.setAttribute("method", method);
    form.setAttribute("action", path);

    for (var key in params) {
      if (params.hasOwnProperty(key)) {
        var hiddenField = document.createElement("input");
        hiddenField.setAttribute("type", "hidden");
        hiddenField.setAttribute("name", key);
        hiddenField.setAttribute("value", params[key]);

        form.appendChild(hiddenField);
      }
    }

    document.body.appendChild(form);
    form.submit();
  }

  $("#loginbutton").on("click", function () {
    username = $("#username").val();
    password = $("#password").val();
    var data = { username: username, password: password };
    $.ajax({
      method: "POST",
      url: "/loginvalidate",
      contentType: "application/json;charset=utf-8",
      cache: false,
      datatype: "text",
      data: JSON.stringify(data),
      success: function (data) {
        if (data == "success") {
          alert(data);
          postForm("/login", { username: username });
        } else {
          handleError()
        }
      },
      error: function (data) {
      },
    });
  });
});
