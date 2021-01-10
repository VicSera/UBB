package io.toylanguage.model.expression.relational.implementation;

import io.toylanguage.model.expression.Expression;
import io.toylanguage.model.expression.relational.RelationalExpression;

public class GreaterOrEqualExpression extends RelationalExpression {
    public GreaterOrEqualExpression(Expression leftExpression, Expression rightExpression) {
        super(leftExpression, rightExpression);
    }

    @Override
    protected boolean compare(int a, int b) {
        return a >= b;
    }

    @Override
    public String toString() {
        return "%s >= %s".formatted(leftExpression.toString(), rightExpression.toString());
    }
}
