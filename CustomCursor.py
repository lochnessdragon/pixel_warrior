import pygame
from pygame.locals import *

class CustomCursor(pygame.sprite.Sprite):
    def __init__(self, cursorFilename):
        super().__init__()
        self.image = pygame.image.load(cursorFilename)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def draw(self, surface):
        if pygame.mouse.get_focused():
            surface.blit(self.image, self.rect)
