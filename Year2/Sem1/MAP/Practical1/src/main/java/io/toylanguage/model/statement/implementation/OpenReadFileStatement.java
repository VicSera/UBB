package io.toylanguage.model.statement.implementation;

import io.toylanguage.datastructure.Map;
import io.toylanguage.datastructure.aliases.FileTable;
import io.toylanguage.datastructure.aliases.TypeEnvironment;
import io.toylanguage.exception.ToyLanguageException;
import io.toylanguage.model.ProgramState;
import io.toylanguage.model.expression.Expression;
import io.toylanguage.model.statement.Statement;
import io.toylanguage.model.type.Type;
import io.toylanguage.model.type.implementation.StringType;
import io.toylanguage.model.value.Value;
import io.toylanguage.model.value.implementation.StringValue;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;

public class OpenReadFileStatement implements Statement {
    private Expression expression;

    public OpenReadFileStatement(Expression expression) {
        this.expression = expression;
    }

    @Override
    public ProgramState execute(ProgramState state) throws ToyLanguageException {
        FileTable fileTable = state.getFileTable();

        Value fileName = expression.evaluate(state.getSymbolTable(), state.getHeap());
        if (!fileName.getType().equals(new StringType())) {
            throw new ToyLanguageException("Expression does not evaluate to a string");
        }

        String fileNameString = ((StringValue)fileName).getValue();

        if (fileTable.containsKey(fileNameString)) {
            throw new ToyLanguageException("File with name %s is already open".formatted(fileNameString));
        }

        BufferedReader fileDescriptor = createBufferedReader(fileNameString);

        fileTable.set(fileNameString, fileDescriptor);

        return null;
    }

    @Override
    public TypeEnvironment typeCheck(TypeEnvironment typeEnvironment) throws ToyLanguageException {
        Type type = expression.typeCheck(typeEnvironment);

        if (type.equals(new StringType()))
            return typeEnvironment;
        else
            throw new ToyLanguageException("Open file failed typecheck: expression is not a string");
    }

    private BufferedReader createBufferedReader(String fileNameString) throws ToyLanguageException {
        try {
            return new BufferedReader(new FileReader(fileNameString));
        } catch (FileNotFoundException fileNotFoundException) {
            throw new ToyLanguageException("File %s could not be opened".formatted(fileNameString));
        }
    }

    @Override
    public String toString() {
        return "Open(%s)".formatted(expression);
    }
}
