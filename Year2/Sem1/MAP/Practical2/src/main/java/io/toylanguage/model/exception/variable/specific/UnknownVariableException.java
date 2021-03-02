package io.toylanguage.model.exception.variable.specific;

import io.toylanguage.model.exception.variable.VariableException;

public class UnknownVariableException extends VariableException {
    public UnknownVariableException(String message) {
        super(message);
    }
}
