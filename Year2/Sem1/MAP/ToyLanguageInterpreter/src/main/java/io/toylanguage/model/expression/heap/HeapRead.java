package io.toylanguage.model.expression.heap;

import io.toylanguage.datastructure.Heap;
import io.toylanguage.datastructure.aliases.SymbolTable;
import io.toylanguage.datastructure.aliases.TypeEnvironment;
import io.toylanguage.exception.ToyLanguageException;
import io.toylanguage.model.expression.Expression;
import io.toylanguage.model.type.Type;
import io.toylanguage.model.type.implementation.RefType;
import io.toylanguage.model.value.Value;
import io.toylanguage.model.value.implementation.RefValue;

public class HeapRead implements Expression {
    private final Expression expression;

    public HeapRead(Expression expression) {
        this.expression = expression;
    }

    @Override
    public Value evaluate(SymbolTable symbolTable, Heap heap) throws ToyLanguageException {
        synchronized (heap) {
            Value value = expression.evaluate(symbolTable, heap);
            if (!(value.getType() instanceof RefType))
                throw new ToyLanguageException("Expression does not evaluate to a Ref type");

            int address = ((RefValue)value).getAddress();
            return heap.get(address);
        }
    }

    @Override
    public Type typeCheck(TypeEnvironment typeEnvironment) throws ToyLanguageException {
        Type type = expression.typeCheck(typeEnvironment);
        if (type instanceof RefType)
            return ((RefType) type).getReferencedType();
        else
            throw new ToyLanguageException("The HeapRead argument is not a RefType");
    }

    @Override
    public String toString() {
        return "HeapRead(%s)".formatted(expression);
    }
}
