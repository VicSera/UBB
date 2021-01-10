package controller;

import exceptions.DuplicateIdException;
import exceptions.IdNotFoundException;
import model.Eggplant;
import model.Pepper;
import model.Tomato;
import model.Vegetable;
import repository.VegetableRepository;

public class VegetableController {
    private final VegetableRepository repository;

    public VegetableController(VegetableRepository repository) {
        this.repository = repository;
    }

    public void addTomato(int id, float weight) throws DuplicateIdException {
        this.repository.addVegetable(new Tomato(id, weight));
    }

    public void addPepper(int id, float weight) throws DuplicateIdException {
        this.repository.addVegetable(new Pepper(id, weight));
    }

    public void addEggplant(int id, float weight) throws DuplicateIdException {
        this.repository.addVegetable(new Eggplant(id, weight));
    }

    public void deleteVegetable(int id) throws IdNotFoundException {
        this.repository.deleteVegetable(id);
    }

    public Vegetable[] getVegetablesHeavierThan200Grams() {
        return this.repository.getFilteredVegetables(vegetable -> vegetable.getWeight() > 0.2f);
    }

    public Vegetable[] getAllVegetables() {
        return this.repository.getAllVegetables();
    }
}
