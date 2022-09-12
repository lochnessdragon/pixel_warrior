import pygame
from pygame.locals import *
import random

class Tilemap(pygame.sprite.Sprite):
    def __init__(self, tileset, width, height):
        super().__init__()
        self.tileset = tileset
        self.width = width
        self.height = height
        self.tiles = [[0 for i in range(width)] for j in range(height)] # allocate empty array to initalize later

    def draw(self, surface, camera):
        for y in range(self.height):
            for x in range(self.width):
                surface.blit(self.tileset.getTile(self.tiles[y][x]), (x * self.tileset.tile_width, y * self.tileset.tile_height) - camera.pos)

    def getTile(self, x, y):
        if x < 0 or x > self.width:
            raise ValueError("The provided x is out of bounds!")
        if y < 0 or y > self.height:
            raise ValueError("The provided y is out of bounds!")

        return self.tiles[y][x]

    def setTile(self, x, y, id):
        if x < 0 or x > self.width:
            raise ValueError("The provided x is out of bounds!")
        if y < 0 or y > self.height:
            raise ValueError("The provided y is out of bounds!")

        self.tiles[y][x] = id
