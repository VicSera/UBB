package io.toylanguage.model.type.implementation;

import io.toylanguage.model.type.Type;
import io.toylanguage.model.value.Value;
import io.toylanguage.model.value.implementation.BoolValue;

public class BoolType implements Type {
    private static final String BOOL_TYPE_NAME = "bool";

    @Override
    public boolean equals(Object otherObject) {
        return otherObject instanceof BoolType;
    }

    @Override
    public String toString() {
        return BOOL_TYPE_NAME;
    }

    @Override
    public Value getDefaultValue() {
        return new BoolValue();
    }
}
