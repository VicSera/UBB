# -*- coding: utf-8 -*-


# imports
import numpy
import numpy as np
from numpy import average
from numpy.core import std

from gui import *
from controller import *
from domain import *
from matplotlib.pyplot import *

class Menu:
    def __init__(self, controller: Controller):
        self.__controller = controller
        self.__config = {
            "map": Map(),
            "map-fill": 0.2,
            "map-size": 20,
            "number-of-iterations": 100,
            "initial-position": (randint(0, 19), randint(0, 19)),
            "individual-size": 20,
            "population-size": 100,
            "mutation-chance": 0.1,
            "crossover-chance": 0.8
        }

        self.__config["map"].randomMap(0.2)

        self.__mainOptions = {
            "1": self.__mapMenu,
            "2": self.__eaMenu
        }

        self.__eaOptions = {
            "0": self.__mainMenu,
            "1": self.__setupParameters,
            "2": self.__runSolver,
            "3": self.__runMultipleSolvers,
            "4": self.__visualizeDroneMoving
        }

        self. __mapOptions = {
            "0": self.__mainMenu,
            "1": self.__createRandomMap,
            "2": self.__loadMap,
            "3": self.__saveMap,
            "4": self.__visualizeMap
        }

    def run(self):
        self.__mainMenu()

    def __mainMenu(self):
        print("1. Map options")
        print("2. EA options")

        option = input("Choice -> ")
        self.__mainOptions[option]()


    def __mapMenu(self):
        print("0. Back")
        print("1. Create a random map")
        print("2. Load a map")
        print("3. Save a map")
        print("4. Visualize map")

        option = input("Choice -> ")
        self.__mapOptions[option]()
        self.__mapMenu()


    def __eaMenu(self):
        print("0. Back")
        print("1. Setup parameters")
        print("2. Run the solver")
        print("3. Visualize the statistics")
        print("4. Visualize the drone moving")

        option = input("Choice -> ")
        self.__eaOptions[option]()
        self.__eaMenu()

    def __createRandomMap(self):
        self.__config["map-size"] = int(input("Map size: "))
        self.__config["map-fill"] = float(input("Map fill: "))

        map = Map(self.__config["map-size"], self.__config["map-size"])
        map.randomMap(self.__config["map-fill"])
        self.__config["map"] = map

    def __loadMap(self):
        path = input("Map path: ")
        self.__config["map"] = self.__controller.loadObject(path)
        self.__config["map-size"] = self.__config["map"].n

    def __saveMap(self):
        path = input("Map path: ")
        self.__controller.saveObject(self.__config["map"], path)

    def __visualizeMap(self):
        displayMap(self.__config)

    def __setupParameters(self):
        self.__config["initial-position"] = (int(input("Initial X: ")), int(input("Initial Y: ")))
        self.__config["number-of-iterations"] = int(input("Number of iterations: "))
        self.__config["population-size"] = int(input("Population size: "))
        self.__config["individual-size"] = int(input("Battery size: "))
        self.__config["mutation-chance"] = float(input("Mutation chance: "))
        self.__config["crossover-chance"] = float(input("Crossover chance: "))

    def __runSolver(self):
        startTime = time.time()
        results = self.__controller.solver(self.__config)

        averageFitness, maxFitness = results["averageFitnessHistory"], results["maxFitnessHistory"]
        endTime = time.time()

        self.__config["best-path"] = results["bestPath"]

        print("Duration: " + str(endTime - startTime) + "s")
        print("Average fitness: " + str(averageFitness[-1]))
        print("Max fitness: " + str(maxFitness[-1]))

        fig, axes = subplots(2)
        fig.suptitle("Max and average fitnesses")
        axes[0].plot(maxFitness)
        axes[1].plot(averageFitness)
        show()

    def __runMultipleSolvers(self):
        startTime = time.time()

        maxFitnesses = []
        for solverNumber in range(30):
            startTimeSolver = time.time()
            seed(time.time())
            results = self.__controller.solver(self.__config)
            endTimeSolver = time.time()

            print("Solver " + str(solverNumber) + " finished in: " + str(endTimeSolver - startTimeSolver))

            maxFitnesses.append(results["maxFitnessHistory"][-1])

        endTime = time.time()
        print("All solvers finished in: " + str(endTime - startTime))
        print("Average max fitness: " + str(average(maxFitnesses)))
        print("Max fitness standard deviation: " + str(std(maxFitnesses)))
        plot(maxFitnesses)
        show()

    def __visualizeDroneMoving(self):
        if self.__config["best-path"] is None:
            print("Please run the algorithm before trying this.")
            return

        movingDrone(self.__config["map"], self.__config["best-path"])