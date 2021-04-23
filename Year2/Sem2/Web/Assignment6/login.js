function login() {
    const username = document.getElementById("username").innerText;
    const password = document.getElementById("password").innerText;

    $.ajax({
        type: "POST",
        url: ""
    });

    $.post(apiUrl + "/login", {
            username: username,
            password: password
        }, function (data, status) {
        alert(data + " " + status);
    });
}
