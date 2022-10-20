import pygame
from pygame.locals import *
from Entity import Entity

class FollowCamera:
    def __init__(self, followObj: Entity, window, bounds):
        self.pos = pygame.Vector2(0, 0)
        self.view_center = pygame.Vector2(window.size[0] // 2, window.size[1] // 2)
        self.view_size = pygame.Vector2(window.size[0], window.size[1])
        self.follow = followObj

        self.bounds = bounds

    def update(self, frameTime):
        # calculate move vector
        # move smoothing

        # apply move
        self.pos = self.follow.rect.center - self.view_center

        # restrict camera to bounds
        self.pos.x = min(max(self.pos.x, self.bounds.x), self.bounds.width - self.view_size.x)
        self.pos.y = min(max(self.pos.y, self.bounds.y), self.bounds.height - self.view_size.y)

    def resize(self, width, height):
        self.view_center.x = width // 2
        self.view_center.y = height // 2

        self.view_size.x = width
        self.view_size.y = height

    def getX(self):
        return self.pos.x
    def getY(self):
        return self.pos.y
