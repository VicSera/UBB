package io.cygnus.imglkr;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.Arrays;

public class Util {
    public static int getUserId(HttpServletRequest request, HttpServletResponse response) throws IOException {
        int userId =  Arrays.stream(request.getCookies())
                .filter(cookie -> cookie.getName().equals("userId"))
                .map(cookie -> Integer.parseInt(cookie.getValue()))
                .findFirst().orElse(-1);

        if (userId == -1) {
            response.sendRedirect(request.getContextPath() + "/login.jsp");
        }

        return userId;
    }
}
