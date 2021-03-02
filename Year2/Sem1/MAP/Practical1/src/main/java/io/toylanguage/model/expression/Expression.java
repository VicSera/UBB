package io.toylanguage.model.expression;

import io.toylanguage.datastructure.Heap;
import io.toylanguage.datastructure.Map;
import io.toylanguage.datastructure.aliases.SymbolTable;
import io.toylanguage.datastructure.aliases.TypeEnvironment;
import io.toylanguage.exception.ToyLanguageException;
import io.toylanguage.model.type.Type;
import io.toylanguage.model.value.Value;

public interface Expression {
    Value evaluate(SymbolTable symbolTable, Heap heap) throws ToyLanguageException;

    Type typeCheck(TypeEnvironment typeEnvironment) throws ToyLanguageException;
}
