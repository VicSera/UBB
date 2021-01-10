package io.toylanguage.model.statement.implementation;

import io.toylanguage.datastructure.aliases.TypeEnvironment;
import io.toylanguage.exception.ToyLanguageException;
import io.toylanguage.model.ProgramState;
import io.toylanguage.model.expression.Expression;
import io.toylanguage.model.statement.Statement;
import io.toylanguage.model.type.Type;
import io.toylanguage.model.type.implementation.BoolType;
import io.toylanguage.model.value.Value;
import io.toylanguage.model.value.implementation.BoolValue;

public class IfStatement implements Statement {
    Expression conditionExpression;
    Statement thenStatement;
    Statement elseStatement;

    public IfStatement(Expression conditionExpression, Statement thenStatement, Statement elseStatement) {
        this.conditionExpression = conditionExpression;
        this.thenStatement = thenStatement;
        this.elseStatement = elseStatement;
    }

    @Override
    public ProgramState execute(ProgramState state) throws ToyLanguageException {
        Value conditionResult = conditionExpression.evaluate(state.getSymbolTable(), state.getHeap());
        if (conditionResult.getType().equals(new BoolType())) {
            if (((BoolValue)conditionResult).getValue()) {
                thenStatement.execute(state);
            } else {
                elseStatement.execute(state);
            }
        } else {
            throw new ToyLanguageException("Condition is not a boolean type");
        }

        return null;
    }

    @Override
    public TypeEnvironment typeCheck(TypeEnvironment typeEnvironment) throws ToyLanguageException {
        Type expressionType = conditionExpression.typeCheck(typeEnvironment);
        if (expressionType.equals(new BoolType())) {
            thenStatement.typeCheck(typeEnvironment.deepCopy());
            elseStatement.typeCheck(typeEnvironment.deepCopy());

            return typeEnvironment;
        }
        else
            throw new ToyLanguageException("If statement failed typecheck: condition is not of bool type");
    }

    @Override
    public String toString() {
        return "if (%s) then {%s} else {%s}".formatted(
                conditionExpression, thenStatement, elseStatement
        );
    }
}
