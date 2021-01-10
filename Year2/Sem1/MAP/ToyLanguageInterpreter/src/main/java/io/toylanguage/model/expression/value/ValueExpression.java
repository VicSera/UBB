package io.toylanguage.model.expression.value;

import io.toylanguage.datastructure.Heap;
import io.toylanguage.datastructure.Map;
import io.toylanguage.datastructure.aliases.SymbolTable;
import io.toylanguage.datastructure.aliases.TypeEnvironment;
import io.toylanguage.exception.ToyLanguageException;
import io.toylanguage.model.expression.Expression;
import io.toylanguage.model.type.Type;
import io.toylanguage.model.value.Value;

public class ValueExpression implements Expression {
    Value value;

    public ValueExpression(Value value) {
        this.value = value;
    }

    public Value evaluate(SymbolTable symbolTable, Heap heap) {
        return value;
    }

    @Override
    public Type typeCheck(TypeEnvironment typeEnvironment) throws ToyLanguageException {
        return value.getType();
    }

    @Override
    public String toString() {
        return "%s".formatted(value);
    }
}
