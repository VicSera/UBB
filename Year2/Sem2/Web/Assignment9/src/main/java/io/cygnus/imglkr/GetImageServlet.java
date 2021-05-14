package io.cygnus.imglkr;

import io.cygnus.imglkr.dtos.ImageWithLikesDTO;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;


@WebServlet("/get-image-servlet")
public class GetImageServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        int userId = Util.getUserId(request, response);
        int imageId = Integer.parseInt(request.getParameter("id"));

        Connection conn = null;
        ResultSet rs = null;
        PreparedStatement statement = null;
        try {
            DriverManager.registerDriver(new com.mysql.cj.jdbc.Driver());
            conn = DriverManager.getConnection(DBConfig.url, DBConfig.user, DBConfig.password);

            String sql = """
            select img.content from t_image img where img.id = ?
            """;
            statement = conn.prepareStatement(sql);
            statement.setInt(1, imageId);

            rs = statement.executeQuery();
            if (rs.next()) {
                InputStream input = rs.getBinaryStream("content");
                OutputStream output = response.getOutputStream();
                response.setContentType("image/*");
                output.write(input.readAllBytes());
            }

//            request.getServletContext().getRequestDispatcher("/images.jsp").forward(request, response);
//            response.sendRedirect(request.getContextPath() + "/images.jsp");
        } catch (SQLException exception) {
            exception.printStackTrace();
        }
    }
}
