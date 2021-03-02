package io.toylanguage.model.expression.arithmetic;

import io.toylanguage.datastructure.Heap;
import io.toylanguage.datastructure.Map;
import io.toylanguage.datastructure.aliases.SymbolTable;
import io.toylanguage.datastructure.aliases.TypeEnvironment;
import io.toylanguage.exception.ToyLanguageException;
import io.toylanguage.model.exception.arithmetic.specific.DivisonByZeroException;
import io.toylanguage.model.exception.arithmetic.specific.WrongOperandTypeException;
import io.toylanguage.model.expression.Expression;
import io.toylanguage.model.type.Type;
import io.toylanguage.model.type.implementation.IntType;
import io.toylanguage.model.value.Value;
import io.toylanguage.model.value.implementation.IntValue;

public abstract class ArithmeticExpression implements Expression {
    protected Expression leftExpression;
    protected Expression rightExpression;

    public ArithmeticExpression(Expression leftExpression, Expression rightExpression) {
        this.leftExpression = leftExpression;
        this.rightExpression = rightExpression;
    }

    @Override
    public IntValue evaluate(SymbolTable symbolTable, Heap heap) throws ToyLanguageException {
        Value leftValue = leftExpression.evaluate(symbolTable, heap);
        checkValueTypeAndThrow(leftValue);
        Value rightValue = rightExpression.evaluate(symbolTable, heap);
        checkValueTypeAndThrow(rightValue);

        int leftInt = ((IntValue)leftValue).getValue();
        int rightInt = ((IntValue)rightValue).getValue();

        return applyOperand(leftInt, rightInt);
    }

    @Override
    public Type typeCheck(TypeEnvironment typeEnvironment) throws ToyLanguageException {
        Type type1 = leftExpression.typeCheck(typeEnvironment);
        Type type2 = rightExpression.typeCheck(typeEnvironment);

        if (!type1.equals(new IntType()))
            throw new ToyLanguageException("First operand is not an int type");
        if (!type2.equals(new IntType()))
            throw new ToyLanguageException("Second operand is not an int type");

        return new IntType();
    }

    protected abstract IntValue applyOperand(int leftValue, int rightValue) throws DivisonByZeroException;

    private void checkValueTypeAndThrow(Value value) throws WrongOperandTypeException {
        if (!value.getType().equals(new IntType())) {
            throw new WrongOperandTypeException(
                    "Expected %s but got %s".formatted(new IntType().toString(), value.getType().toString()));
        }
    }
}
