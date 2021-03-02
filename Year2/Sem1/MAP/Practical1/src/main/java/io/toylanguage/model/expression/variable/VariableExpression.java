package io.toylanguage.model.expression.variable;

import io.toylanguage.datastructure.Heap;
import io.toylanguage.datastructure.Map;
import io.toylanguage.datastructure.aliases.SymbolTable;
import io.toylanguage.datastructure.aliases.TypeEnvironment;
import io.toylanguage.datastructure.exception.KeyNotFoundException;
import io.toylanguage.exception.ToyLanguageException;
import io.toylanguage.model.exception.variable.VariableException;
import io.toylanguage.model.exception.variable.specific.UnknownVariableException;
import io.toylanguage.model.expression.Expression;
import io.toylanguage.model.type.Type;
import io.toylanguage.model.value.Value;

public class VariableExpression implements Expression {
    String variableId;

    public VariableExpression(String variableId) {
        this.variableId = variableId;
    }

    @Override
    public Value evaluate(SymbolTable symbolTable, Heap heap) throws VariableException {
        try {
            return symbolTable.get(variableId);
        } catch (KeyNotFoundException exception) {
            throw new UnknownVariableException("Unknown variable %s".formatted(variableId));
        }
    }

    @Override
    public Type typeCheck(TypeEnvironment typeEnvironment) throws ToyLanguageException {
        return typeEnvironment.get(variableId);
    }

    @Override
    public String toString() {
        return "%s".formatted(variableId);
    }
}
