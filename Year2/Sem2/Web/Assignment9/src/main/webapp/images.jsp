<%--
  Created by IntelliJ IDEA.
  User: Victor
  Date: 5/14/2021
  Time: 1:15 AM
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<html>
<head>
    <title>Images</title>
    <link rel="stylesheet" type="text/css" href="style/core.css">
</head>
<body>
    <form method="get" action="uploadImage.jsp">
        <button type="submit">Add a new image</button>
    </form>
    <form method="get" action="${pageContext.request.contextPath}/load-images-servlet">
        <label for="limit">Limit:</label>
        <input name="limit" id="limit" placeholder="10">
    </form>
    <div class="image-list">
        <c:forEach var="image" items="${images}">
            <div>
                Title: ${image.title} |
                Uploaded by: ${image.username} |
                <c:choose>
                    <c:when test="${image.liked}">
                        <form method="post" action="${pageContext.request.contextPath}/dislike-image-servlet?imageId=${image.id}">
                            <button>Dislike this!</button>
                        </form>
                    </c:when>
                    <c:otherwise>
                        <form method="post" action="${pageContext.request.contextPath}/like-image-servlet?imageId=${image.id}">
                            <button>Like this!</button>
                        </form>
                    </c:otherwise>
                </c:choose>
                ${image.likes} people like this
                <br>
                <img src="${pageContext.request.contextPath}/get-image-servlet?id=${image.id}"
                     alt="image" width="500px" height="500px"/>
            </div>
            <hr>
        </c:forEach>
    </div>
</body>
</html>
