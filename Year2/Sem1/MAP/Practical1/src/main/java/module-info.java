module ToyLanguageInterpreter {
    requires javafx.fxml;
    requires javafx.controls;
    requires javafx.graphics;
    requires javafx.base;

    opens io.toylanguage.gui;
    opens io.toylanguage.gui.models;
}
