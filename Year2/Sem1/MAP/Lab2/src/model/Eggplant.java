package model;

public class Eggplant extends AbstractVegetable {
    public Eggplant(int id, float weight) {
        super(id, weight);
    }

    @Override
    public String toString() {
        return "Eggplant (" + this.id + "): " + this.weight + "kg";
    }
}
