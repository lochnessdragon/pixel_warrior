import pygame
from pygame.locals import *
from pygame._sdl2 import Texture, Renderer
import math

"""
Spriteset:
    A joint tilesheet/spritemap class.
"""
class Spriteset():
    def __init__(self, renderer: Renderer, spritesetName, sprite_width, sprite_height):
        self.texture = Texture.from_surface(renderer, pygame.image.load(spritesetName))
        self.width = self.texture.width
        self.height = self.texture.height
        self.sprite_width = sprite_width
        self.sprite_height = sprite_height

        # check if the tile width and tile height actually fit into the tilset width/height
        if self.width % self.sprite_width != 0 or self.height % self.sprite_height != 0:
            raise ValueError("The provided tile widths and tile heights do not fit into the provided tilemap evenly")

        self.sprites_in_row = int(self.width / self.sprite_width)
        self.sprites_in_col = int(self.height / self.sprite_height)
        self.maxId = (self.sprites_in_row * self.sprites_in_col) - 1 # the max tile id is one less than the area of the tiles. (start the id at 0)

        self.src_regions = []

        # create array of surfaces for lookups later
        for y in range(self.sprites_in_col):
            for x in range(self.sprites_in_row):
                self.src_regions.append(pygame.Rect(x * self.sprite_width, y * self.sprite_height, self.sprite_width, self.sprite_height))
        
    def getSpriteRect(self, id) -> pygame.Rect:
        if id < 0 or id > self.maxId:
            raise ValueError("Tile id: " + id + " is out of bounds!")

        return self.src_regions[id]
    
    def drawSprite(self, id: int, area: pygame.Rect, angle: int = 0, flipX: bool = False, flipY: bool = False) -> None:
        rect = self.getSpriteRect(id)

        self.texture.draw(rect, area, angle, flipX=flipX, flipY=flipY)
