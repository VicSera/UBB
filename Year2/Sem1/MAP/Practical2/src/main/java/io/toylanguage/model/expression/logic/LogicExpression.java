package io.toylanguage.model.expression.logic;

import io.toylanguage.datastructure.Heap;
import io.toylanguage.datastructure.Map;
import io.toylanguage.datastructure.aliases.SymbolTable;
import io.toylanguage.datastructure.aliases.TypeEnvironment;
import io.toylanguage.exception.ToyLanguageException;
import io.toylanguage.model.exception.arithmetic.specific.WrongOperandTypeException;
import io.toylanguage.model.expression.Expression;
import io.toylanguage.model.type.Type;
import io.toylanguage.model.type.implementation.BoolType;
import io.toylanguage.model.type.implementation.IntType;
import io.toylanguage.model.value.Value;
import io.toylanguage.model.value.implementation.BoolValue;

public abstract class LogicExpression implements Expression {
    protected Expression leftExpression;
    protected Expression rightExpression;

    public LogicExpression(Expression leftExpression, Expression rightExpression) {
        this.leftExpression = leftExpression;
        this.rightExpression = rightExpression;
    }

    @Override
    public BoolValue evaluate(SymbolTable symbolTable, Heap heap) throws ToyLanguageException {
        Value leftValue = leftExpression.evaluate(symbolTable, heap);
        checkValueTypeAndThrow(leftValue);
        Value rightValue = rightExpression.evaluate(symbolTable, heap);
        checkValueTypeAndThrow(rightValue);

        boolean leftBool = ((BoolValue)leftValue).getValue();
        boolean rightBool = ((BoolValue)rightValue).getValue();

        return applyOperand(leftBool, rightBool);
    }

    @Override
    public Type typeCheck(TypeEnvironment typeEnvironment) throws ToyLanguageException {
        Type type1 = leftExpression.typeCheck(typeEnvironment);
        Type type2 = rightExpression.typeCheck(typeEnvironment);

        if (!type1.equals(new BoolType()))
            throw new ToyLanguageException("First operand is not a bool type");
        if (!type2.equals(new BoolType()))
            throw new ToyLanguageException("Second operand is not a bool type");

        return new BoolType();
    }

    protected abstract BoolValue applyOperand(boolean leftValue, boolean rightValue);

    private void checkValueTypeAndThrow(Value value) throws WrongOperandTypeException {
        if (!value.getType().equals(new BoolType())) {
            throw new WrongOperandTypeException(
                    "Expected %s but got %s".formatted(new IntType().toString(), value.getType().toString()));
        }
    }
}
