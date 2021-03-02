package io.toylanguage.gui.models;

import io.toylanguage.model.value.implementation.IntValue;
import javafx.beans.property.SimpleIntegerProperty;

public class LockModel {
    public int getLockLocation() {
        return lockLocation.get();
    }

    public void setLockLocation(int lockLocation) {
        this.lockLocation.set(lockLocation);
    }

    public int getLockValue() {
        return lockValue.get();
    }


    public void setLockValue(int lockValue) {
        this.lockValue.set(lockValue);
    }

    private SimpleIntegerProperty lockLocation;
    private SimpleIntegerProperty lockValue;

    public LockModel(int lockLocation, int lockValue) {
        this.lockLocation = new SimpleIntegerProperty(lockLocation);
        this.lockValue = new SimpleIntegerProperty(lockValue);
    }
}
