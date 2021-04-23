from copy import deepcopy
from random import *
import numpy as np

from utils import directions


class Map:
    def __init__(self, n=20, m=20):
        self.n = n
        self.m = m
        self.surface = np.zeros((self.n, self.m))

    def randomMap(self, fill=0.2):
        for i in range(self.n):
            for j in range(self.m):
                if random() <= fill:
                    self.surface[i][j] = 1

    def __str__(self):
        string = ""
        for i in range(self.n):
            for j in range(self.m):
                string = string + str(int(self.surface[i][j]))
            string = string + "\n"
        return string

class Gene:
    def __init__(self):
        self.value = randrange(0, 3, 1)

    def repair(self, value):
        self.value = value

class Individual:
    def __init__(self, size = 0, chromosome = None):
        self.__size = size
        if chromosome is None:
            self.__chromosome = [Gene() for i in range(self.__size)]
        else:
            self.__chromosome = chromosome
        self.__f = None

    @property
    def chromosome(self):
        return self.__chromosome

    @chromosome.setter
    def chromosome(self, value):
        self.__chromosome = value

    @property
    def fitness(self):
        return self.__f

    def computePath(self, initialPos: tuple):
        currentPos = initialPos

        path = [currentPos]
        for gene in self.__chromosome:
            currentPos = (currentPos[0] + directions[gene.value][0], currentPos[1] + directions[gene.value][1])
            path.append(currentPos)

        return path

    def computeFitness(self, envMap: Map, initialPos: tuple):
        if self.__f is not None:
            return
        def invalidMove(pos: tuple, envMap: Map):
            return pos[0] < 0 or pos[0] > 19 or pos[1] < 0 or pos[1] > 19 or envMap.surface[pos[0]][pos[1]] == 1

        def getMarkedCells(pos: tuple, envMap: Map, marked):
            counter = 0
            for direction in directions:
                posCopy = deepcopy(pos)
                while not invalidMove(posCopy, envMap):
                    if posCopy not in marked or not marked[posCopy]:
                        marked[posCopy] = True
                        counter += 1
                    posCopy = (posCopy[0] + direction[0], posCopy[1] + direction[1])
            return counter


        def geneCorrection(currentPos, envMap):
            for index, direction in enumerate(directions):
                nextPos = (currentPos[0] + direction[0], currentPos[1] + direction[1])
                if not invalidMove(nextPos, envMap):
                    return index
            return 0


        marked = {}
        self.__f = getMarkedCells(initialPos, envMap, marked)
        currentPos = initialPos

        for gene in self.__chromosome:
            nextPos = (currentPos[0] + directions[gene.value][0], currentPos[1] + directions[gene.value][1])
            if invalidMove(nextPos, envMap):
                gene.repair(geneCorrection(currentPos, envMap))
                nextPos = (currentPos[0] + directions[gene.value][0], currentPos[1] + directions[gene.value][1])
            currentPos = nextPos
            self.__f += getMarkedCells(currentPos, envMap, marked)

        penalty = (abs(currentPos[0] - initialPos[0]) + abs(currentPos[1] - initialPos[1])) * 50
        self.__f -= penalty

    
    def mutate(self, mutateProbability = 0.04):
        for index in range(len(self.__chromosome)):
            if random() < mutateProbability:
                self.__chromosome[index] = Gene()

    # do a 2-cutting-point crossover directly at the middle
    def crossover(self, otherParent, crossoverProbability = 0.8):
        offspring1, offspring2 = Individual(self.__size), Individual(self.__size) 
        if random() < crossoverProbability:
            leftChromosome = []
            rightChromosome = []

            for rank in range(len(self.chromosome)):
                if rank < len(self.chromosome) / 2:
                    leftChromosome.append(deepcopy(self.chromosome[rank]))
                    rightChromosome.append(deepcopy(otherParent.chromosome[rank]))
                else:
                    rightChromosome.append(deepcopy(self.chromosome[rank]))
                    leftChromosome.append(deepcopy(otherParent.chromosome[rank]))

            offspring1.chromosome = leftChromosome
            offspring2.chromosome = rightChromosome
        else:
            offspring1.chromosome = deepcopy(self.chromosome)
            offspring2.chromosome = deepcopy(otherParent.chromosome)
        
        return offspring1, offspring2
    
class Population:
    def __init__(self, initialPos: tuple, populationSize = 0, individualSize = 0):
        self.__initialPos = initialPos
        self.__populationSize = populationSize
        self.__individuals = [Individual(individualSize) for _ in range(populationSize)]

    @property
    def size(self):
        return self.__populationSize

    @property
    def individuals(self):
        return self.__individuals

    @individuals.setter
    def individuals(self, value):
        self.__individuals = value

    def evaluate(self, map: Map):
        # evaluates the population
        for individual in self.__individuals:
            individual.computeFitness(map, self.__initialPos)

    def selection(self, k = 0):
        self.__individuals.sort(key = lambda individual: individual.fitness,
                                reverse = True)
        return deepcopy(list(self.__individuals[:k]))

                
    