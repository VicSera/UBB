package io.toylanguage.model.statement;

import io.toylanguage.datastructure.aliases.TypeEnvironment;
import io.toylanguage.exception.ToyLanguageException;
import io.toylanguage.model.ProgramState;

public interface Statement {
    ProgramState execute(ProgramState state) throws ToyLanguageException;

    TypeEnvironment typeCheck(TypeEnvironment typeEnvironment) throws ToyLanguageException;
}
