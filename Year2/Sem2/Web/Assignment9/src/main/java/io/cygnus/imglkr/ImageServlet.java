package io.cygnus.imglkr;

import javax.servlet.ServletException;
import javax.servlet.annotation.MultipartConfig;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.Part;
import java.io.IOException;
import java.io.InputStream;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

@WebServlet("/image-servlet")
@MultipartConfig(maxFileSize = 16177215)
public class ImageServlet extends HttpServlet {

    protected void doPost(HttpServletRequest request,
                          HttpServletResponse response) throws ServletException, IOException {

        String title = request.getParameter("title");
        int userId = Util.getUserId(request, response);

        InputStream inputStream = null;

        Part filePart = request.getPart("image");
        if (filePart != null) {
            System.out.println(filePart.getName());
            System.out.println(filePart.getSize());
            System.out.println(filePart.getContentType());

            inputStream = filePart.getInputStream();
        }

        Connection conn = null;
        String message = null;

        try {
//            DriverManager.registerDriver(new com.mysql.jdbc.Driver());
            conn = DriverManager.getConnection(DBConfig.url, DBConfig.user, DBConfig.password);

            String sql = "insert into t_image (title, content, userId) values (?, ?, ?)";
            PreparedStatement statement = conn.prepareStatement(sql);
            statement.setString(1, title);
            statement.setInt(3, userId);

            if (inputStream != null) {
                statement.setBlob(2, inputStream);
            }

            int row = statement.executeUpdate();
            if (row > 0) {
                message = "Image successfully added";
            }
        } catch (SQLException ex) {
            message = "ERROR: " + ex.getMessage();
            ex.printStackTrace();
        } finally {
            if (conn != null) {
                try {
                    conn.close();
                } catch (SQLException ex) {
                    ex.printStackTrace();
                }
            }

            response.sendRedirect(request.getContextPath() + "/load-images-servlet");
        }
    }
}
