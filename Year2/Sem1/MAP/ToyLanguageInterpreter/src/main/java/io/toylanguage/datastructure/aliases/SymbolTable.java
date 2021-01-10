package io.toylanguage.datastructure.aliases;

import io.toylanguage.datastructure.implementation.StandardMap;
import io.toylanguage.model.value.Value;

import java.util.Map;

public class SymbolTable extends StandardMap<String, Value> {
    private SymbolTable(Map<String, Value> map) {
        super(map);
    }

    public SymbolTable() {

    }

    @Override
    public synchronized SymbolTable deepCopy() {
        return new SymbolTable(super.map);
    }
}
