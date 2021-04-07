import time
from random import seed

from controller import Controller
from repository import Repository
from ui import Menu

if __name__ == "__main__":
    seed(time.time())
    repository = Repository()
    controller = Controller(repository)
    menu = Menu(controller)
    menu.run()