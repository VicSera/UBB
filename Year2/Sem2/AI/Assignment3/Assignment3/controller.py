from repository import *


class Controller:
    def __init__(self, repository: Repository):
        self.__repository = repository

    def iteration(self, population: Population, mutationProbability, crossoverProbability):
        newPopulation = population.selection(int(population.size / 2))

        parents = deepcopy(newPopulation)
        partners = deepcopy(parents)
        shuffle(partners)

        for mom, dad in zip(parents, partners):
            firstKid, secondKid = mom.crossover(dad, crossoverProbability)
            if random() < .5:
                firstKid.mutate(mutationProbability)
                newPopulation.append(firstKid)
            else:
                secondKid.mutate(mutationProbability)
                newPopulation.append(secondKid)

        population.individuals = newPopulation

        
    def run(self, population, map, iterations, mutationProbability, crossoverProbability, initialPos):
        averageFitnessHistory = []
        maxFitnessHistory = []
        bestPath = None
        population.evaluate(map)

        for iteration in range(iterations):
            self.iteration(population, mutationProbability, crossoverProbability)
            population.evaluate(map)
            fitnesses = [individual.fitness for individual in population.individuals]

            averageFitness = np.average(fitnesses)
            maxFitness = np.max(fitnesses)

            averageFitnessHistory.append(averageFitness)
            maxFitnessHistory.append(maxFitness)

        for individual in population.individuals:
            if individual.fitness == maxFitnessHistory[-1]:
                bestPath = individual.computePath(initialPos)

        return {
            "averageFitnessHistory": averageFitnessHistory,
            "maxFitnessHistory": maxFitnessHistory,
            "bestPath": bestPath
        }

    def solver(self, config):
        map = Map(config["map-size"], config["map-size"])
        map.randomMap(config["map-fill"])
        population = self.__repository.createPopulation(config)
        iterations = config["number-of-iterations"]
        mutationProbability = config["mutation-chance"]
        crossoverProbability = config["crossover-chance"]
        initialPos = config["initial-position"]

        return self.run(population, map, iterations, mutationProbability, crossoverProbability, initialPos)

    def saveObject(self, object, path):
        self.__repository.saveObject(object, path)

    def loadObject(self, path):
        return self.__repository.loadObject(path)