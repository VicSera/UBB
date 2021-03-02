package io.toylanguage.logger;

import io.toylanguage.config.Config;
import io.toylanguage.exception.ToyLanguageException;
import io.toylanguage.model.ProgramState;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;

public class Logger {
    OutputStream output;

    public Logger() {
        output = System.out;
    }

    public Logger(OutputStream output) {
        this.output = output;
    }

    public Logger(String logFilePath) throws ToyLanguageException {
        try {
            this.output = new FileOutputStream(logFilePath);
        } catch (FileNotFoundException fileNotFoundException) {
            throw new ToyLanguageException("IO exception");
        }
    }

    public void logProgramState(ProgramState state) throws ToyLanguageException {
        if (Config.DISPLAY_PROGRAM_STATE) {
            try {
                output.write(state.toString().getBytes());
                output.write("-------------------------------\n".getBytes());
            } catch (IOException ioException) {
                throw new ToyLanguageException("An IOException occured while logging the program state");
            }
        }
    }

    public void logError(ToyLanguageException exception) throws ToyLanguageException {
        try {
            output.write(exception.getMessage().getBytes());
        } catch (IOException ioException) {
            throw new ToyLanguageException("An IOException occured while logging another error");
        }
    }
}
