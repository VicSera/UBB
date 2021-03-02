package io.toylanguage.example;

import io.toylanguage.model.expression.arithmetic.implementation.AdditionExpression;
import io.toylanguage.model.expression.arithmetic.implementation.MultiplicationExpression;
import io.toylanguage.model.expression.heap.HeapRead;
import io.toylanguage.model.expression.logic.implementation.AndExpression;
import io.toylanguage.model.expression.logic.implementation.OrExpression;
import io.toylanguage.model.expression.relational.implementation.NotEqualsExpression;
import io.toylanguage.model.expression.relational.implementation.SmallerThanExpression;
import io.toylanguage.model.expression.value.ValueExpression;
import io.toylanguage.model.expression.variable.VariableExpression;
import io.toylanguage.model.statement.Statement;
import io.toylanguage.model.statement.implementation.*;
import io.toylanguage.model.type.implementation.BoolType;
import io.toylanguage.model.type.implementation.IntType;
import io.toylanguage.model.type.implementation.RefType;
import io.toylanguage.model.type.implementation.StringType;
import io.toylanguage.model.value.implementation.BoolValue;
import io.toylanguage.model.value.implementation.IntValue;
import io.toylanguage.model.value.implementation.StringValue;
import javafx.stage.Stage;

import java.util.ArrayList;
import java.util.List;

public class ProgramExampleFactory {
    public static List<ProgramExample> getAllPrograms() {
        List<ProgramExample> programs = new ArrayList<>();

        Statement programFor = programFor();
        programs.add(new ProgramExample(programFor, "1", programFor.toString(), "programFor"));
        Statement programFor2 = programFor2();
        programs.add(new ProgramExample(programFor2, "2", programFor2.toString(), "programFor2"));

        return programs;
    }

//    A test program
    public static Statement programFor() {
        return new StatementBuilder()
                .add(new ForStatement(
                        "i", new ValueExpression(new IntValue(0)),
                        new ValueExpression(new IntValue(10)),
                        new AdditionExpression(new VariableExpression("i"), new ValueExpression(new IntValue(1))),
                        new PrintStatement(new VariableExpression("i"))
                ))
                .build();
    }

//    Ref int a; new(a,20);
//(for(v=0;v<3;v=v+1) fork(print(v);v=v*rh(a)));
//    print(rh(a))
//    The final Out should be {0,1,2,20}
    public static Statement programFor2() {
        return new StatementBuilder()
                .add(new DeclarationStatement("a", new RefType(new IntType())))
                .add(new HeapAllocation("a", new ValueExpression(new IntValue(20))))
                .add(new ForStatement(
                        "v", new ValueExpression(new IntValue(0)),
                        new ValueExpression(new IntValue(3)),
                        new AdditionExpression(new VariableExpression("v"), new ValueExpression(new IntValue(1))),
                        new ForkStatement(
                                new StatementBuilder()
                                        .add(new PrintStatement(new VariableExpression("v")))
                                        .add(new AssignmentStatement("v", new MultiplicationExpression(
                                                new VariableExpression("v"),
                                                new HeapRead(new VariableExpression("a"))
                                        )))
                                        .build())
                ))
                .add(new PrintStatement(new HeapRead(new VariableExpression("a"))))
                .build();
    }
}
