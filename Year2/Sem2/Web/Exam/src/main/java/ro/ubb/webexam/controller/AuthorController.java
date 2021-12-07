package ro.ubb.webexam.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import ro.ubb.webexam.model.Author;
import ro.ubb.webexam.model.Document;
import ro.ubb.webexam.model.Movie;
import ro.ubb.webexam.repository.AuthorRepository;
import ro.ubb.webexam.repository.DocumentRepository;
import ro.ubb.webexam.repository.MovieRepository;

import java.util.Arrays;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

@RestController
@RequestMapping("/api/authors")
@CrossOrigin
public class AuthorController {
    private final AuthorRepository authorRepository;
    private final DocumentRepository documentRepository;
    private final MovieRepository movieRepository;

    @Autowired
    public AuthorController(AuthorRepository authorRepository, DocumentRepository documentRepository, MovieRepository movieRepository) {
        this.authorRepository = authorRepository;
        this.documentRepository = documentRepository;
        this.movieRepository = movieRepository;
    }

    @PostMapping("/login")
    public ResponseEntity<Author> login(@RequestBody String name) {
        Optional<Author> author = authorRepository.findByName(name);
        return author.map(ResponseEntity::ok).orElseGet(() -> ResponseEntity.notFound().build());
    }

    @GetMapping("/get-documents/{id}")
    public ResponseEntity<List<Document>> getDocuments(@PathVariable("id") Integer authorId) {
        Author author = authorRepository.getById(authorId);
        String encodedDocumentList = author.getDocumentList();
        List<Integer> documentIds = Arrays.stream(encodedDocumentList.split(","))
                .map(Integer::parseInt)
                .collect(Collectors.toList());
        return ResponseEntity.ok(documentRepository.findAllById(documentIds));
    }

    @GetMapping("/get-movies/{id}")
    public ResponseEntity<List<Movie>> getMovies(@PathVariable("id") Integer authorId) {
        Author author = authorRepository.getById(authorId);
        String encodedMovieList = author.getMovieList();
        List<Integer> movieIds = Arrays.stream(encodedMovieList.split(","))
                .map(Integer::parseInt)
                .collect(Collectors.toList());
        return ResponseEntity.ok(movieRepository.findAllById(movieIds));
    }
}
