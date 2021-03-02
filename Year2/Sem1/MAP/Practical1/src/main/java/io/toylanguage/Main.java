package io.toylanguage;

import io.toylanguage.controller.ToyLanguageController;
import io.toylanguage.datastructure.aliases.TypeEnvironment;
import io.toylanguage.example.ProgramExample;
import io.toylanguage.example.ProgramExampleFactory;
import io.toylanguage.exception.ToyLanguageException;
import io.toylanguage.gui.ToyLanguageInterpreterWithGUI;
import io.toylanguage.repository.ProgramStateRepository;
import io.toylanguage.repository.implementation.StandardProgramStateRepository;
import io.toylanguage.view.command.implementation.ExitCommand;
import io.toylanguage.view.command.implementation.RunCommand;
import io.toylanguage.view.menu.TextMenu;
import javafx.application.Application;

public class Main {
    public static void main(String[] args) {
        TextMenu textMenu = new TextMenu();

        ExitCommand exitCommand = new ExitCommand("0", "exit");
        textMenu.addCommand(exitCommand);

        for (ProgramExample programExample : ProgramExampleFactory.getAllPrograms()) {
            try {
                programExample.getProgram().typeCheck(new TypeEnvironment());
                ProgramStateRepository repository = new StandardProgramStateRepository(
                        programExample.getProgram(), programExample.getLogFile());
                ToyLanguageController controller = new ToyLanguageController(repository);
                RunCommand command = new RunCommand(programExample.getKey(), programExample.getDescription(), controller);

                textMenu.addCommand(command);
            } catch (ToyLanguageException exception) {
                System.out.printf("Program %s failed: %s\n", programExample.getKey(), exception.getMessage());
            }
        }

        textMenu.show();
    }
}
