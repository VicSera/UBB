package io.toylanguage.gui.models;

import javafx.beans.property.SimpleIntegerProperty;
import javafx.beans.property.SimpleStringProperty;

public class ReferenceModel {
    private SimpleIntegerProperty referenceAddress;
    private SimpleStringProperty referenceValue;

    public int getReferenceAddress() {
        return referenceAddress.get();
    }

    public void setReferenceAddress(int referenceAddress) {
        this.referenceAddress = new SimpleIntegerProperty(referenceAddress);
    }

    public String getReferenceValue() {
        return referenceValue.get();
    }

    public void setReferenceValue(String referenceValue) {
        this.referenceValue = new SimpleStringProperty(referenceValue);
    }

    public ReferenceModel(int referenceAddress, String referenceValue) {
        this.referenceAddress = new SimpleIntegerProperty(referenceAddress);
        this.referenceValue = new SimpleStringProperty(referenceValue);
    }
}
