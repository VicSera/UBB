# -*- coding: utf-8 -*-

import pickle
from domain import *

from domain import Population


class Repository:
    def __init__(self):
        self.__populations = []
        self.cmap = Map()
        
    def createPopulation(self, config):
        # args = [initialPosition, populationSize, individualSize] -- you can add more args
        return Population(
            config["initial-position"],
            config["population-size"],
            config["individual-size"])

    def saveObject(self, object, path):
        with open(path, mode="wb") as file:
            pickle.dump(object, file)

    def loadObject(self, path):
        with open(path, mode="rb") as file:
            return pickle.load(file)

    # TO DO : add the other components for the repository: 
    #    load and save from file, etc
            