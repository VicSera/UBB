package io.toylanguage.model.expression.relational.implementation;

import io.toylanguage.model.expression.Expression;
import io.toylanguage.model.expression.relational.RelationalExpression;

public class EqualsExpression extends RelationalExpression {
    public EqualsExpression(Expression leftExpression, Expression rightExpression) {
        super(leftExpression, rightExpression);
    }

    @Override
    protected boolean compare(int a, int b) {
        return a == b;
    }

    @Override
    public String toString() {
        return "%s == %s".formatted(leftExpression.toString(), rightExpression.toString());
    }
}