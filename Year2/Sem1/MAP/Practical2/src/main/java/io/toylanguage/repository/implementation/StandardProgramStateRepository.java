package io.toylanguage.repository.implementation;

import io.toylanguage.datastructure.aliases.*;
import io.toylanguage.datastructure.implementation.StandardHeap;
import io.toylanguage.datastructure.implementation.StandardLockTable;
import io.toylanguage.exception.ToyLanguageException;
import io.toylanguage.logger.Logger;
import io.toylanguage.model.ProgramState;
import io.toylanguage.model.statement.Statement;
import io.toylanguage.repository.ProgramStateRepository;

import java.util.ArrayList;
import java.util.List;

public class StandardProgramStateRepository implements ProgramStateRepository {
    private List<ProgramState> programStates = new ArrayList<>();
    private Logger logger;

    public StandardProgramStateRepository(Statement program, String logFilePath) throws ToyLanguageException {
        setStartingProgram(program);
        this.logger = new Logger(logFilePath);
    }

    public StandardProgramStateRepository() {
        this.logger = new Logger();
    }

    @Override
    public void setStartingProgram(Statement program) {
        programStates.clear();
        programStates.add(new ProgramState(
                new ExecutionStack(),
                new SymbolTable(),
                new OutputList(),
                new FileTable(),
                new StandardHeap(),
                new StandardLockTable(),
                program
        ));
    }

    @Override
    public List<ProgramState> getPrograms() {
        return programStates;
    }

    @Override
    public void setPrograms(List<ProgramState> programs) {
        programStates = programs;
    }

    @Override
    public void logProgramState(ProgramState programState) throws ToyLanguageException {
        logger.logProgramState(programState);
    }

    @Override
    public void setLogFilePath(String logFilePath) throws ToyLanguageException {
        this.logger = new Logger(logFilePath);
    }
}
