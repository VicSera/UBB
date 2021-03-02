package io.toylanguage.gui;

import io.toylanguage.controller.ToyLanguageController;
import io.toylanguage.datastructure.aliases.TypeEnvironment;
import io.toylanguage.example.ProgramExample;
import io.toylanguage.example.ProgramExampleFactory;
import io.toylanguage.exception.ToyLanguageException;
import io.toylanguage.gui.models.ReferenceModel;
import io.toylanguage.gui.models.SymbolModel;
import io.toylanguage.model.ProgramState;
import io.toylanguage.model.value.Value;
import io.toylanguage.repository.implementation.StandardProgramStateRepository;
import javafx.beans.InvalidationListener;
import javafx.beans.Observable;
import javafx.collections.FXCollections;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.ListView;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.stage.Stage;

import java.io.IOException;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class MainScreen implements InvalidationListener {
    public Button chooseProgramButton;

    public Button oneStepButton;

    public ListView<String> executionStackView;

    public TableView<SymbolModel> symbolTableView;
    public TableColumn<SymbolModel, String> symbolName;
    public TableColumn<SymbolModel, Value> symbolValue;

    public ListView<String> programListView;

    public TableView<ReferenceModel> heapView;
    public TableColumn<ReferenceModel, String> referenceAddress;
    public TableColumn<ReferenceModel, Integer> referenceValue;

    public ListView<String> outputView;

    public ListView<String> fileListView;

    private ToyLanguageController controller;
    private int selectedProgramStateIndex;

    @FXML
    private void initialize() {
        Controllers.MAIN_SCREEN = this;

        initializeCellValueFactories();
        initializeButtonEvents();
        initializeProgramListClick();
    }

    private void initializeProgramListClick() {
        programListView.setOnMouseClicked(mouseEvent -> {
            int selectedIndex = programListView.getSelectionModel().getSelectedIndex();
            if (selectedIndex > -1 && selectedIndex < controller.getPrograms().size())
            {
                selectedProgramStateIndex = selectedIndex;
                programStateChanged();
            }
        });
    }

    private void initializeCellValueFactories() {
        symbolName.setCellValueFactory(new PropertyValueFactory<>("symbolName"));
        symbolValue.setCellValueFactory(new PropertyValueFactory<>("symbolValue"));
        referenceAddress.setCellValueFactory(new PropertyValueFactory<>("referenceAddress"));
        referenceValue.setCellValueFactory(new PropertyValueFactory<>("referenceValue"));
    }

    private void initializeButtonEvents() {
        initialiseChooseProgramButton();
        initialiseOneStepButton();
    }

    private void initialiseChooseProgramButton() {
        chooseProgramButton.setOnAction(actionEvent -> {
            try {
                Parent root = FXMLLoader.load(getClass().getClassLoader().getResource("ChooseProgramScreen.fxml"));
                Stage popup = new Stage();
                popup.setScene(new Scene(root));
                popup.setTitle("Pick A Program");
                popup.show();
            } catch (IOException ioException) {
                //ioException.printStackTrace();
                showError(ioException);
            }
        });
    }

    private void initialiseOneStepButton() {
        oneStepButton.setOnAction(actionEvent -> {
            try {
                if (controller == null)
                    throw new ToyLanguageException("Please pick a program!");
                controller.oneStep();
            } catch (ToyLanguageException exception) {
                showError(exception);
            }
        });
    }

    public void programStateChanged() {
        List<ProgramState> programStates = controller.getPrograms();

        refreshAllViews(programStates);
    }

    public void programPicked(int index) {
        System.out.println("Picked program " + index);

        ProgramExample programExample = ProgramExampleFactory.getAllPrograms().get(index);
        StandardProgramStateRepository repository;
        try {
            programExample.getProgram().typeCheck(new TypeEnvironment());

            repository = new StandardProgramStateRepository(programExample.getProgram(), programExample.getLogFile());
            controller = new ToyLanguageController(repository);
            controller.addListener(this);

            selectedProgramStateIndex = 0;

            programStateChanged();
        } catch (ToyLanguageException exception) {
            //exception.printStackTrace();
            showError(exception);
        }
    }

    private void showError(Exception exception) {
        FXMLLoader loader = new FXMLLoader(getClass().getClassLoader().getResource("Alert.fxml"));
        try {
            loader.load();
        } catch (IOException ioException) {
            ioException.printStackTrace();
        }
        Alert alert = loader.getController();
        alert.message.setText(exception.getMessage());

        Parent root = loader.getRoot();
        Stage errorStage = new Stage();
        errorStage.setScene(new Scene(root));
        errorStage.setTitle("Error");
        errorStage.show();
    }

    private void refreshAllViews(List<ProgramState> programStates) {
        ProgramState selectedProgramState = programStates.get(selectedProgramStateIndex);

        refreshExecutionStackView(selectedProgramState);
        refreshFileListView(selectedProgramState);
        refreshHeapView(selectedProgramState);
        refreshOutput(selectedProgramState);
        refreshSymbolTableView(selectedProgramState);
        refreshProgramList(programStates);
    }

    private void refreshExecutionStackView(ProgramState programState) {
        executionStackView.getItems().clear();
//        executionStackView.getItems().add(programState.getExecutionStack().toString());
        executionStackView.setItems(FXCollections.observableArrayList(
                programState.getExecutionStack().stream()
                        .map(Object::toString)
                        .collect(Collectors.toList())
        ));
    }

    private void refreshSymbolTableView(ProgramState programState) {
        symbolTableView.getItems().clear();
        symbolTableView.setItems(FXCollections.observableArrayList(
                programState.getSymbolTable().stream()
                        .map(symbol -> new SymbolModel(symbol.getKey(), symbol.getValue().toString()))
                        .collect(Collectors.toList())
        ));
    }

    private void refreshHeapView(ProgramState programState) {
        heapView.getItems().clear();
        heapView.setItems(FXCollections.observableArrayList(
                programState.getHeap().stream()
                        .map(reference -> new ReferenceModel(reference.getKey(), reference.getValue().toString()))
                        .collect(Collectors.toList())
        ));
    }

    private void refreshFileListView(ProgramState programState) {
        fileListView.getItems().clear();
        fileListView.setItems(FXCollections.observableArrayList(
                programState.getFileTable().stream()
                        .map(Map.Entry::getKey)
                        .collect(Collectors.toList())
        ));
    }

    private void refreshOutput(ProgramState programState) {
        outputView.getItems().clear();
        outputView.setItems(FXCollections.observableArrayList(
                programState.getOutput().stream()
                        .map(Object::toString)
                        .collect(Collectors.toList())
        ));
    }

    private void refreshProgramList(List<ProgramState> programStates) {
        programListView.getItems().clear();
        programListView.setItems(FXCollections.observableArrayList(
                programStates.stream()
                        .map(programState -> "Program " + programState.getId().toString())
                        .collect(Collectors.toList())
        ));
    }

    @Override
    public void invalidated(Observable observable) {
        if (observable instanceof ToyLanguageController) {
            programStateChanged();
        }
    }
}
