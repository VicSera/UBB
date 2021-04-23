# -*- coding: utf-8 -*-

from pygame.locals import *
import pygame, time
from utils import *
from domain import *
from util.colors import BLUE, WHITE, GREEN, RED, GRAYBLUE
from util.environmentUtils import Directions, Cells


def initPyGame(dimension):
    # init the pygame
    pygame.init()
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("drone exploration with AE")

    screen = pygame.display.set_mode(dimension)
    screen.fill(WHITE)
    return screen


def closePyGame():
    # closes the pygame
    running = True
    # loop for events
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
    pygame.quit()


def movingDrone(currentMap, initialCell, moves, paths, speed=1):
    # animation of a drone on a path
    marked = []
    screen = initPyGame((currentMap.size * 20, currentMap.size * 20))

    drona = pygame.image.load("drona.png")
    start = initialCell

    seen = pygame.Surface((20, 20))
    seen.fill(GRAYBLUE)
    brick = pygame.Surface((20, 20))
    brick.fill(GREEN)
    mapImage = image(currentMap)

    for move in moves:
        for cell in paths[start, move.sensor.position].cells:
            pygame.event.pump()

            screen.blit(mapImage, (0, 0))
            for seenCell in marked:
                screen.blit(seen, (seenCell[1] * 20, seenCell[0] * 20))
            screen.blit(drona, (cell[1] * 20, cell[0] * 20))
            pygame.display.flip()
            time.sleep(0.5 * speed)

        for energyLevel in range(move.energy + 1):
            markSeen(move.sensor.position, currentMap, marked, energyLevel)
            pygame.event.pump()

            screen.blit(mapImage, (0, 0))
            for seenCell in marked:
                screen.blit(seen, (seenCell[1] * 20, seenCell[0] * 20))
            # screen.blit(drona, (move.sensor.position[1] * 20, move.sensor.position[0] * 20))
            pygame.display.flip()
            time.sleep(0.5 * speed)

        start = move.sensor.position

    closePyGame()


def markSeen(pos, environment, marked, energyLevel):
    sensor = environment.getSensorAt(pos)
    for cell in sensor.computeVisibleCells(energyLevel):
        if cell not in marked:
            marked.append(cell)

def image(currentMap, colour=BLUE, background=WHITE):
    # creates the image of a map

    imagine = pygame.Surface((currentMap.size * 20, currentMap.size * 20))
    brick = pygame.Surface((20, 20))
    brick.fill(colour)
    sensor = pygame.Surface((20, 20))
    sensor.fill(RED)
    imagine.fill(background)
    for i in range(currentMap.size):
        for j in range(currentMap.size):
            if currentMap.cells[i][j] == Cells.WALL:
                imagine.blit(brick, (j * 20, i * 20))
            elif currentMap.cells[i][j] == Cells.SENSOR:
                imagine.blit(sensor, (j * 20, i * 20))
    return imagine


def displayMap(environment):
    screen = initPyGame((environment.size * 20, environment.size * 20))
    screen.blit(image(environment), (0, 0))
    pygame.display.flip()
    closePyGame()