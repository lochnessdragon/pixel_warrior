import pygame
from pygame.locals import *
import math

class Tileset():
    def __init__(self, tilesetName, tile_width, tile_height):
        self.image = pygame.image.load(tilesetName).convert()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.tile_width = tile_width
        self.tile_height = tile_height

        # check if the tile width and tile height actually fit into the tilset width/height
        if self.width % self.tile_width != 0 or self.height % self.tile_height != 0:
            raise ValueError("The provided tile widths and tile heights do not fit into the provided tilemap evenly")

        self.tiles_in_row = int(self.width / self.tile_width)
        self.tiles_in_col = int(self.height / self.tile_height)
        self.maxId = (self.tiles_in_row * self.tiles_in_col) - 1 # the max tile id is one less than the area of the tiles. (start the id at 0)

        self.surfaces = []

        # create array of surfaces for lookups later
        for y in range(self.tiles_in_col):
            for x in range(self.tiles_in_row):
                self.surfaces.append(self.image.subsurface(pygame.Rect(x * self.tile_width, y * self.tile_height, self.tile_width, self.tile_height)))

    def getTile(self, id):
        if id < 0 or id > self.maxId:
            raise ValueError("Tile id: " + id + " is out of bounds!")

        return self.surfaces[id]
