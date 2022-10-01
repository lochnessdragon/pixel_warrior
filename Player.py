import pygame
from pygame.locals import *
from Entity import *

class Player(Entity):
    def __init__(self, sprite_sheet, animator):
        super().__init__(sprite_sheet, animator)
        self.speed = 2

    def update(self, frameTime, tilemap):
        reduced_frame_time = (frameTime / 25)

        # respond to player input
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.velocity[0] -= self.speed * reduced_frame_time
            if self.isFacingRight:
                #self.image = pygame.transform.flip(self.image, True, False).convert() # I don't really know if this convert is necessary
                self.isFacingRight = False
        if pressed_keys[K_RIGHT]:
            self.velocity[0] += self.speed * reduced_frame_time
            if not self.isFacingRight:
                #self.image = pygame.transform.flip(self.image, True, False).convert()
                self.isFacingRight = True
        if pressed_keys[K_UP]:
            self.velocity[1] -= self.speed * reduced_frame_time
        if pressed_keys[K_DOWN]:
            self.velocity[1] += self.speed * reduced_frame_time

        # call super method to handle physics
        super().update(frameTime, tilemap)
