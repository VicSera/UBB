package io.toylanguage.model.statement.implementation;

import io.toylanguage.datastructure.Map;
import io.toylanguage.datastructure.aliases.SymbolTable;
import io.toylanguage.datastructure.aliases.TypeEnvironment;
import io.toylanguage.exception.ToyLanguageException;
import io.toylanguage.model.ProgramState;
import io.toylanguage.model.statement.Statement;
import io.toylanguage.model.type.Type;
import io.toylanguage.model.value.Value;

public class DeclarationStatement implements Statement {
    String name;
    Type type;

    public DeclarationStatement(String name, Type type) {
        this.name = name;
        this.type = type;
    }

    @Override
    public ProgramState execute(ProgramState state) throws ToyLanguageException {
        SymbolTable symbolTable = state.getSymbolTable();

        if (symbolTable.containsKey(name)) {
            throw new ToyLanguageException("Variable redefinition (%s)".formatted(name));
        }

        symbolTable.set(name, type.getDefaultValue());

        return null;
    }

    @Override
    public TypeEnvironment typeCheck(TypeEnvironment typeEnvironment) throws ToyLanguageException {
        typeEnvironment.set(name, type);
        return typeEnvironment;
    }

    @Override
    public String toString() {
        return "%s %s".formatted(type, name);
    }
}
