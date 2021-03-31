import time
from random import randint

import pygame

from src.model.dmap import DMap
from src.model.drone import Drone


class Controller:
    def __init__(self, environment_repository, image_repository):
        self.__environment_repository = environment_repository
        self.__image_repository = image_repository

        self.__init_pygame()
        self.__init_drone()
        self.__init_map()
        self.__init_environment()

        self.__listener = None

    def set_listener(self, listener):
        self.__listener = listener

    def loop(self):
        # define a variable to control the main loop
        running = True

        # main loop
        while running:
            pygame.event.pump()
            # event handling, gets all event from the event queue
            for event in pygame.event.get():
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    # change the value to False, to exit the main loop
                    running = False

            self.__drone.moveDSF(self.__map)
            self.__map.markDetectedWalls(self.__environment, self.__drone.x, self.__drone.y)

            self.__drone_moved()

            time.sleep(.5)

        pygame.quit()

    def __drone_moved(self):
        self.__listener.react_to_drone_movement((self.__drone.x, self.__drone.y, self.__image_repository.getDroneImage()))

    def __init_pygame(self):
        pygame.init()
        logo = self.__image_repository.getLogoImage()
        pygame.display.set_icon(logo)
        pygame.display.set_caption("Drone exploration")

    def __init_drone(self):
        starting_x = randint(0, 19)
        starting_y = randint(0, 19)

        self.__drone = Drone(starting_x, starting_y)

    def __init_map(self):
        self.__map = DMap()

    def __init_environment(self):
        self.__environment = self.__environment_repository.getEnvironment()

    @property
    def environment(self):
        return self.__environment

    @property
    def drone(self):
        return self.__drone

    @property
    def map(self):
        return self.__map
