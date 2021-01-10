package io.toylanguage.model.statement.implementation;

import io.toylanguage.datastructure.Heap;
import io.toylanguage.datastructure.aliases.SymbolTable;
import io.toylanguage.datastructure.aliases.TypeEnvironment;
import io.toylanguage.exception.ToyLanguageException;
import io.toylanguage.model.ProgramState;
import io.toylanguage.model.expression.Expression;
import io.toylanguage.model.statement.Statement;
import io.toylanguage.model.type.Type;
import io.toylanguage.model.type.implementation.RefType;
import io.toylanguage.model.value.Value;
import io.toylanguage.model.value.implementation.RefValue;

public class HeapWrite implements Statement {
    private final String variableName;
    private final Expression expression;

    public HeapWrite(String variableName, Expression expression) {
        this.variableName = variableName;
        this.expression = expression;
    }

    @Override
    public ProgramState execute(ProgramState state) throws ToyLanguageException {
        SymbolTable symbolTable = state.getSymbolTable();
        Heap heap = state.getHeap();

        if (!symbolTable.containsKey(variableName))
            throw new ToyLanguageException("Could not find symbol %s".formatted(variableName));

        Value value = symbolTable.get(variableName);
        if (!(value.getType() instanceof RefType))
            throw new ToyLanguageException("Value is not of Ref type");

        int address = ((RefValue)value).getAddress();
        if (!heap.containsKey(address))
            throw new ToyLanguageException("The address associated to %s was not found on the heap"
                    .formatted(variableName));

        RefValue refValue = (RefValue) value;
        Value newValue = expression.evaluate(symbolTable, heap);
        if (!newValue.getType().equals(refValue.getReferencedType()))
            throw new ToyLanguageException("The expression evaluated to a different type than what was found on the heap");

        heap.put(address, newValue);

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
                throw new ToyLanguageException("Heap write failed typecheck: variable and expression have different types");

        }
        else
            throw new ToyLanguageException("Heap write failed typecheck: variable is not a RefType");
    }

    @Override
    public String toString() {
        return "HeapWrite(%s, %s)".formatted(variableName, expression);
    }
}
