import pygame

from src.commons.colors import WHITE


class GUI:
    def __init__(self, controller):
        self.__controller = controller
        self.__controller.set_listener(self)

        self.__screen = pygame.display.set_mode((800, 400))
        self.__screen.fill(WHITE)
        self.__screen.blit(self.__controller.environment.image(), (0, 0))

    def react_to_drone_movement(self, drone_data):
        detected_map = self.__controller.map
        self.__screen.blit(detected_map.image(drone_data[0], drone_data[1], drone_data[2]), (400, 0))
        pygame.display.flip()

    def start(self):
        self.__controller.loop()
