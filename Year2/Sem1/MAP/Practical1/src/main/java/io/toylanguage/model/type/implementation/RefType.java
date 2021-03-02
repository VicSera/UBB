package io.toylanguage.model.type.implementation;

import io.toylanguage.model.type.Type;
import io.toylanguage.model.value.Value;
import io.toylanguage.model.value.implementation.IntValue;
import io.toylanguage.model.value.implementation.RefValue;

public class RefType implements Type {
    private static final String REF_TYPE_NAME = "ref(%s)";
    private final Type referencedType;

    public RefType(Type referencedType) {
        this.referencedType = referencedType;
    }

    @Override
    public boolean equals(Object otherObject) {
        if (otherObject instanceof RefType)
            return referencedType.equals(((RefType) otherObject).getReferencedType());
        return false;
    }

    @Override
    public String toString() {
        return REF_TYPE_NAME.formatted(referencedType);
    }

    @Override
    public Value getDefaultValue() {
        return new RefValue(referencedType);
    }

    public Type getReferencedType() {
        return referencedType;
    }
}
