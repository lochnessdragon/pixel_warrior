import pygame
from pygame.locals import *

from Tilemap import *
import random

def generate_blank_map(width, height, tileset):
    map = Tilemap(tileset, width, height)
    for y in range(height):
        for x in range(width):
            isYMin = y == 0
            isYMax = y == (width - 1)
            isXMin = x == 0
            isXMax = x == (height - 1)
            if isYMin:
                map.setTile(x, y, 2) # top panel
            elif isYMax:
                    map.setTile(x, y, 14) # bottom panel
            elif isXMin:
                map.setTile(x, y, 7) # side panel left
            elif isXMax:
                map.setTile(x, y, 9) # side panel right
            elif y == 1 and not isXMin or isXMax:
                map.setTile(x, y, random.choices([8, 22, 16, 17], weights=[50, 50, 5, 5])[0]) # regular wall, regular wall 2, dungeon wall, banner wall
            else:
                map.setTile(x, y, random.choices([24, 25, 23, 48], weights=[70, 10, 1, 10])[0]) # basic ground, speckled ground, spike trap, stones

    # override 4 corners
    map.setTile(0, 0, 1)
    map.setTile(0, height - 1, 13)
    map.setTile(width - 1, 0, 3)
    map.setTile(width - 1, height - 1, 15)

    return map
