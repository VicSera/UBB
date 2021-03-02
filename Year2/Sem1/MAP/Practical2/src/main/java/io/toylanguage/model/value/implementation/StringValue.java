package io.toylanguage.model.value.implementation;

import io.toylanguage.model.type.Type;
import io.toylanguage.model.type.implementation.StringType;
import io.toylanguage.model.value.Value;

public class StringValue implements Value {
    private static final String STRING_VALUE_STRING = new StringType().toString() + "(%s)";
    String value;

    public StringValue() {
        this.value = "";
    }

    public StringValue(String value) {
        this.value = value;
    }

    public String getValue() {
        return value;
    }

    @Override
    public Type getType() {
        return new StringType();
    }

    @Override
    public String toString() {
        return STRING_VALUE_STRING.formatted(value);
    }
}
