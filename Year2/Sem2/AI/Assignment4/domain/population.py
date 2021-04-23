from domain.drone import Drone


class Population:
    def __init__(self, environment, paths, battery, size, startingSensor):
        self.environment = environment
        self.paths = paths
        self.size = size
        self.battery = battery
        self.startingSensor = startingSensor

        self.__initDrones()

    def __initDrones(self):
        self.drones = [Drone(environment=self.environment,
                             paths=self.paths,
                             battery=self.battery,
                             startingSensor=self.startingSensor) for _ in range(self.size)]