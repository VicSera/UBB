package ro.ubb.webexam.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import ro.ubb.webexam.model.Movie;

@Repository
public interface MovieRepository extends JpaRepository<Movie, Integer> {
}
