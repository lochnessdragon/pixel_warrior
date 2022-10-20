import pygame
from pygame.locals import *
import math
from utils import sign
from Spriteset import Spriteset


# TODO: add more comments
# TODO: restructure class
class Entity(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet : Spriteset, animator):
        super().__init__()
        self.sprite_id = 0
        self.sprite_sheet = sprite_sheet
        self.rect = Rect(0, 0, self.sprite_sheet.sprite_width, self.sprite_sheet.sprite_height)
        self.rect.center = (100, 100)

        self.isFacingLeft = False
        self.velocity = [0, 0]
        self.maxSpeed = 5
        self.decelerationFactor = 0.5
        self.animator = animator

    def update(self, frameTime, tilemap):
        reduced_frame_time = (frameTime / 25)

        # check if applying the velocity would make the player hit a wall
        vTiles = tilemap.getSolidTilesV(
            self.rect.center[0], self.rect.center[1])
        collideIndex = self.rect.move(
            0, self.velocity[1] * reduced_frame_time).collidelist(vTiles)
        if collideIndex > -1:
            # the player collides with a rect on the y axis, avoid this!
            self.velocity[1] = 0
            # this code would break if the player and the tiles were different sizes
            self.rect.centery = vTiles[collideIndex].centery + (
                tilemap.tileset.sprite_height * (-1 if vTiles[collideIndex].centery > self.rect.centery else 1))

        hTiles = tilemap.getSolidTilesH(
            self.rect.center[0], self.rect.center[1])
        collideIndex = self.rect.move(
            self.velocity[0] * reduced_frame_time, 0).collidelist(hTiles)
        if collideIndex > -1:
            # avoid the player moving on the x axis
            self.velocity[0] = 0
            # this code would break if the player and the tiles were different sizes
            self.rect.centerx = vTiles[collideIndex].centerx + (
                tilemap.tileset.sprite_width * (-1 if vTiles[collideIndex].centerx > self.rect.centerx else 1))

        # apply velocity
        self.rect.move_ip(
            self.velocity[0] * reduced_frame_time, self.velocity[1] * reduced_frame_time)

        # update animation
        self.sprite_id = self.animator.update(frameTime, self)

        # cap entity's velocity
        self.velocity[0] = max(
            min(self.velocity[0], self.maxSpeed), -self.maxSpeed)
        self.velocity[1] = max(
            min(self.velocity[1], self.maxSpeed), -self.maxSpeed)

        # apply deceleration
        self.velocity[0] = sign(self.velocity[0]) * max(
            (abs(self.velocity[0]) - (self.decelerationFactor * reduced_frame_time)), 0)
        self.velocity[1] = sign(self.velocity[1]) * max(
            (abs(self.velocity[1]) - (self.decelerationFactor * reduced_frame_time)), 0)

    def draw(self, camera):
        # apply camera offset to entity pos
        self.sprite_sheet.drawSprite(
            self.sprite_id, self.rect.move(-camera.pos.x, -camera.pos.y), flipX=self.isFacingLeft)
