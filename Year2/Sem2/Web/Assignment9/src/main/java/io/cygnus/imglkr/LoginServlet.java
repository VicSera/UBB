package io.cygnus.imglkr;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.sql.*;

@WebServlet("/login-servlet")
public class LoginServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request,
                          HttpServletResponse response) throws ServletException, IOException {

        String username = request.getParameter("username");
        String password = request.getParameter("password");
        int id = -1;

        Connection conn = null;
        try {
            DriverManager.registerDriver(new com.mysql.cj.jdbc.Driver());
            conn = DriverManager.getConnection(DBConfig.url, DBConfig.user, DBConfig.password);

            String sql = "select id from t_user where username = ? and password = ?";
            PreparedStatement statement = conn.prepareStatement(sql);
            statement.setString(1, username);
            statement.setString(2, password);

            ResultSet rs = statement.executeQuery();
            if (rs.next()) {
                id = rs.getInt(1);

                Cookie userIdCookie = new Cookie("userId", Integer.toString(id));
                userIdCookie.setMaxAge(60 * 60 * 24 * 7);
                response.addCookie(userIdCookie);

                response.sendRedirect(request.getContextPath() + "/load-images-servlet");
            } else {
                response.sendRedirect(request.getContextPath() + "/login.jsp");
            }

        } catch (SQLException exception) {
            exception.printStackTrace();
        } finally {
            if (conn != null) {
                try {
                    conn.close();
                } catch (SQLException exception) {
                    exception.printStackTrace();
                }
            }
        }
    }
}
