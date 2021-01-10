package io.toylanguage.model.statement.implementation;

import io.toylanguage.datastructure.Map;
import io.toylanguage.datastructure.aliases.SymbolTable;
import io.toylanguage.datastructure.aliases.TypeEnvironment;
import io.toylanguage.datastructure.exception.KeyNotFoundException;
import io.toylanguage.exception.ToyLanguageException;
import io.toylanguage.model.ProgramState;
import io.toylanguage.model.expression.Expression;
import io.toylanguage.model.statement.Statement;
import io.toylanguage.model.type.Type;
import io.toylanguage.model.value.Value;

public class AssignmentStatement implements Statement {
    String name;
    Expression expression;

    public AssignmentStatement(String name, Expression expression) {
        this.name = name;
        this.expression = expression;
    }

    @Override
    public ProgramState execute(ProgramState state) throws ToyLanguageException {
        SymbolTable symbolTable = state.getSymbolTable();
        Value newValue = expression.evaluate(symbolTable, state.getHeap());
        Type newType = newValue.getType();

        Value currentValue = getCurrentValue(symbolTable);
        checkType(currentValue.getType(), newType);

        symbolTable.set(name, newValue);
        return null;
    }

    @Override
    public TypeEnvironment typeCheck(TypeEnvironment typeEnvironment) throws ToyLanguageException {
        Type variableType = typeEnvironment.get(name);
        Type expressionType = expression.typeCheck(typeEnvironment);

        if (variableType.equals(expressionType))
            return typeEnvironment;
        else
            throw new ToyLanguageException("Assignment failed typecheck: left and right hand side are of different types");
    }

    private Value getCurrentValue(Map<String, Value> symbolTable) throws ToyLanguageException {
        try {
            return symbolTable.get(name);
        } catch (KeyNotFoundException exception) {
            throw new ToyLanguageException("Variable %s was not declared".formatted(name));
        }
    }

    private void checkType(Type currentType, Type newType) throws ToyLanguageException {
        if (!currentType.equals(newType)) {
            throw new ToyLanguageException("Variable %s - cannot assign %s to %s".formatted(
                    name, newType, currentType
            ));
        }
    }

    @Override
    public String toString() {
        return "%s = %s".formatted(name, expression);
    }
}
