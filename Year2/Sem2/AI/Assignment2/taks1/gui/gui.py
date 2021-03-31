from random import randint

import pygame

from taks1.domain.constants import GREEN, GRAYBLUE, RED, WHITE
from taks1.domain.dmap import Map
from taks1.domain.drone import Drone


class GUI:
    def __init__(self, search_service):
        self.__search_service = search_service
        self.__map = Map()

    def displayWithPath(self, image, path):
        mark = pygame.Surface((20, 20))
        start = pygame.Surface((20, 20))
        end = pygame.Surface((20, 20))
        mark.fill(GREEN)
        start.fill(GRAYBLUE)
        end.fill(RED)
        image.blit(start, (path[0][1] * 20, path[0][0] * 20))
        image.blit(end, (path[-1][1] * 20, path[-1][0] * 20))
        for move in path[1:-1]:
            image.blit(mark, (move[1] * 20, move[0] * 20))

        return image

    def run(self):
        # m.randomMap()
        # m.saveMap("test2.map")
        self.__map.loadMap("test1.map")

        # initialize the pygame module
        pygame.init()
        # load and set the logo
        logo = pygame.image.load("logo32x32.png")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("Path in simple environment")

        # we position the drone somewhere in the area
        x = randint(0, 19)
        y = randint(0, 19)
        finalX = randint(0, 19)
        finalY = randint(0, 19)

        print(f'{x}, {y} -> {finalX}, {finalY}')

        # create drona
        d = Drone(x, y)

        # create a surface on screen that has the size of 400 x 480
        screen = pygame.display.set_mode((400, 400))
        screen.fill(WHITE)

        # define a variable to control the main loop
        running = True

        path = self.__search_service.searchGreedy(self.__map, d, x, y, finalX, finalY)
        # path = self.__search_service.searchAStar(self.__map, d, x, y, finalX, finalY)
        print(path)
        if path is None:
            print("No path found. Exiting.")
            pygame.quit()
            return

        screen.blit(self.displayWithPath(self.__map.image(), path), (0, 0))
        pygame.display.flip()

        # main loop
        while running:
            # event handling, gets all event from the event queue
            for event in pygame.event.get():
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    # change the value to False, to exit the main loop
                    running = False

        pygame.quit()