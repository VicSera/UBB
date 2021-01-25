package io.toylanguage.example;

import io.toylanguage.model.expression.arithmetic.implementation.AdditionExpression;
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

        Statement program1 = program1();
        programs.add(new ProgramExample(program1, "1", program1.toString(), "program1"));
        Statement program2 = program2();
        programs.add(new ProgramExample(program2, "2", program2.toString(), "program2"));
        Statement program3 = program3();
        programs.add(new ProgramExample(program3, "3", program3.toString(), "program3"));
        Statement program4 = program4();
        programs.add(new ProgramExample(program4, "4", program4.toString(), "program4"));
        Statement program5 = program5();
        programs.add(new ProgramExample(program5, "5", program5.toString(), "program5"));
        Statement program6 = program6();
        programs.add(new ProgramExample(program6, "6", program6.toString(), "program6"));
        Statement program7 = program7();
        programs.add(new ProgramExample(program7, "7", program7.toString(), "program7"));
        Statement program8 = program8();
        programs.add(new ProgramExample(program8, "8", program8.toString(), "program8"));
        Statement program9 = program9();
        programs.add(new ProgramExample(program9, "9", program9.toString(), "program9"));
        Statement program10 = program10();
        programs.add(new ProgramExample(program10, "10", program10.toString(), "program10"));
        Statement program11 = program11();
        programs.add(new ProgramExample(program11, "11", program11.toString(), "program11"));

        return programs;
    }

    /*
    bool x;
    x = 2;
    Print(x);
     */
    public static Statement program1() {
        return new CompoundStatement(
                new DeclarationStatement("x", new BoolType()),
                new CompoundStatement(
                        new AssignmentStatement("x", new ValueExpression(new IntValue(2))),
                        new PrintStatement(new VariableExpression("x"))
                )
        );
    }

    /*
    int x;
    x = 5;
    bool y;
    y = (false or true) and false;
    if (y) x = 7;
    else x = 6;
    Print(x);
     */
    public static Statement program2() {
        return new CompoundStatement(
                new DeclarationStatement("x", new IntType()),
                new CompoundStatement(
                        new AssignmentStatement("x", new ValueExpression(new IntValue(5))),
                        new CompoundStatement(
                                new DeclarationStatement("y", new BoolType()),
                                new CompoundStatement(
                                        new AssignmentStatement("y", new AndExpression(
                                                new OrExpression(
                                                        new ValueExpression(new BoolValue(false)),
                                                        new ValueExpression(new BoolValue(true))),
                                                new ValueExpression(new BoolValue(false))
                                        )),
                                        new CompoundStatement(
                                                new IfStatement(
                                                        new VariableExpression("y"),
                                                        new AssignmentStatement("x", new ValueExpression(new IntValue(7))),
                                                        new AssignmentStatement("x", new ValueExpression(new IntValue(6)))),
                                                new PrintStatement(new VariableExpression("x"))
                                        )
                                )
                        )
                )
        );
    }

    /*
    int x;
    x = false; <- error
     */
    public static Statement program3() {
        return new CompoundStatement(
                new DeclarationStatement("x", new IntType()),
                new AssignmentStatement("x", new ValueExpression(new BoolValue(false)))
        );
    }

    /*
    int x;
    bool y;
    x = 1;
    y = true;
    Print(x + y);
     */
    public static Statement program4() {
        return new CompoundStatement(
                new DeclarationStatement("x", new IntType()),
                new CompoundStatement(
                        new DeclarationStatement("y", new BoolType()),
                        new CompoundStatement(
                                new AssignmentStatement("x", new ValueExpression(new IntValue(1))),
                                new CompoundStatement(
                                        new AssignmentStatement("y", new ValueExpression(new BoolValue(false))),
                                        new PrintStatement(new AdditionExpression(
                                                new VariableExpression("x"),
                                                new VariableExpression("y")
                                        ))
                                )
                        )
                )
        );
    }

    /*
    string varf;
    varf = "test.in";
    openRFile(varf);
    int varc;
    readFile(varf, varc);
    print(varc);
    readFile(varf, varc);
    print(varc);
    closeRFile(varf);
    */
    public static Statement program5() {
        StatementBuilder builder = new StatementBuilder();
        return builder
                .add(new DeclarationStatement("varf", new StringType()))
                .add(new AssignmentStatement("varf", new ValueExpression(new StringValue("test.in"))))
                .add(new OpenReadFileStatement(new VariableExpression("varf")))
                .add(new DeclarationStatement("varc", new IntType()))
                .add(new ReadFileExpression(new VariableExpression("varf"), "varc"))
                .add(new PrintStatement(new VariableExpression("varc")))
                .add(new ReadFileExpression(new VariableExpression("varf"), "varc"))
                .add(new PrintStatement(new VariableExpression("varc")))
                .add(new CloseReadFileStatement(new VariableExpression("varf")))
                .build();
    }

    /*
    int x;
    x = 5;
    int y;
    y = 10;
    print(x < y);
     */
    public static Statement program6() {
        StatementBuilder builder = new StatementBuilder();
        return builder
                .add(new DeclarationStatement("x", new IntType()))
                .add(new AssignmentStatement("x", new ValueExpression(new IntValue(5))))
                .add(new DeclarationStatement("y", new IntType()))
                .add(new AssignmentStatement("y", new ValueExpression(new IntValue(10))))
                .add(new PrintStatement(new SmallerThanExpression(new VariableExpression("x"), new VariableExpression("y"))))
                .build();
    }

    /*
    Ref int v;
    v = new(int(20));
    Ref ref int a;
    a = new(v);
    v = new(int(30));
    Print(read(read(var("a")));
    */
    public static Statement program7() {
        StatementBuilder builder = new StatementBuilder();
        return builder
                .add(new DeclarationStatement("v", new RefType(new IntType())))
                .add(new HeapAllocation("v", new ValueExpression(new IntValue(20))))
                .add(new DeclarationStatement("a", new RefType(new RefType(new IntType()))))
                .add(new HeapAllocation("a", new VariableExpression("v")))
                .add(new HeapAllocation("v", new ValueExpression(new IntValue(30))))
                .add(new PrintStatement(new HeapRead(new HeapRead(new VariableExpression("a")))))
                .build();
    }

    /*
    Ref int v;
    v = new(int(20));
    print(var("v"))
    write("v", int(30));
    Print(read(var("v")) + int(5));
     */
    public static Statement program8() {
        return new StatementBuilder()
                .add(new DeclarationStatement("v", new RefType(new IntType())))
                .add(new HeapAllocation("v", new ValueExpression(new IntValue(20))))
                .add(new PrintStatement(new HeapRead(new VariableExpression("v"))))
                .add(new HeapWrite("v", new ValueExpression(new IntValue(30))))
                .add(new PrintStatement(new AdditionExpression(
                        new HeapRead(new VariableExpression("v")),
                        new ValueExpression(new IntValue(5))
                )))
                .build();
    }

    /*
    int i;
    while (i != int(10))
        i = i + int(1)
     */
    public static Statement program9() {
        return new StatementBuilder()
                .add(new DeclarationStatement("i", new IntType()))
                .add(new WhileStatement(
                        new NotEqualsExpression(
                                new VariableExpression("i"),
                                new ValueExpression(new IntValue(10))),
                        new AssignmentStatement("i", new AdditionExpression(
                                new VariableExpression("i"), new ValueExpression(new IntValue(1))
                        ))))
                .build();
    }

    public static Statement program10() {
        return new StatementBuilder()
                .add(new DeclarationStatement("v", new IntType()))
                .add(new DeclarationStatement("a", new RefType(new IntType())))
                .add(new AssignmentStatement("v", new ValueExpression(new IntValue(10))))
                .add(new HeapAllocation("a", new ValueExpression(new IntValue(22))))
                .add(new ForkStatement(
                        new StatementBuilder()
                                .add(new HeapWrite("a", new ValueExpression(new IntValue(30))))
                                .add(new AssignmentStatement("v", new ValueExpression(new IntValue(32))))
                                .add(new PrintStatement(new VariableExpression("v")))
                                .add(new PrintStatement(new HeapRead(new VariableExpression("a"))))
                                .build()
                ))
                .add(new PrintStatement(new VariableExpression("v")))
                .add(new PrintStatement(new HeapRead(new VariableExpression("a"))))
                .build();
    }

    public static Statement program11() {
        return new StatementBuilder()
                .add(new DeclarationStatement("i", new IntType()))
                .add(new DeclarationStatement("v", new RefType(new IntType())))
                .add(new HeapAllocation("v", new ValueExpression(new IntValue(0))))
                .add(new WhileStatement(
                        new SmallerThanExpression(new VariableExpression("i"), new ValueExpression(new IntValue(10))),
                        new StatementBuilder()
                                .add(new AssignmentStatement("i",
                                        new AdditionExpression(new VariableExpression("i"), new ValueExpression(new IntValue(1)))))
                                .add(new ForkStatement(
                                        new StatementBuilder()
                                                .add(new HeapWrite("v",
                                                        new AdditionExpression(
                                                                new HeapRead(new VariableExpression("v")),
                                                                new ValueExpression(new IntValue(1))
                                                        )))
                                                .add(new HeapWrite("v",
                                                        new AdditionExpression(
                                                                new HeapRead(new VariableExpression("v")),
                                                                new ValueExpression(new IntValue(1))
                                                        )))
                                                .add(new HeapWrite("v",
                                                        new AdditionExpression(
                                                                new HeapRead(new VariableExpression("v")),
                                                                new ValueExpression(new IntValue(1))
                                                        )))
                                                .add(new HeapWrite("v",
                                                        new AdditionExpression(
                                                                new HeapRead(new VariableExpression("v")),
                                                                new ValueExpression(new IntValue(1))
                                                        )))
                                                .add(new HeapWrite("v",
                                                        new AdditionExpression(
                                                                new HeapRead(new VariableExpression("v")),
                                                                new ValueExpression(new IntValue(1))
                                                        )))
                                                .build()
                                ))
                                .build()
                ))
                .build();
    }
}
