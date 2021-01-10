package repository;

import exceptions.DuplicateIdException;
import exceptions.IdNotFoundException;
import model.Vegetable;

import java.util.function.Predicate;

public class InMemoryVegetableRepository implements VegetableRepository {
    private Vegetable[] vegetables;
    private int capacity = 100;
    private int size;

    public InMemoryVegetableRepository() {
        this.vegetables = new Vegetable[capacity];
        size = 0;
    }

    @Override
    public void addVegetable(Vegetable vegetable) throws DuplicateIdException {
        for (Vegetable existingVegetable: vegetables) {
            if (existingVegetable != null && existingVegetable.getId() == vegetable.getId())
                throw new DuplicateIdException();
        }

        vegetables[size] = vegetable;
        ++size;

        resize();
    }

    private void resize() {
        if (size == capacity) {
            Vegetable[] newVegetables = new Vegetable[capacity * 2];
            System.arraycopy(this.vegetables, 0, newVegetables, 0, capacity);
            this.vegetables = newVegetables;

            capacity *= 2;
        }
    }

    @Override
    public Vegetable[] getAllVegetables() {
        Vegetable[] vegetables = new Vegetable[this.size];
        System.arraycopy(this.vegetables, 0, vegetables, 0, size);
        return vegetables;
    }

    @Override
    public Vegetable[] getFilteredVegetables(Predicate<Vegetable> predicate) {
        Vegetable[] filteredVegetables = new Vegetable[this.size];
        int filteredSize = 0;

        for (Vegetable vegetable: vegetables) {
            if (vegetable != null && predicate.test(vegetable)) {
                filteredVegetables[filteredSize] = vegetable;
                ++filteredSize;
            }
        }

        Vegetable[] trimmedVegetables = new Vegetable[filteredSize];
        System.arraycopy(filteredVegetables, 0, trimmedVegetables, 0, filteredSize);

        return trimmedVegetables;
    }

    @Override
    public void deleteVegetable(int id) throws IdNotFoundException {
        Vegetable[] vegetables = new Vegetable[capacity];
        int newSize = 0;
        for (Vegetable vegetable: this.vegetables) {
            if (vegetable != null && vegetable.getId() != id) {
                vegetables[newSize] = vegetable;
                ++newSize;
            }
        }

        if (newSize == this.size)
            throw new IdNotFoundException();

        this.vegetables = vegetables;
        this.size = newSize;
    }
}
