package io.toylanguage.example;

import io.toylanguage.model.statement.Statement;
import io.toylanguage.model.statement.implementation.CompoundStatement;

import java.util.ArrayList;
import java.util.List;

public class StatementBuilder {
    List<Statement> statements = new ArrayList<>();

    public StatementBuilder add(Statement statement) {
        statements.add(statement);
        return this;
    }

    public Statement build() {
        return combineRec(statements, 0);
    }

    private Statement combineRec(List<Statement> statements, int index) {
        if (index == statements.size() - 1)
            return statements.get(index);
        else
            return combine(statements.get(index), combineRec(statements, index + 1));
    }

    private Statement combine(Statement firstStatement, Statement secondStatement) {
        return new CompoundStatement(firstStatement, secondStatement);
    }
}
