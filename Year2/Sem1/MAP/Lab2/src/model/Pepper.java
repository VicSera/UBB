package model;

public class Pepper extends AbstractVegetable {
    public Pepper(int id, float weight) {
        super(id, weight);
    }

    @Override
    public String toString() {
        return "Pepper (" + this.id + "): " + this.weight + "kg";
    }
}
