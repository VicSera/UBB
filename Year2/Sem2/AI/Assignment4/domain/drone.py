import random
import numpy as np

from domain.move import Move

class Drone:
    def __init__(self, battery, environment, paths, startingSensor):
        self.environment = environment
        self.battery = battery
        self.path = []
        self.paths = paths
        self.startingSensor = startingSensor
        self.__initPosition()

    def __initPosition(self):
        # start from a random sensor
        energySpent = random.randint(0, 5)
        self.path.append(Move(self.startingSensor, energySpent))
        self.battery -= energySpent

    def validMoves(self):
        moves = []
        sensorsVisited = [move.sensor for move in self.path]
        for sensor in self.environment.sensors:
           if sensor not in sensorsVisited and self.battery >= self.paths[(self.path[-1].sensor.position, sensor.position)].cost:
                # the amount of battery that would be left if the drone moved to this position
                theoreticalBatteryLeft = self.battery - self.paths[self.path[-1].sensor.position, sensor.position].cost

                # for every energy level between 0 and min(5, remaining batter), add a move
                for energyLevel in range(min(5, theoreticalBatteryLeft) + 1):
                    moves.append(Move(sensor, energyLevel))
        return moves

    def __makeMove(self, move: Move):
        self.battery -= self.paths[(self.path[-1].sensor.position, move.sensor.position)].cost + move.energy
        self.path.append(move)

    def move(self, q0, trace, alpha, beta):
        validMoves = self.validMoves()

        # if no moves are left, stop
        if len(validMoves) == 0:
            return False

        movesWithDesirability = [
            (move, (move.score ** beta) * (trace[(self.path[-1].sensor.position, move.sensor.position, move.energy)] ** alpha))
            for move in validMoves
        ]

        if random.random() < q0:
            # take the best possible move
            bestMove = max(movesWithDesirability, key=lambda mwd: mwd[1])
            self.__makeMove(bestMove[0])
        else:
            desirabilities = [mwd[1] for mwd in movesWithDesirability]
            s = sum(desirabilities)

            if s == 0:
                self.__makeMove(random.choice(validMoves))
                return True

            scaledDesirabilities = [desirability / s for desirability in desirabilities]
            move = np.random.choice(validMoves, 1, scaledDesirabilities)[0]
            self.__makeMove(move)
        return True

    @property
    def fitness(self):
        fitness = 0
        for move in self.path:
            fitness += move.score

        return fitness
