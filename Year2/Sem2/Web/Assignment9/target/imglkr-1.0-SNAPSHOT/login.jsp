<%--
  Created by IntelliJ IDEA.
  User: Victor
  Date: 5/13/2021
  Time: 9:43 PM
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Login</title>
    <link rel="stylesheet" type="text/css" href="style/login.css">
    <link rel="stylesheet" type="text/css" href="style/core.css">
</head>
<body>
    <form method="post" action="login-servlet" class="card" enctype="application/x-www-form-urlencoded">
        <div class="login-info">
            <input name="username" id="username" placeholder="Username">
        </div>

        <div class="login-info">
            <input name="password" id="password" type="password" placeholder="Password">
        </div>
        <button type="submit">Log in</button>
    </form>
</body>
</html>
