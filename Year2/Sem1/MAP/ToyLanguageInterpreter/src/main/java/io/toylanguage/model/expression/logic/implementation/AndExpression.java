package io.toylanguage.model.expression.logic.implementation;

import io.toylanguage.model.expression.Expression;
import io.toylanguage.model.expression.logic.LogicExpression;
import io.toylanguage.model.value.implementation.BoolValue;

public class AndExpression extends LogicExpression {
    public AndExpression(Expression leftExpression, Expression rightExpression) {
        super(leftExpression, rightExpression);
    }

    @Override
    protected BoolValue applyOperand(boolean leftValue, boolean rightValue) {
        return new BoolValue(leftValue && rightValue);
    }

    @Override
    public String toString() {
        return "%s && %s".formatted(leftExpression, rightExpression);
    }
}
