import pygame
from pygame.locals import *
import math

"""
Spriteset:
    A joint tilesheet/spritemap class.
"""
class Spriteset():
    def __init__(self, spritesetName, sprite_width, sprite_height):
        self.image = pygame.image.load(spritesetName).convert_alpha()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.sprite_width = sprite_width
        self.sprite_height = sprite_height

        # check if the tile width and tile height actually fit into the tilset width/height
        if self.width % self.sprite_width != 0 or self.height % self.sprite_height != 0:
            raise ValueError("The provided tile widths and tile heights do not fit into the provided tilemap evenly")

        self.sprites_in_row = int(self.width / self.sprite_width)
        self.sprites_in_col = int(self.height / self.sprite_height)
        self.maxId = (self.sprites_in_row * self.sprites_in_col) - 1 # the max tile id is one less than the area of the tiles. (start the id at 0)

        self.surfaces = []

        # create array of surfaces for lookups later
        for y in range(self.sprites_in_col):
            for x in range(self.sprites_in_row):
                self.surfaces.append(self.image.subsurface(pygame.Rect(x * self.sprite_width, y * self.sprite_height, self.sprite_width, self.sprite_height)))

    def getSprite(self, id):
        if id < 0 or id > self.maxId:
            raise ValueError("Tile id: " + id + " is out of bounds!")

        return self.surfaces[id]
