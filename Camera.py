import pygame
from pygame.locals import *

class FollowCamera:
    def __init__(self, followObj, view, bounds):
        self.pos = pygame.Vector2(0, 0)
        self.view_center = pygame.Vector2(view.get_width() // 2, view.get_height() // 2)
        self.view_size = pygame.Vector2(view.get_width(), view.get_height())
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
