import os

import pygame


class ImageRepository:
    def __init__(self):
        self.__drone_image_path = os.path.join("assets", "drona.png")
        self.__board_image_path = os.path.join("assets", "board.png")
        self.__logo_image_path = os.path.join("assets", "logo32x32.png")

    def getDroneImage(self):
        return pygame.image.load(self.__drone_image_path)

    def getBoardImage(self):
        return pygame.image.load(self.__board_image_path)

    def getLogoImage(self):
        return pygame.image.load(self.__logo_image_path)
