package io.toylanguage.datastructure.exception;

import io.toylanguage.exception.ToyLanguageException;

public class KeyNotFoundException extends ToyLanguageException {
    public KeyNotFoundException(String message) {
        super(message);
    }

    public KeyNotFoundException() {
        super("");
    }
}
