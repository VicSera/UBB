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
    <link rel="stylesheet" type="text/css" href="style/flex-body.css">
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
                        <form class="inline" method="post" action="${pageContext.request.contextPath}/dislike-image-servlet?imageId=${image.id}">
                            <button>Remove like</button>
                        </form>
                    </c:when>
                    <c:otherwise>
                        <form class="inline" method="post" action="${pageContext.request.contextPath}/like-image-servlet?imageId=${image.id}">
                            <button>Like this!</button>
                        </form>
                    </c:otherwise>
                </c:choose>
                ${image.likes} like(s)
                <br>
                <img src="${pageContext.request.contextPath}/get-image-servlet?id=${image.id}" alt="image"/>
            </div>
            <hr>
        </c:forEach>
    </div>
</body>
</html>
