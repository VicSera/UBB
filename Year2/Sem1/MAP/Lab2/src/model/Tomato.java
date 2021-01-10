package model;

public class Tomato extends AbstractVegetable {
    public Tomato(int id, float weight) {
        super(id, weight);
    }

    @Override
    public String toString() {
        return "Tomato (" + this.id + "): " + this.weight + "kg";
    }
}
