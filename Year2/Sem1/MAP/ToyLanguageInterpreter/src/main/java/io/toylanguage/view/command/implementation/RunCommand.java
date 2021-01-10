package io.toylanguage.view.command.implementation;

import io.toylanguage.controller.ToyLanguageController;
import io.toylanguage.exception.ToyLanguageException;
import io.toylanguage.view.command.Command;

public class RunCommand extends Command {
    private final ToyLanguageController controller;

    public RunCommand(String key, String description, ToyLanguageController controller) {
        super(key, description);
        this.controller = controller;
    }

    @Override
    public void execute() {
        try {
            controller.execute();
        } catch (ToyLanguageException exception) {
            System.out.printf("%s\n%n", exception.getMessage());
        }
    }
}
