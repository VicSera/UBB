package io.toylanguage.model.statement.implementation;

import io.toylanguage.datastructure.List;
import io.toylanguage.datastructure.aliases.OutputList;
import io.toylanguage.datastructure.aliases.TypeEnvironment;
import io.toylanguage.exception.ToyLanguageException;
import io.toylanguage.model.ProgramState;
import io.toylanguage.model.expression.Expression;
import io.toylanguage.model.expression.variable.VariableExpression;
import io.toylanguage.model.statement.Statement;
import io.toylanguage.model.value.Value;

public class PrintStatement implements Statement {
    Expression expression;

    public PrintStatement(Expression expression) {
        this.expression = expression;
    }

    @Override
    public ProgramState execute(ProgramState state) throws ToyLanguageException {
        OutputList output = state.getOutput();
        Value value = expression.evaluate(state.getSymbolTable(), state.getHeap());

        output.add(value);

        return null;
    }

    @Override
    public TypeEnvironment typeCheck(TypeEnvironment typeEnvironment) throws ToyLanguageException {
        expression.typeCheck(typeEnvironment);
        return typeEnvironment;
    }

    @Override
    public String toString() {
        return "Print(%s)".formatted(expression);
    }
}
