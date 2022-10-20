import pygame
from pygame import Rect
from pygame._sdl2 import Texture
from pygame.locals import *


class NPatchWindow():
    def __init__(self, renderer: pygame._sdl2.Renderer, filename: str, insetAmt: int):
        self.texture = Texture.from_surface(
            renderer, pygame.image.load(filename))
        self.width = self.texture.width
        self.height = self.texture.height
        self.insetAmt = insetAmt

        # setup the different regions required for the nine patches
        self.regions = []
        self.regions.append(Rect(0, 0, insetAmt, insetAmt))  # top left
        self.regions.append(
            Rect(insetAmt, 0, self.width - (2*insetAmt), insetAmt))  # top
        self.regions.append(Rect(self.width - insetAmt, 0,
                            insetAmt, insetAmt))  # top right

        self.regions.append(
            Rect(0, insetAmt, insetAmt, self.height - (2*insetAmt)))  # left
        self.regions.append(Rect(insetAmt, insetAmt, self.width -
                            (2*insetAmt), self.height - (2*insetAmt)))  # center
        self.regions.append(Rect(self.width - insetAmt, insetAmt,
                            insetAmt, self.height - (2*insetAmt)))  # right

        self.regions.append(Rect(0, self.height - insetAmt,
                            insetAmt, insetAmt))  # bottom left
        self.regions.append(Rect(insetAmt, self.height - insetAmt,
                            self.width - (2 * insetAmt), insetAmt))  # bottom
        self.regions.append(Rect(self.width - insetAmt, self.height -
                            insetAmt, insetAmt, insetAmt))  # bottom right

    def draw(self, area: pygame.Rect):
        self.texture.draw(self.regions[0], Rect(
            area.x, area.y, self.insetAmt, self.insetAmt))  # top left
        self.texture.draw(self.regions[1], Rect(
            area.x + self.insetAmt, area.y, area.width - (2*self.insetAmt), self.insetAmt))  # top
        self.texture.draw(self.regions[2], Rect(
            area.x + (area.width - self.insetAmt), area.y, self.insetAmt, self.insetAmt))  # top right

        self.texture.draw(self.regions[3], Rect(
            area.x, area.y + self.insetAmt, self.insetAmt, area.height - (2*self.insetAmt)))  # left
        self.texture.draw(self.regions[4], Rect(area.x + self.insetAmt, area.y + self.insetAmt,
                          area.width - (2*self.insetAmt), area.height - (2*self.insetAmt)))  # center
        self.texture.draw(self.regions[5], Rect(area.x + (area.width - self.insetAmt),
                          area.y + self.insetAmt, self.insetAmt, area.height - (2*self.insetAmt)))  # right

        self.texture.draw(self.regions[6], Rect(
            area.x, area.y + (area.height - self.insetAmt), self.insetAmt, self.insetAmt))  # top left
        self.texture.draw(self.regions[7], Rect(area.x + self.insetAmt, area.y + (
            area.height - self.insetAmt), area.width - (2*self.insetAmt), self.insetAmt))  # top
        self.texture.draw(self.regions[8], Rect(area.x + (area.width - self.insetAmt), area.y + (
            area.height - self.insetAmt), self.insetAmt, self.insetAmt))  # top right
