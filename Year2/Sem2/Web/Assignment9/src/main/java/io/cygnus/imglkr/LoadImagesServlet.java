package io.cygnus.imglkr;

import io.cygnus.imglkr.dtos.ImageWithLikesDTO;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;


@WebServlet("/load-images-servlet")
public class LoadImagesServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        int userId = Util.getUserId(request, response);
        String limitStr = request.getParameter("limit");
        int limit = limitStr == null? 10 : Integer.parseInt(limitStr);

        Connection conn = null;
        ResultSet rs = null;
        PreparedStatement statement = null;
        try {
            DriverManager.registerDriver(new com.mysql.cj.jdbc.Driver());
            conn = DriverManager.getConnection(DBConfig.url, DBConfig.user, DBConfig.password);

            String sql = """
            select img.id, img.title, img.content, img.userId, u.username, if(likedByUser.imageId is not null, true, false) as liked, ifnull(imageLikes.likes, 0) as likes
            from t_image img
            left join (
                select lk.imageId as imageId, count(lk.userId) as likes from t_like lk
                group by lk.imageId
            ) as imageLikes on img.id = imageLikes.imageId
            left join (
                select distinct imageId from t_like where userId = ?
            ) as likedByUser on likedByUser.imageId = img.id
            left join t_user u on u.id = img.userId
            order by likes desc
            limit ?
            """;
            statement = conn.prepareStatement(sql);
            statement.setInt(1, userId);
            statement.setInt(2, limit);

            rs = statement.executeQuery();
            List<ImageWithLikesDTO> images = new ArrayList<>();
            while (rs.next()) {
                var img = new ImageWithLikesDTO();
                img.setId(rs.getInt("id"));
                img.setTitle(rs.getString("title"));
                img.setUserId(rs.getInt("userId"));
                img.setUsername(rs.getString("username"));
                img.setLiked(rs.getBoolean("liked"));
                img.setLikes(rs.getInt("likes"));

                images.add(img);
            }

            request.setAttribute("images", images);
            request.getServletContext().getRequestDispatcher("/images.jsp").forward(request, response);

//            response.sendRedirect(request.getContextPath() + "/images.jsp");
        } catch (SQLException exception) {
            exception.printStackTrace();
        }
    }
}
