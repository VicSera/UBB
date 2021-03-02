package io.toylanguage.example;

import io.toylanguage.model.statement.Statement;

public class ProgramExample {
    private final Statement program;
    private final String key;
    private final String description;
    private final String logFile;

    public ProgramExample(Statement program, String key, String description, String logFile) {
        this.program = program;
        this.key = key;
        this.description = description;
        this.logFile = logFile;
    }

    public Statement getProgram() {
        return program;
    }

    public String getKey() {
        return key;
    }

    public String getDescription() {
        return description;
    }

    public String getLogFile() {
        return logFile;
    }
}
