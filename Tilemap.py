import pygame
from pygame.locals import *
import random


class Tilemap(pygame.sprite.Sprite):
    def __init__(self, tileset, width, height):
        super().__init__()
        self.pos = pygame.Vector2(0, 0)
        self.tileset = tileset
        self.width = width
        self.height = height
        self.tiles = [[0 for i in range(width)] for j in range(
            height)]  # allocate empty array to initalize later
        self.solid_tiles = []

    def draw(self, camera):
        for y in range(self.height):
            for x in range(self.width):
                self.tileset.drawSprite(self.tiles[y][x], Rect((x * self.tileset.sprite_width) - camera.pos.x, (
                    y * self.tileset.sprite_height) - camera.pos.y, self.tileset.sprite_width, self.tileset.sprite_height))

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

    def setSolid(self, solid_tiles_list):
        self.solid_tiles = solid_tiles_list

    """
     getSolidTilesV:
        returns rects for the solid tiles that are above and below a certain point(non-localized space)
    """

    def getSolidTilesV(self, x, y):
        tile_rect = pygame.Rect(
            0, 0, self.tileset.sprite_width, self.tileset.sprite_height)
        result = []
        # convert x and y to a localized tile coordinate
        localX = int(x - self.pos.x)
        localY = int(y - self.pos.y)
        localX = localX // self.tileset.sprite_width
        localY = localY // self.tileset.sprite_width
        for y in range(localY - 1, localY + 2, 2):
            if (y < 0 or y > self.height):
                continue
            for x in range(localX - 1, localX + 2):
                if (x < 0 or x > self.width):
                    continue
                #print("Checking:", x, ",", y)
                if self.getTile(x, y) in self.solid_tiles:
                    # add tile rect to the result
                    result.append(tile_rect.move((x * self.tileset.sprite_width) +
                                  self.pos.x, (y * self.tileset.sprite_height) + self.pos.y))
        return result

    """
     getSolidTilesH:
        returns the solid tiles that are left and right of a certain point(non-localized space)
    """

    def getSolidTilesH(self, x, y):
        tile_rect = pygame.Rect(
            0, 0, self.tileset.sprite_width, self.tileset.sprite_height)
        result = []
        # convert x and y to a localized tile coordinate
        localX = int(x - self.pos.x)
        localY = int(y - self.pos.y)
        localX = localX // self.tileset.sprite_width
        localY = localY // self.tileset.sprite_width
        for y in range(localY - 1, localY + 2):
            if (y < 0 or y > self.height):
                continue
            for x in range(localX - 1, localX + 2, 2):
                if (x < 0 or x > self.width):
                    continue
                #print("Checking:", x, ",", y)
                if self.getTile(x, y) in self.solid_tiles:
                    # add tile rect to the result
                    result.append(tile_rect.move((x * self.tileset.sprite_width) +
                                  self.pos.x, (y * self.tileset.sprite_height) + self.pos.y))
        return result
