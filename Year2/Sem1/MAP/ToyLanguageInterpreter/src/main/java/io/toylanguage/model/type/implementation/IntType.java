package io.toylanguage.model.type.implementation;

import io.toylanguage.model.type.Type;
import io.toylanguage.model.value.Value;
import io.toylanguage.model.value.implementation.IntValue;

public class IntType implements Type {
    private static final String INT_TYPE_NAME = "int";

    @Override
    public boolean equals(Object otherObject) {
        return otherObject instanceof IntType;
    }

    @Override
    public String toString() {
        return INT_TYPE_NAME;
    }

    @Override
    public Value getDefaultValue() {
        return new IntValue();
    }
}
