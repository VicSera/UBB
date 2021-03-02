package io.toylanguage.gui.models;

import javafx.beans.property.SimpleStringProperty;

import java.io.BufferedReader;

public class FileModel {
    public FileModel(String fileName) {
        this.fileName = new SimpleStringProperty(fileName);
    }

    public String getFileName() {
        return fileName.get();
    }

    public void setFileName(String fileName) {
        this.fileName = new SimpleStringProperty(fileName);
    }

    private SimpleStringProperty fileName;
}
