package ro.ubb.webexam.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import ro.ubb.webexam.model.Document;

@Repository
public interface DocumentRepository extends JpaRepository<Document, Integer> {
}
