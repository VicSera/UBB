package io.toylanguage.model.value.implementation;

import io.toylanguage.model.type.Type;
import io.toylanguage.model.type.implementation.IntType;
import io.toylanguage.model.type.implementation.RefType;
import io.toylanguage.model.value.Value;

public class RefValue implements Value {
    private final String REF_VALUE_STRING;
    int address;
    Type referencedType;

    public RefValue(Type referencedType) {
        address = 0;
        this.referencedType = referencedType;
        REF_VALUE_STRING = new RefType(referencedType).toString() + "[%d]";
    }

    public RefValue(int address, Type referencedType) {
        this.address = address;
        this.referencedType = referencedType;
        REF_VALUE_STRING = new RefType(referencedType).toString() + "[%d]";
    }

    public int getAddress() {
        return this.address;
    }

    @Override
    public Type getType() {
        return new RefType(referencedType);
    }

    public Type getReferencedType() {
        return referencedType;
    }

    @Override
    public String toString() {
        return REF_VALUE_STRING.formatted(address);
    }
}
