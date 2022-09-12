import pygame
from pygame.locals import *
import math
from utils import sign

class Player(pygame.sprite.Sprite):
    def __init__(self, assets_dir):
        super().__init__()
        self.image = pygame.image.load(assets_dir + "Tiles/tile_0084.png").convert()
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)
        self.isFacingRight = True
        self.velocity = [0, 0]
        self.speed = 2
        self.maxSpeed = 5
        self.decelerationFactor = 0.5

    def update(self, frameTime):
        frameTime = (frameTime / 25)

        # respond to player input
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.velocity[0] -= self.speed * frameTime
            if self.isFacingRight:
                self.image = pygame.transform.flip(self.image, True, False).convert() # I don't really know if this convert is necessary
                self.isFacingRight = False
        if pressed_keys[K_RIGHT]:
            self.velocity[0] += self.speed * frameTime
            if not self.isFacingRight:
                self.image = pygame.transform.flip(self.image, True, False).convert()
                self.isFacingRight = True
        if pressed_keys[K_UP]:
            self.velocity[1] -= self.speed * frameTime
        if pressed_keys[K_DOWN]:
            self.velocity[1] += self.speed * frameTime

        # cap player's velocity
        self.velocity[0] = max(min(self.velocity[0], self.maxSpeed), -self.maxSpeed)
        self.velocity[1] = max(min(self.velocity[1], self.maxSpeed), -self.maxSpeed)

        # apply velocity
        self.rect.move_ip(self.velocity[0] * frameTime, self.velocity[1] * frameTime)

        # apply deceleration
        self.velocity[0] = sign(self.velocity[0]) * max((abs(self.velocity[0]) - (self.decelerationFactor * frameTime)), 0)
        self.velocity[1] = sign(self.velocity[1]) * max((abs(self.velocity[1]) - (self.decelerationFactor * frameTime)), 0)

    def draw(self, surface, camera):
        surface.blit(self.image, self.rect.topleft - camera.pos)#.move(camera.getX(), camera.getY()))
