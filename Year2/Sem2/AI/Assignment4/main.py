from controller.controller import Controller
from repository.repository import Repository
from ui.menu import Menu

if __name__ == '__main__':
    repository = Repository()
    controller = Controller(repository)
    menu = Menu(controller)