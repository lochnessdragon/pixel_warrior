import pygame
from pygame.locals import *
from Entity import *

class Player(Entity):
    def __init__(self, sprite_sheet, animator, maxHealth):
        super().__init__(sprite_sheet, animator)
        self.speed = 2
        self.health = maxHealth
        self.maxHealth = maxHealth

    def update(self, frameTime, tilemap):
        reduced_frame_time = (frameTime / 25)

        # respond to player input
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.velocity[0] -= self.speed * reduced_frame_time
            if self.isFacingRight:
                self.isFacingRight = False
        if pressed_keys[K_RIGHT]:
            self.velocity[0] += self.speed * reduced_frame_time
            if not self.isFacingRight:
                self.isFacingRight = True
        if pressed_keys[K_UP]:
            self.velocity[1] -= self.speed * reduced_frame_time
        if pressed_keys[K_DOWN]:
            self.velocity[1] += self.speed * reduced_frame_time

        # call super method to handle physics and animations
        super().update(frameTime, tilemap)
