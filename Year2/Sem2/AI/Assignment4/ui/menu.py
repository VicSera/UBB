from functools import partial

from controller.controller import Controller
from domain.environment import Environment
from ui.draw import displayMap, movingDrone


class Menu:
    def __init__(self, controller: Controller):
        self.controller = controller
        self.__initEnvironment()

        self.__options = {
            0: (partial(exit, 0), "Exit"),
            1: (self.__displayMap, "Display map"),
            2: (self.__runSimulation, "Run simulation")
        }

        while True:
            self.__runMenu()
        pass

    def __initEnvironment(self):
        self.controller.repository.environment = Environment(20, 0.1, 5)

    def __runMenu(self):
        options = self.__options
        for nr in options:
            print(str(nr) + ". " + options[nr][1])
        choice = int(input("--> "))
        options[choice][0]()

    def __displayMap(self):
        displayMap(self.controller.repository.environment)

    def __runSimulation(self):
        env = self.controller.repository.environment
        start = env.sensors[0]
        solution = self.controller.simulateAntColony(100, 5, start,
                                                     100, env, 1.9, 0.9, 0.05, 0.5)

        for move in solution.path:
            print("Sensor: " + str(move.sensor.position) + "; Energy: " + str(move.energy))
        movingDrone(env, start.position, solution.path, self.controller.bestPaths)


