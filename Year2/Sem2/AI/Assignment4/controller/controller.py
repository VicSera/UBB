from queue import PriorityQueue

from domain.drone import Drone
from domain.environment import Environment
from domain.path import Path
from domain.population import Population
from util.environmentUtils import Directions
from util.functions import taxicabDistance, isValidPosition

import itertools
import math

class Controller:
    def __init__(self, repository):
        self.repository = repository

    def createNewEnvironment(self, environmentSize, fill, numberOfSensors):
        return Environment(environmentSize, fill, numberOfSensors)

    def findBestPathsBetweenAllSensors(self, environment):
        self.bestPaths = {}
        for sensor1 in environment.sensors:
            for sensor2 in environment.sensors:
                path = self.findBestPathBetweenSensors(sensor1, sensor2, environment)
                self.bestPaths[(sensor1.position, sensor2.position)] = path

        return self.bestPaths

    def findBestPathBetweenSensors(self, sensor1, sensor2, environment):
        # find the best path between two sensors using A*
        # implement the search function and put it in controller
        # returns a Path containing the moves and the total cost of the path

        def reconstructPath(initialPos, finalPos, parent):
            path = []
            current = finalPos
            path.append(current)
            while current != initialPos:
                current = parent[current]
                path.append(current)
            path.reverse()
            return path

        queue = PriorityQueue()
        parent = {}
        steps = {}

        queue.put((taxicabDistance(sensor1.position, sensor2.position), sensor1.position))
        steps[sensor1.position] = 0

        while not queue.empty():
            current = queue.get()[1]
            if current == sensor2.position:
                return Path(reconstructPath(sensor1.position, sensor2.position, parent), steps[sensor2.position])
            for direction in Directions.ALL:
                next = (current[0] + direction[0], current[1] + direction[1])
                if isValidPosition(next, environment) and \
                        (next not in steps or steps[current] + 1 < steps[next]):
                    dist = taxicabDistance(next, sensor2.position)
                    steps[next] = steps[current] + 1
                    queue.put((dist, next))
                    parent[next] = current

        # If we got here, there isn't any path leading to our destination
        raise Exception("The sensors are not all reachable")

    def simulateAntColony(self, numberOfEpochs, numberOfAnts, startingSensor, battery, environment, alpha, beta, rho, q0):
        bestPaths = self.findBestPathsBetweenAllSensors(environment)
        bestDrone = Drone(battery, environment, bestPaths, startingSensor)
        trace = {(sensor1.position, sensor2.position, energy): 1
                 for sensor1 in environment.sensors for sensor2 in environment.sensors for energy in range(6)}

        for epochNumber in range(numberOfEpochs):
            candidateDrone = self.__oneEpoch(numberOfAnts, startingSensor, battery, environment, bestPaths,
                                       trace, q0, alpha, beta, rho)
            if candidateDrone.fitness > bestDrone.fitness:
                bestDrone = candidateDrone

        return bestDrone

    def __oneEpoch(self, numberOfAnts, startingSensor, battery, environment, bestPaths, trace, q0, alpha, beta, rho):
        population = Population(environment=environment,
                                paths=bestPaths,
                                battery=battery,
                                size=numberOfAnts,
                                startingSensor=startingSensor)

        for moveNumber in range(math.factorial(len(environment.sensors)) * math.factorial(5)):
            for drone in population.drones:
                drone.move(q0, trace, alpha, beta)

        dTrace = [(drone, drone.fitness) for drone in population.drones]

        # decay trace
        for sensor1, sensor2, energy in itertools.product(environment.sensors, environment.sensors, range(6)):
            trace[(sensor1.position, sensor2.position, energy)] *= (1 - rho)

        for drone, fitness in dTrace:
            for i in range(len(drone.path) - 1):
                start = drone.path[i]
                end = drone.path[i + 1]
                trace[(start.sensor.position, end.sensor.position, end.energy)] += fitness

        # get the path of the drone with the highest fitness
        return max(dTrace, key=lambda dwf: dwf[1])[0]
