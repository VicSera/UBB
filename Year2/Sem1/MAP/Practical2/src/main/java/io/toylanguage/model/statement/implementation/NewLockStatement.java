package io.toylanguage.model.statement.implementation;

import io.toylanguage.datastructure.LockTable;
import io.toylanguage.datastructure.aliases.TypeEnvironment;
import io.toylanguage.exception.ToyLanguageException;
import io.toylanguage.model.ProgramState;
import io.toylanguage.model.statement.Statement;
import io.toylanguage.model.type.implementation.IntType;
import io.toylanguage.model.value.implementation.IntValue;

public class NewLockStatement implements Statement {
    private final String var;

    public NewLockStatement(String var) {
        this.var = var;
    }

    @Override
    public ProgramState execute(ProgramState state) throws ToyLanguageException {
        LockTable lockTable = state.getLockTable();
        int location = lockTable.add(-1);
        state.getSymbolTable().set(var, new IntValue(location));

        return null;
    }

    @Override
    public TypeEnvironment typeCheck(TypeEnvironment typeEnvironment) throws ToyLanguageException {
        if (typeEnvironment.containsKey(var) && typeEnvironment.get(var).equals(new IntType()))
            return typeEnvironment;
        throw new ToyLanguageException("NewLock failed typecheck: variable is either not declared or not an integer");
    }

    @Override
    public String toString() {
        return "NewLock(" + var + ")";
    }
}
