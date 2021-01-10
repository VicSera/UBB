package io.toylanguage.model.expression.arithmetic.implementation;

import io.toylanguage.model.expression.Expression;
import io.toylanguage.model.expression.arithmetic.ArithmeticExpression;
import io.toylanguage.model.value.implementation.IntValue;

public class AdditionExpression extends ArithmeticExpression {
    public AdditionExpression(Expression leftExpression, Expression rightExpression) {
        super(leftExpression, rightExpression);
    }

    @Override
    protected IntValue applyOperand(int leftValue, int rightValue) {
        return new IntValue(leftValue + rightValue);
    }

    @Override
    public String toString() {
        return "%s + %s".formatted(leftExpression, rightExpression);
    }
}
