import pygame
from pygame.locals import *

class FollowCamera:
    def __init__(self, followObj, view, bounds):
        self.pos = pygame.Vector2(0, 0)
        self.view_center = pygame.Vector2(view.get_width() // 2, view.get_height() // 2)
        self.follow = followObj

    def update(self, frameTime):
        # calculate move vector
        # move smoothing

        # restrict camera to bounds

        # apply move
        self.pos = self.follow.rect.center - self.view_center

    def resize(self, width, height):
        self.view_center.x = width // 2
        self.view_center.y = height // 2

    def getX(self):
        return self.pos.x
    def getY(self):
        return self.pos.y
