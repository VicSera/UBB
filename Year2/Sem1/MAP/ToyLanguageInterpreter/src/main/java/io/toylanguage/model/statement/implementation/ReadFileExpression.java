package io.toylanguage.model.statement.implementation;

import io.toylanguage.datastructure.Map;
import io.toylanguage.datastructure.aliases.FileTable;
import io.toylanguage.datastructure.aliases.SymbolTable;
import io.toylanguage.datastructure.aliases.TypeEnvironment;
import io.toylanguage.exception.ToyLanguageException;
import io.toylanguage.model.ProgramState;
import io.toylanguage.model.expression.Expression;
import io.toylanguage.model.statement.Statement;
import io.toylanguage.model.type.Type;
import io.toylanguage.model.type.implementation.IntType;
import io.toylanguage.model.type.implementation.StringType;
import io.toylanguage.model.value.Value;
import io.toylanguage.model.value.implementation.IntValue;
import io.toylanguage.model.value.implementation.StringValue;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class ReadFileExpression implements Statement {
    private final Expression expression;
    private final String variableName;

    public ReadFileExpression(Expression expression, String variableName) {
        this.expression = expression;
        this.variableName = variableName;
    }

    @Override
    public ProgramState execute(ProgramState state) throws ToyLanguageException {
        SymbolTable symbolTable = state.getSymbolTable();
        FileTable fileTable = state.getFileTable();

        if (!symbolTable.containsKey(variableName)) {
            throw new ToyLanguageException("Variable %s wasn't declared".formatted(variableName));
        }

        Value fileName = expression.evaluate(symbolTable, state.getHeap());

        if (!fileName.getType().equals(new StringType())) {
            throw new ToyLanguageException("Expression does not evaluate to a string type");
        }

        String fileNameString = ((StringValue)fileName).getValue();
        BufferedReader reader = getBufferedReader(fileNameString, fileTable);
        String line = getLineFromReader(reader);
        int value = getIntFromString(line);
        symbolTable.set(variableName, new IntValue(value));

        return null;
    }

    @Override
    public TypeEnvironment typeCheck(TypeEnvironment typeEnvironment) throws ToyLanguageException {
        Type expressionType = expression.typeCheck(typeEnvironment);
        Type variableType = typeEnvironment.get(variableName);

        if (!variableType.equals(new IntType()))
            throw new ToyLanguageException("Read file failed typecheck: variable is not an int");
        if (!expressionType.equals(new StringType()))
            throw new ToyLanguageException("Read file failed typecheck: expression is not a string");

        return typeEnvironment;
    }

    private int getIntFromString(String line) throws ToyLanguageException {
        if (line == null) {
            return 0;
        }

        try {
            return Integer.parseInt(line);
        } catch (NumberFormatException exception) {
            throw new ToyLanguageException("The line from the file could not be converted to an integer");
        }
    }

    private String getLineFromReader(BufferedReader reader) throws ToyLanguageException {
        try {
            return reader.readLine();
        } catch (IOException ioException) {
            throw new ToyLanguageException("An IOException occurred when reading from the file");
        }
    }

    private BufferedReader getBufferedReader(String fileNameString, FileTable fileTable) throws ToyLanguageException {
        if (!fileTable.containsKey(fileNameString)) {
            throw new ToyLanguageException("File %s is not open".formatted(fileNameString));
        }

        return fileTable.get(fileNameString);
    }

    @Override
    public String toString() {
        return "Read(%s, %s)".formatted(expression, variableName);
    }
}
