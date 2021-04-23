from util.environmentUtils import Directions
from util.functions import isValidPosition


class Sensor:
    def __init__(self, position, environment):
        self.position = position
        self.environment = environment

        self.__initEnergyLevels()

    def __initEnergyLevels(self):
        self.scoreAtEnergyLevel = {}
        for energyLevel in range(6):
            visibleCells = self.computeVisibleCells(energyLevel)
            self.scoreAtEnergyLevel[energyLevel] = len(visibleCells)

    def computeVisibleCells(self, energyLevel):
        visibleCells = []

        for direction in Directions.ALL:
            newPos = self.position
            newPos = (newPos[0] + direction[0], newPos[1] + direction[1])
            remainingEnergy = energyLevel
            while remainingEnergy != 0 and isValidPosition(newPos, self.environment):
                visibleCells.append(newPos)
                remainingEnergy -= 1
                newPos = (newPos[0] + direction[0], newPos[1] + direction[1])

        return visibleCells