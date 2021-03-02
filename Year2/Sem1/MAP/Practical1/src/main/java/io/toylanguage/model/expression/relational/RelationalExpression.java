package io.toylanguage.model.expression.relational;

import io.toylanguage.datastructure.Heap;
import io.toylanguage.datastructure.Map;
import io.toylanguage.datastructure.aliases.SymbolTable;
import io.toylanguage.datastructure.aliases.TypeEnvironment;
import io.toylanguage.exception.ToyLanguageException;
import io.toylanguage.model.expression.Expression;
import io.toylanguage.model.type.Type;
import io.toylanguage.model.type.implementation.BoolType;
import io.toylanguage.model.type.implementation.IntType;
import io.toylanguage.model.value.Value;
import io.toylanguage.model.value.implementation.BoolValue;
import io.toylanguage.model.value.implementation.IntValue;

public abstract class RelationalExpression implements Expression {
    protected final Expression leftExpression;
    protected final Expression rightExpression;

    public RelationalExpression(Expression leftExpression, Expression rightExpression) {
        this.leftExpression = leftExpression;
        this.rightExpression = rightExpression;
    }

    @Override
    public Value evaluate(SymbolTable symbolTable, Heap heap) throws ToyLanguageException {
        IntValue leftValue = getIntValueFromExpression(leftExpression, symbolTable, heap);
        IntValue rightValue = getIntValueFromExpression(rightExpression, symbolTable, heap);

        return new BoolValue(compare(leftValue.getValue(), rightValue.getValue()));
    }

    @Override
    public Type typeCheck(TypeEnvironment typeEnvironment) throws ToyLanguageException {
        Type type1 = leftExpression.typeCheck(typeEnvironment);
        Type type2 = rightExpression.typeCheck(typeEnvironment);

        if (!type1.equals(new IntType()))
            throw new ToyLanguageException("First operand is not an int type");
        if (!type2.equals(new IntType()))
            throw new ToyLanguageException("Second operand is not an int type");

        return new BoolType();
    }

    private IntValue getIntValueFromExpression(Expression expression, SymbolTable symbolTable, Heap heap) throws ToyLanguageException {
        Value value = expression.evaluate(symbolTable, heap);
        if (!value.getType().equals(new IntType())) {
            throw new ToyLanguageException("Expression does not evaluate to an int");
        }

        return (IntValue)value;
    }

    protected abstract boolean compare(int a, int b);
}
