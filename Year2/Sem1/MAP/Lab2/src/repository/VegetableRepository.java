package repository;

import exceptions.DuplicateIdException;
import exceptions.IdNotFoundException;
import model.Vegetable;

import java.util.function.Predicate;

public interface VegetableRepository {
    void addVegetable(Vegetable vegetable) throws DuplicateIdException;

    Vegetable[] getAllVegetables();

    void deleteVegetable(int id) throws IdNotFoundException;

    Vegetable[] getFilteredVegetables(Predicate<Vegetable> predicate);
}
