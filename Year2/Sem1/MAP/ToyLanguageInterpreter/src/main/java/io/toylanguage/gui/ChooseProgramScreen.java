package io.toylanguage.gui;

import io.toylanguage.example.ProgramExample;
import io.toylanguage.example.ProgramExampleFactory;
import javafx.collections.FXCollections;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.ListView;
import javafx.stage.Stage;

import java.util.stream.Collectors;

public class ChooseProgramScreen {
    public Button confirmChoiceButton;
    public ListView<String> programList;

    @FXML
    public void initialize() {
        initializeProgramList();
        initializeConfirmButton();
    }

    private void initializeProgramList() {
        programList.setItems(FXCollections.observableArrayList(
                ProgramExampleFactory.getAllPrograms().stream()
                .map(programExample -> programExample.getKey() + ")\n" + programExample.getDescription())
                .collect(Collectors.toList())
        ));
    }

    private void initializeConfirmButton() {
        confirmChoiceButton.setOnAction((actionEvent -> {
            int programIndex = programList.getSelectionModel().getSelectedIndex();

            Stage stage = (Stage) confirmChoiceButton.getScene().getWindow();
            stage.close();

            MainScreen mainScreen = Controllers.MAIN_SCREEN;
            mainScreen.programPicked(programIndex);
        }));
    }
}
