package io.toylanguage.model.type.implementation;

import io.toylanguage.model.type.Type;
import io.toylanguage.model.value.Value;
import io.toylanguage.model.value.implementation.BoolValue;
import io.toylanguage.model.value.implementation.StringValue;

public class StringType implements Type {
    private static final String STRING_TYPE_NAME = "string";

    @Override
    public boolean equals(Object otherObject) {
        return otherObject instanceof StringType;
    }

    @Override
    public String toString() {
        return STRING_TYPE_NAME;
    }

    @Override
    public Value getDefaultValue() {
        return new StringValue();
    }
}
