package io.toylanguage.repository;

import io.toylanguage.exception.ToyLanguageException;
import io.toylanguage.model.ProgramState;
import io.toylanguage.model.statement.Statement;

import java.util.List;

public interface ProgramStateRepository {
    void setStartingProgram(Statement program) throws ToyLanguageException;

    List<ProgramState> getPrograms();

    void setPrograms(List<ProgramState> programs);

    void logProgramState(ProgramState programState) throws ToyLanguageException;

    void setLogFilePath(String logFilePath) throws ToyLanguageException;
}
