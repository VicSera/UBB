from src.controller.controller import Controller
from src.gui.gui import GUI
from src.model.environment import Environment


from src.repository.environment_repository import EnvironmentRepository
from src.repository.image_repository import ImageRepository


def main():
    environment_repository = EnvironmentRepository()
    image_repository = ImageRepository()

    controller = Controller(environment_repository, image_repository)

    gui = GUI(controller)
    gui.start()


if __name__ == "__main__":
    main()
