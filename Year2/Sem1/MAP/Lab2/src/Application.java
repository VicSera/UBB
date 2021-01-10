import controller.VegetableController;
import repository.InMemoryVegetableRepository;
import view.CommandLineView;

public class Application {
    public static void main(String[] args) {
        InMemoryVegetableRepository repository = new InMemoryVegetableRepository();
        VegetableController controller = new VegetableController(repository);
        CommandLineView view = new CommandLineView(controller);

        view.addVegetable("Tomato", 1, 0.1f);
        view.addVegetable("Pepper", 2, 0.1f);
        view.addVegetable("Pepper", 1, 0.3f); // Throws exception!
        view.addVegetable("Eggplant", 3, 0.3f);

        view.displayVegetables();

        view.deleteVegetable(1);
        view.deleteVegetable(5); // Throws exception!

        view.displayVegetables();
        view.displayVegetablesHeavierThan200Grams();
    }
}
