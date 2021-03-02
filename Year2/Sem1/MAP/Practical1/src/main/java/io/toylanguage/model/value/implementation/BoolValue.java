package io.toylanguage.model.value.implementation;

import io.toylanguage.model.type.Type;
import io.toylanguage.model.type.implementation.BoolType;
import io.toylanguage.model.value.Value;

public class BoolValue implements Value {
    private static final String BOOL_VALUE_STRING = new BoolType().toString() + "(%b)";
    Boolean value;

    public BoolValue() {
        this.value = false;
    }

    public BoolValue(Boolean value) {
        this.value = value;
    }

    public Boolean getValue() {
        return value;
    }

    @Override
    public Type getType() {
        return new BoolType();
    }

    @Override
    public String toString() {
        return BOOL_VALUE_STRING.formatted(value);
    }
}
