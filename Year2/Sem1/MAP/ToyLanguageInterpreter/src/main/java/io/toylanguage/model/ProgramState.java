package io.toylanguage.model;

import io.toylanguage.datastructure.Heap;
import io.toylanguage.datastructure.Stack;
import io.toylanguage.datastructure.aliases.*;
import io.toylanguage.exception.ToyLanguageException;
import io.toylanguage.model.statement.Statement;

public class ProgramState {
    private static Integer nextId = 1;
    synchronized private static Integer getNextId() {
        return nextId++;
    }

    private final Integer id = getNextId();
    private final ExecutionStack executionStack;
    private final SymbolTable symbolTable;
    private final OutputList output;
    private final FileTable fileTable;
    private final Heap heap;

    public Integer getId() {
        return id;
    }

    public ProgramState(
            ExecutionStack executionStack,
            SymbolTable symbolTable,
            OutputList output,
            FileTable fileTable,
            Heap heap,
            Statement program
    ) {
        this.executionStack = executionStack;
        this.symbolTable = symbolTable;
        this.output = output;
        this.fileTable = fileTable;
        this.heap = heap;
        this.executionStack.push(program);
    }

    public ExecutionStack getExecutionStack() {
        return executionStack;
    }

    public SymbolTable getSymbolTable() {
        return symbolTable;
    }

    public OutputList getOutput() {
        return output;
    }

    public FileTable getFileTable() {
        return fileTable;
    }

    public Heap getHeap() {
        return heap;
    }

    public Boolean isFinished() {
        return executionStack.isEmpty();
    }

    public ProgramState step() throws ToyLanguageException {
        if (executionStack.isEmpty()) {
            throw new ToyLanguageException("Execution stack is empty");
        }

        Statement statement = executionStack.pop();
        return statement.execute(this);
    }

    @Override
    public String toString() {
        return "Program %s\nExecution stack:%sSymbol table:%sOutput:%sHeap:%s".formatted(
                id, executionStack, symbolTable, output, heap);
    }
}
