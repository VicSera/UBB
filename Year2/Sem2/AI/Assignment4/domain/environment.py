from random import random, randint

from domain.sensor import Sensor
from util.environmentUtils import Cells


class Environment:
    def __init__(self, size, fill, numberOfSensors):
        self.size = size
        self.cells = [[1 if random() < fill else 0 for x in range(size)] for y in range(size)]

        self.__initializeSensors(numberOfSensors)

    def __initializeSensors(self, numberOfSensors):
        remaining = numberOfSensors
        self.sensors = []

        while remaining != 0:
            x, y = randint(0, 19), randint(0, 19)
            if self.cells[x][y] == Cells.EMPTY:
                self.cells[x][y] = Cells.SENSOR
                self.sensors.append(Sensor((x, y), self))
                remaining -= 1

    def getSensorAt(self, pos):
        for sensor in self.sensors:
            if sensor.position == pos:
                return sensor

        return None
