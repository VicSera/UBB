<%--
  Created by IntelliJ IDEA.
  User: Victor
  Date: 5/13/2021
  Time: 9:56 PM
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Upload image</title>
    <link rel="stylesheet" type="text/css" href="style/core.css">
    <link rel="stylesheet" type="text/css" href="style/uploadImage.css">
</head>
<body>
    <form class="card" method="post" action="image-servlet" enctype="multipart/form-data">
        <input name="title" placeholder="Image title">
        <label for="image">Image:</label>
        <input type="file" accept="image/*" name="image" id="image" alt="Drop image here">
        <button type="submit">Post</button>
    </form>
</body>
</html>
