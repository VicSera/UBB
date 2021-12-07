package ro.ubb.webexam.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import ro.ubb.webexam.model.Author;
import ro.ubb.webexam.model.Document;
import ro.ubb.webexam.repository.AuthorRepository;
import ro.ubb.webexam.repository.DocumentRepository;

import java.util.*;
import java.util.stream.Collectors;

@RestController
@RequestMapping("/api/documents")
@CrossOrigin
public class DocumentController {
    private final DocumentRepository documentRepository;
    private final AuthorRepository authorRepository;

    @Autowired
    public DocumentController(DocumentRepository documentRepository, AuthorRepository authorRepository) {
        this.documentRepository = documentRepository;
        this.authorRepository = authorRepository;
    }

    @PostMapping("/")
    public ResponseEntity<Void> addDocument(@RequestBody Document document) {
        this.documentRepository.save(document);
        return ResponseEntity.ok().build();
    }

    @GetMapping("/most-authors")
    public ResponseEntity<Document> documentWithMostAuthors() {
        Map<Integer, Integer> documentToAuthorCount = new HashMap<>();
        for (Author author : authorRepository.findAll()) {
            String encodedDocumentList = author.getDocumentList();
            List<Integer> ids = Arrays.stream(encodedDocumentList.split(","))
                    .map(Integer::parseInt).collect(Collectors.toList());
            for (Integer id : ids) {
                if (documentToAuthorCount.containsKey(id))
                    documentToAuthorCount.put(id, documentToAuthorCount.get(id) + 1);
                else
                    documentToAuthorCount.put(id, 1);
            }
        }
        Integer id = documentToAuthorCount.entrySet().stream()
                .max(Comparator.comparingInt(Map.Entry::getValue)).get().getKey();
        return ResponseEntity.ok(documentRepository.findById(id).get());
    }
}
