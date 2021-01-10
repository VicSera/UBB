package io.toylanguage.model.statement.implementation;

import io.toylanguage.datastructure.Stack;
import io.toylanguage.datastructure.aliases.ExecutionStack;
import io.toylanguage.datastructure.aliases.TypeEnvironment;
import io.toylanguage.exception.ToyLanguageException;
import io.toylanguage.model.ProgramState;
import io.toylanguage.model.statement.Statement;

public class CompoundStatement implements Statement {
    Statement first;
    Statement second;

    public CompoundStatement(Statement first, Statement second) {
        this.first = first;
        this.second = second;
    }


    @Override
    public ProgramState execute(ProgramState state) {
        ExecutionStack stack = state.getExecutionStack();
        stack.push(second);
        stack.push(first);

        return null;
    }

    @Override
    public TypeEnvironment typeCheck(TypeEnvironment typeEnvironment) throws ToyLanguageException {
        return second.typeCheck(first.typeCheck(typeEnvironment));
    }

    @Override
    public String toString() {
        return "%s\n%s".formatted(first, second);
    }
}
