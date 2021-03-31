import pygame
from pygame import K_UP, K_DOWN, K_LEFT, K_RIGHT

from src.commons.directions import UP, DOWN, LEFT, RIGHT, indexVariation


class Drone():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__visited = []
        self.__stack = [(x, y)]

    def move(self, detectedMap):
        pressed_keys = pygame.key.get_pressed()
        if self.x > 0:
            if pressed_keys[K_UP] and detectedMap.surface[self.x - 1][self.y] == 0:
                self.x = self.x - 1
        if self.x < 19:
            if pressed_keys[K_DOWN] and detectedMap.surface[self.x + 1][self.y] == 0:
                self.x = self.x + 1

        if self.y > 0:
            if pressed_keys[K_LEFT] and detectedMap.surface[self.x][self.y - 1] == 0:
                self.y = self.y - 1
        if self.y < 19:
            if pressed_keys[K_RIGHT] and detectedMap.surface[self.x][self.y + 1] == 0:
                self.y = self.y + 1

    def moveDSF(self, detectedMap):
        def outOfBounds(value):
            return value not in range(0, 20)

        def validMove(x, y):
            return not outOfBounds(x) and not outOfBounds(y) \
                and detectedMap.surface[x][y] != 1 and (x, y) not in self.__visited

        if not (self.x, self.y) in self.__visited:
            self.__visited.append((self.x, self.y))
            for direction in [UP, DOWN, LEFT, RIGHT]:
                new_x = self.x + indexVariation[direction][0]
                new_y = self.y + indexVariation[direction][1]
                if validMove(new_x, new_y):
                    self.__stack.append((self.x, self.y))
                    self.__stack.append((new_x, new_y))

        if len(self.__stack) != 0:
            self.x, self.y = self.__stack.pop()
        else:
            self.x, self.y = None, None
