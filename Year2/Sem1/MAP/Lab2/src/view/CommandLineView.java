package view;

import controller.VegetableController;
import exceptions.DuplicateIdException;
import exceptions.IdNotFoundException;
import model.Vegetable;

public class CommandLineView {
    private final VegetableController controller;

    public CommandLineView(VegetableController controller) {
        this.controller = controller;
    }

    public void displayVegetables() {
        System.out.println("All vegetables:");
        final Vegetable[] vegetables = this.controller.getAllVegetables();

        for (Vegetable vegetable: vegetables) {
            System.out.println(vegetable);
        }

        System.out.println();
    }

    public void displayVegetablesHeavierThan200Grams() {
        System.out.println("Vegetables heavier than 200 grams (0.2kgs):");
        final Vegetable[] vegetables = this.controller.getVegetablesHeavierThan200Grams();

        for (Vegetable vegetable: vegetables) {
            System.out.println(vegetable);
        }

        System.out.println();
    }

    public void deleteVegetable(int id) {
        try {
            controller.deleteVegetable(id);
            System.out.println("Deleted vegetable with id " + id + "\n");
        } catch (IdNotFoundException idNotFoundException) {
            System.out.println("Id " + id + " was not found!\n");
        }
    }

    public void addVegetable(String type, int id, float weight) {
        try{
            switch (type) {
                case "Tomato" -> controller.addTomato(id, weight);
                case "Pepper" -> controller.addPepper(id, weight);
                case "Eggplant" -> controller.addEggplant(id, weight);
                default -> System.out.println("Unknown vegetable: " + type + "\n");
            }
        } catch (DuplicateIdException duplicateId) {
            System.out.println("Id " + id + " already exists!\n");
        }
    }
}
