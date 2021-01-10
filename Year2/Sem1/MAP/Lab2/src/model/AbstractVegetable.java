package model;

public abstract class AbstractVegetable implements Vegetable {
    protected int id;
    protected float weight;

    AbstractVegetable(int id, float weight) {
        this.id = id;
        this.weight = weight;
    }

    @Override
    public float getWeight() {
        return this.weight;
    }

    @Override
    public int getId() {
        return this.id;
    }
}
