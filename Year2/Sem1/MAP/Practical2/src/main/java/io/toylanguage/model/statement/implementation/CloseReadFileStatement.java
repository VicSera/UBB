package io.toylanguage.model.statement.implementation;

import io.toylanguage.datastructure.Heap;
import io.toylanguage.datastructure.Map;
import io.toylanguage.datastructure.aliases.FileTable;
import io.toylanguage.datastructure.aliases.SymbolTable;
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
import java.io.IOException;

public class CloseReadFileStatement implements Statement {
    private final Expression expression;

    public CloseReadFileStatement(Expression expression) {
        this.expression = expression;
    }

    @Override
    public ProgramState execute(ProgramState state) throws ToyLanguageException {
        SymbolTable symbolTable = state.getSymbolTable();
        FileTable fileTable = state.getFileTable();

        String fileName = getStringFromExpression(expression, symbolTable, state.getHeap());
        BufferedReader reader = getBufferedReaderFromString(fileName, fileTable);

        try {
            reader.close();
            fileTable.removeKey(fileName);
        } catch (IOException exception) {
            throw new ToyLanguageException("An IOException occured when trying to close file %s".formatted(fileName));
        }

        return null;
    }

    @Override
    public TypeEnvironment typeCheck(TypeEnvironment typeEnvironment) throws ToyLanguageException {
        Type expressionType = expression.typeCheck(typeEnvironment);
        if (expressionType.equals(new StringType()))
            return typeEnvironment;
        else
            throw new ToyLanguageException("Read file failed typecheck: expression is not a string");
    }

    private BufferedReader getBufferedReaderFromString(String fileName, FileTable fileTable) throws ToyLanguageException {
        if (!fileTable.containsKey(fileName)) {
            throw new ToyLanguageException("File %s is not open".formatted(fileName));
        }

        return fileTable.get(fileName);
    }

    private String getStringFromExpression(Expression expression, SymbolTable symbolTable, Heap heap) throws ToyLanguageException {
        Value value = expression.evaluate(symbolTable, heap);

        if (!value.getType().equals(new StringType())) {
            throw new ToyLanguageException("Expression does not evaluate to a string type");
        }

        return ((StringValue)value).getValue();
    }

    @Override
    public String toString() {
        return "Close(%s)".formatted(expression.toString());
    }
}
