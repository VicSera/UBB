package io.toylanguage.datastructure.aliases;

import io.toylanguage.datastructure.implementation.StandardMap;
import io.toylanguage.model.type.Type;
import io.toylanguage.model.value.Value;

import java.util.Map;

public class TypeEnvironment extends StandardMap<String, Type> {
    private TypeEnvironment(Map<String, Type> map) {
        super(map);
    }

    public TypeEnvironment() {

    }

    @Override
    public synchronized TypeEnvironment deepCopy() {
        return new TypeEnvironment(super.map);
    }
}
