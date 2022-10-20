import pygame
from pygame._sdl2 import Texture, Renderer
from pygame.locals import *

class CustomCursor(pygame.sprite.Sprite):
    def __init__(self, renderer: Renderer, cursorFilename):
        super().__init__()
        self.texture = Texture.from_surface(renderer, pygame.image.load(cursorFilename))
        self.rect = self.texture.get_rect()
        pygame.mouse.set_visible(False)
        
    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def draw(self):
        if pygame.mouse.get_focused():
            self.texture.draw(dstrect = self.rect)
