package io.toylanguage.model.exception.arithmetic.specific;

import io.toylanguage.model.exception.arithmetic.ArithmeticException;

public class DivisonByZeroException extends ArithmeticException {
    public DivisonByZeroException() {
        super("Cannot divide by 0");
    }
}
