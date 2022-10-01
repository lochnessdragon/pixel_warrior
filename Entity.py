import pygame
from pygame.locals import *
import math
from utils import sign


# TODO: add more comments
# TODO: restructure class
class Entity(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, animator):
        super().__init__()
        self.image = sprite_sheet.getSprite(0)
        self.sprite_sheet = sprite_sheet
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)
        self.isFacingRight = True
        self.velocity = [0, 0]
        self.maxSpeed = 5
        self.decelerationFactor = 0.5
        self.animator = animator

    def update(self, frameTime, tilemap):
        reduced_frame_time = (frameTime / 25)

        # cap entity's velocity
        self.velocity[0] = max(min(self.velocity[0], self.maxSpeed), -self.maxSpeed)
        self.velocity[1] = max(min(self.velocity[1], self.maxSpeed), -self.maxSpeed)

        # check if applying the velocity would make the player hit a wall
        vTiles = tilemap.getSolidTilesV(self.rect.center[0], self.rect.center[1])
        collideIndex = self.rect.move(0, self.velocity[1] * reduced_frame_time).collidelist(vTiles)
        if collideIndex > -1:
            # the player collides with a rect on the y axis, avoid this!
            self.velocity[1] = 0
            self.rect.centery = vTiles[collideIndex].centery + (tilemap.tileset.sprite_height * (-1 if vTiles[collideIndex].centery > self.rect.centery else 1)) # this code would break if the player and the tiles were different sizes


        hTiles = tilemap.getSolidTilesH(self.rect.center[0], self.rect.center[1])
        collideIndex = self.rect.move(self.velocity[0] * reduced_frame_time, 0).collidelist(hTiles)
        if collideIndex > -1:
            # avoid the player moving on the x axis
            self.velocity[0] = 0
            self.rect.centerx = vTiles[collideIndex].centerx + (tilemap.tileset.sprite_width * (-1 if vTiles[collideIndex].centerx > self.rect.centerx else 1)) # this code would break if the player and the tiles were different sizes

        # apply velocity
        self.rect.move_ip(self.velocity[0] * reduced_frame_time, self.velocity[1] * reduced_frame_time)

        # update animation
        self.image = self.sprite_sheet.getSprite(self.animator.update(frameTime, self))

        # apply deceleration
        self.velocity[0] = sign(self.velocity[0]) * max((abs(self.velocity[0]) - (self.decelerationFactor * reduced_frame_time)), 0)
        self.velocity[1] = sign(self.velocity[1]) * max((abs(self.velocity[1]) - (self.decelerationFactor * reduced_frame_time)), 0)

    def draw(self, surface, camera):
        flippedImage = self.image
        if not self.isFacingRight:
            flippedImage = pygame.transform.flip(self.image, True, False)
        surface.blit(flippedImage, self.rect.topleft - camera.pos) # apply camera offset to entity offset
