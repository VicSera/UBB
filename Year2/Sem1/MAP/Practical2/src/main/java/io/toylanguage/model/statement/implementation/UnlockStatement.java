package io.toylanguage.model.statement.implementation;

import io.toylanguage.datastructure.LockTable;
import io.toylanguage.datastructure.aliases.SymbolTable;
import io.toylanguage.datastructure.aliases.TypeEnvironment;
import io.toylanguage.exception.ToyLanguageException;
import io.toylanguage.model.ProgramState;
import io.toylanguage.model.statement.Statement;
import io.toylanguage.model.type.implementation.IntType;
import io.toylanguage.model.value.implementation.IntValue;

public class UnlockStatement implements Statement {
    private final String var;

    public UnlockStatement(String var) {
        this.var = var;
    }

    @Override
    public ProgramState execute(ProgramState state) throws ToyLanguageException {
        SymbolTable symbolTable = state.getSymbolTable();
        LockTable lockTable = state.getLockTable();
        int index = ((IntValue)symbolTable.get(var)).getValue();

        synchronized (lockTable) {
            if (!lockTable.containsKey(index))
                throw new ToyLanguageException("The lock table doesn't contain key " + index);

            int val = lockTable.lookup(index);
            if (val == state.getId())
                lockTable.update(index, -1);
        }

        return null;
    }

    @Override
    public TypeEnvironment typeCheck(TypeEnvironment typeEnvironment) throws ToyLanguageException {
        if (typeEnvironment.containsKey(var) && typeEnvironment.get(var).equals(new IntType()))
            return typeEnvironment;
        throw new ToyLanguageException("Unlock failed typecheck: variable is either not declared or not an integer");
    }

    @Override
    public String toString() {
        return "Unlock(" + var + ")";
    }
}
