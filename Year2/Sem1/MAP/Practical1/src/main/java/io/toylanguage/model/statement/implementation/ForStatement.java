package io.toylanguage.model.statement.implementation;

import io.toylanguage.datastructure.aliases.TypeEnvironment;
import io.toylanguage.exception.ToyLanguageException;
import io.toylanguage.model.ProgramState;
import io.toylanguage.model.expression.Expression;
import io.toylanguage.model.expression.relational.implementation.SmallerThanExpression;
import io.toylanguage.model.expression.variable.VariableExpression;
import io.toylanguage.model.statement.Statement;
import io.toylanguage.model.type.implementation.IntType;

//Define the new statement:
//        for(v=exp1;v<exp2;v=exp3) stmt
//        Its execution on the ExeStack is the following:
//        - pop the statement
//        - create the following statement:
//        int v; v=exp1;(while(v<exp2) stmt;v=exp3)
//        - push the new statement on the stack
//        The typecheck method of for statement verifies if exp1, exp2, and exp3 have  	the type

public class ForStatement implements Statement {
    private final String v;
    private final Expression exp1;
    private final Expression exp2;
    private final Expression exp3;
    private final Statement body;

    public ForStatement(String v, Expression exp1, Expression exp2, Expression exp3, Statement body) {
        this.v = v;
        this.exp1 = exp1;
        this.exp2 = exp2;
        this.exp3 = exp3;
        this.body = body;
    }

    @Override
    public ProgramState execute(ProgramState state) throws ToyLanguageException {
        Statement comp = new CompoundStatement(
                new DeclarationStatement(v, new IntType()),
                new CompoundStatement(
                        new AssignmentStatement(v, exp1),
                        new WhileStatement(
                                new SmallerThanExpression(new VariableExpression(v), exp2),
                                new CompoundStatement(
                                        body,
                                        new AssignmentStatement(v, exp3)))
                )
        );

        state.getExecutionStack().push(comp);
        return null;
    }

    @Override
    public TypeEnvironment typeCheck(TypeEnvironment typeEnvironment) throws ToyLanguageException {
        TypeEnvironment typeEnvironmentCopy = typeEnvironment.deepCopy();
        typeEnvironmentCopy.set(v, new IntType());
        if (exp1.typeCheck(typeEnvironmentCopy).equals(new IntType()) &&
                exp2.typeCheck(typeEnvironmentCopy).equals(new IntType()) &&
                exp3.typeCheck(typeEnvironmentCopy).equals(new IntType())) {
            body.typeCheck(typeEnvironmentCopy.deepCopy());
            return typeEnvironment;
        }
        else {
            throw new ToyLanguageException("For statement failed typecheck. At least one expression does not evaluate to an int type");
        }
    }

    @Override
    public String toString() {
        return "For(int " + v + "=" + exp1 + "; " + v + "<" + exp2 + "; " + v + "=" + exp3 + ") { " + body + " }";
    }
}
