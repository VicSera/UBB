package io.toylanguage.model.statement.implementation;

import io.toylanguage.datastructure.aliases.ExecutionStack;
import io.toylanguage.datastructure.aliases.SymbolTable;
import io.toylanguage.datastructure.aliases.TypeEnvironment;
import io.toylanguage.exception.ToyLanguageException;
import io.toylanguage.model.ProgramState;
import io.toylanguage.model.statement.Statement;

public class ForkStatement implements Statement {
    private final Statement forkArgument;

    public ForkStatement(Statement statement) {
        forkArgument = statement;
    }

    @Override
    public ProgramState execute(ProgramState state) {
        SymbolTable symbolTableClone = state.getSymbolTable().deepCopy();

        return new ProgramState(
                new ExecutionStack(),
                symbolTableClone,
                state.getOutput(),
                state.getFileTable(),
                state.getHeap(),
                forkArgument
        );
    }

    @Override
    public String toString() {
        return "Fork\n{\n%s\n}".formatted(forkArgument.toString());
    }

    @Override
    public TypeEnvironment typeCheck(TypeEnvironment typeEnvironment) throws ToyLanguageException {
        return forkArgument.typeCheck(typeEnvironment);
    }
}
