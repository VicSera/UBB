import os

from src.model.environment import Environment


class EnvironmentRepository:
    def __init__(self):
        self.__environment_path = os.path.join("assets", "test2.map")

    def getEnvironment(self):
        environment = Environment()
        environment.loadEnvironment(self.__environment_path)

        return environment
