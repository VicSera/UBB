package io.toylanguage.model.exception.arithmetic.specific;

import io.toylanguage.model.exception.arithmetic.ArithmeticException;

public class WrongOperandTypeException extends ArithmeticException {
    public WrongOperandTypeException(String message) {
        super(message);
    }
}
