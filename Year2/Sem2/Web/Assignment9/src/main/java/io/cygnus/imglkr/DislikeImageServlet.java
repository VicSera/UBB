package io.cygnus.imglkr;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

@WebServlet("/dislike-image-servlet")
public class DislikeImageServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request,
                          HttpServletResponse response) throws ServletException, IOException {

        int userId = Util.getUserId(request, response);
        int imageId = Integer.parseInt(request.getParameter("imageId"));

        Connection conn = null;
        try {
            DriverManager.registerDriver(new com.mysql.cj.jdbc.Driver());
            conn = DriverManager.getConnection(DBConfig.url, DBConfig.user, DBConfig.password);

            String sql = "delete from t_like where userId = ? and imageId = ?";
            PreparedStatement statement = conn.prepareStatement(sql);
            statement.setInt(1, userId);
            statement.setInt(2, imageId);

            int rowsAffected = statement.executeUpdate();
            if (rowsAffected == 1) {
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
