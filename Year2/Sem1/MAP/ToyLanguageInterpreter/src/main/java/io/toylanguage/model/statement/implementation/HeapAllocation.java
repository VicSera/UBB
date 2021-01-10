package io.toylanguage.model.statement.implementation;

import io.toylanguage.datastructure.Heap;
import io.toylanguage.datastructure.aliases.SymbolTable;
import io.toylanguage.datastructure.aliases.TypeEnvironment;
import io.toylanguage.datastructure.exception.KeyNotFoundException;
import io.toylanguage.exception.ToyLanguageException;
import io.toylanguage.model.ProgramState;
import io.toylanguage.model.expression.Expression;
import io.toylanguage.model.statement.Statement;
import io.toylanguage.model.type.Type;
import io.toylanguage.model.type.implementation.RefType;
import io.toylanguage.model.value.Value;
import io.toylanguage.model.value.implementation.RefValue;

public class HeapAllocation implements Statement {
    private final String variableName;
    private final Expression expression;

    public HeapAllocation(String variableName, Expression expression) {
        this.variableName = variableName;
        this.expression = expression;
    }

    @Override
    public ProgramState execute(ProgramState state) throws ToyLanguageException {
        SymbolTable symbolTable = state.getSymbolTable();
        Heap heap = state.getHeap();

        try {
            Value value = symbolTable.get(variableName);
            if (!(value.getType() instanceof RefType))
                throw new ToyLanguageException("Value is not of Ref type");
            RefValue refValue = (RefValue) value;

            Value expressionValue = expression.evaluate(symbolTable, state.getHeap());
            if (!expressionValue.getType().equals(refValue.getReferencedType()))
                throw new ToyLanguageException("Expression result is of type %s. Expected %s".formatted(
                        expressionValue.getType(), value.getType()));

            int newAddress = heap.allocate(expressionValue);
            RefValue newValue = new RefValue(newAddress, expressionValue.getType());

            symbolTable.set(variableName, newValue);
        } catch (KeyNotFoundException exception) {
            throw new ToyLanguageException("Could not find variable with name %s".formatted(variableName));
        }

        return null;
    }

    @Override
    public TypeEnvironment typeCheck(TypeEnvironment typeEnvironment) throws ToyLanguageException {
        Type variableType = typeEnvironment.get(variableName);
        Type expressionType = expression.typeCheck(typeEnvironment);

        if (variableType instanceof RefType) {
            RefType refType = (RefType) variableType;
            if (refType.getReferencedType().equals(expressionType))
                return typeEnvironment;
            else
                throw new ToyLanguageException("Heap allocation failed typecheck: variable and expression have different types");

        }
        else
            throw new ToyLanguageException("Heap allocation failed typecheck: variable is not a RefType");
    }

    @Override
    public String toString() {
        return "new(%s, %s)".formatted(variableName, expression);
    }
}
