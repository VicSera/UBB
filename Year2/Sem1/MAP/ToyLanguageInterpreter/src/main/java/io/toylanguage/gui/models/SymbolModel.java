package io.toylanguage.gui.models;

import io.toylanguage.model.value.Value;
import javafx.beans.property.SimpleStringProperty;

public class SymbolModel {
    private SimpleStringProperty symbolName;
    private SimpleStringProperty symbolValue;

    public SymbolModel(String symbolName, String symbolValue) {
        this.symbolName = new SimpleStringProperty(symbolName);
        this.symbolValue = new SimpleStringProperty(symbolValue);
    }

    public String getSymbolName() {
        return symbolName.get();
    }

    public void setSymbolName(String symbolName) {
        this.symbolName = new SimpleStringProperty(symbolName);
    }

    public String getSymbolValue() {
        return symbolValue.get();
    }

    public void setSymbolValue(String symbolValue) {
        this.symbolValue = new SimpleStringProperty(symbolValue);
    }
}
