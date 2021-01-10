package io.toylanguage.model.value.implementation;

import io.toylanguage.model.type.Type;
import io.toylanguage.model.type.implementation.IntType;
import io.toylanguage.model.value.Value;

public class IntValue implements Value  {
    private static final String INT_VALUE_STRING = new IntType().toString() + "(%d)";
    int value;

    public IntValue() {
        this.value = 0;
    }

    public IntValue(int value) {
        this.value = value;
    }

    public int getValue() {
        return this.value;
    }

    @Override
    public Type getType() {
        return new IntType();
    }

    @Override
    public String toString() {
        return INT_VALUE_STRING.formatted(value);
    }
}
