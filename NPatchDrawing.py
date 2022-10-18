import pygame
from pygame import Rect
from pygame.locals import *

class NPatchWindow():
    def __init__(self, filename, insetAmt):
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.insetAmt = insetAmt

        # setup the different regions required for the nine patches
        self.regions = []
        self.regions.append(Rect(0, 0, insetAmt, insetAmt)) # top left
        self.regions.append(Rect(insetAmt, 0, self.width - (2*insetAmt), insetAmt)) # top
        self.regions.append(Rect(self.width - insetAmt, 0, insetAmt, insetAmt)) # top right

        self.regions.append(Rect(0, insetAmt, insetAmt, self.height - (2*insetAmt))) # left
        self.regions.append(Rect(insetAmt, insetAmt, self.width - (2*insetAmt), self.height - (2*insetAmt))) # center
        self.regions.append(Rect(self.width - insetAmt, insetAmt, insetAmt, self.height - (2*insetAmt))) # right
        
        self.regions.append(Rect(0, self.height - insetAmt, insetAmt, insetAmt)) # bottom left
        self.regions.append(Rect(insetAmt, self.height - insetAmt, self.width - (2 * insetAmt), insetAmt)) # bottom
        self.regions.append(Rect(self.width - insetAmt, self.height - insetAmt, insetAmt, insetAmt)) # bottom right

    def draw(self, framebuffer: pygame.Surface, area: pygame.Rect):
        modified_image = pygame.transform.scale(self.image, (area.width, area.height))
        
        framebuffer.blit(self.image, area, self.regions[0]) # top left
        framebuffer.blit(self.image, area.move(self.insetAmt, 0), self.regions[1], SCALED) # top
        framebuffer.blit(self.image, area.move(area.width - self.insetAmt, 0), self.regions[2]) # top right
        
        framebuffer.blit(self.image, area.move(0, self.insetAmt), self.regions[3], SCALED) # left
        framebuffer.blit(self.image, area.move(self.insetAmt, self.insetAmt), self.regions[4], SCALED) # center
        framebuffer.blit(self.image, area.move(area.width - self.insetAmt, self.insetAmt), self.regions[5], SCALED) # right

        framebuffer.blit(self.image, area.move(0, area.height - self.insetAmt), self.regions[6]) # bottom left
        framebuffer.blit(self.image, area.move(self.insetAmt, area.height - self.insetAmt), self.regions[7], SCALED) # bottom
        framebuffer.blit(self.image, area.move(area.width - self.insetAmt, area.height - self.insetAmt), self.regions[8]) # bottom right