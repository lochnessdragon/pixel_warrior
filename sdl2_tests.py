import sys

import pygame
import pygame._sdl2.video
from pygame.locals import *
from pygame import Rect

class NPatch:
    def __init__(self, filename: str, insetAmt: int, renderer: pygame._sdl2.video.Renderer):
        self.renderer = renderer
        self.texture = pygame._sdl2.video.Texture.from_surface(renderer, pygame.image.load(filename))
        self.width = self.texture.width
        self.height = self.texture.height
        self.insetAmt = insetAmt

        self.regions = []
        # calculate src regions
        self.regions.append(Rect(0, 0, insetAmt, insetAmt)) # top left
        self.regions.append(Rect(insetAmt, 0, self.width - (2*insetAmt), insetAmt)) # top
        self.regions.append(Rect(self.width - insetAmt, 0, insetAmt, insetAmt)) # top right

        self.regions.append(Rect(0, insetAmt, insetAmt, self.height - (2*insetAmt))) # left
        self.regions.append(Rect(insetAmt, insetAmt, self.width - (2*insetAmt), self.height - (2*insetAmt))) # center
        self.regions.append(Rect(self.width - insetAmt, insetAmt, insetAmt, self.height - (2*insetAmt))) # right
        
        self.regions.append(Rect(0, self.height - insetAmt, insetAmt, insetAmt)) # bottom left
        self.regions.append(Rect(insetAmt, self.height - insetAmt, self.width - (2 * insetAmt), insetAmt)) # bottom
        self.regions.append(Rect(self.width - insetAmt, self.height - insetAmt, insetAmt, insetAmt)) # bottom right

    def draw(self, area: Rect):
        self.renderer.blit(self.texture, Rect(area.x, area.y, self.insetAmt, self.insetAmt), self.regions[0]) # top left
        self.renderer.blit(self.texture, Rect(area.x + self.insetAmt, area.y, area.width - (2*self.insetAmt), self.insetAmt), self.regions[1]) # top 
        self.renderer.blit(self.texture, Rect(area.x + (area.width - self.insetAmt), area.y, self.insetAmt, self.insetAmt), self.regions[2]) # top right

        self.renderer.blit(self.texture, Rect(area.x, area.y + self.insetAmt, self.insetAmt, area.height - (2*self.insetAmt)), self.regions[3]) # left
        self.renderer.blit(self.texture, Rect(area.x + self.insetAmt, area.y + self.insetAmt, area.width - (2*self.insetAmt), area.height - (2*self.insetAmt)), self.regions[4]) # center
        self.renderer.blit(self.texture, Rect(area.x + (area.width - self.insetAmt), area.y + self.insetAmt, self.insetAmt, area.height - (2*self.insetAmt)), self.regions[5]) # right

        self.renderer.blit(self.texture, Rect(area.x, area.y + (area.height - self.insetAmt), self.insetAmt, self.insetAmt), self.regions[6]) # bottom left
        self.renderer.blit(self.texture, Rect(area.x + self.insetAmt, area.y + (area.height - self.insetAmt), area.width - (2*self.insetAmt), self.insetAmt), self.regions[7]) # bottom 
        self.renderer.blit(self.texture, Rect(area.x + (area.width - self.insetAmt), area.y + (area.height - self.insetAmt), self.insetAmt, self.insetAmt), self.regions[8]) # bottom right

window = pygame._sdl2.video.Window("NPatch Test", (640, 480))
renderer = pygame._sdl2.video.Renderer(window, accelerated = 1)
uiBlock = NPatch("assets/ui/window_npatch.png", 3, renderer)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            window.destroy()
            pygame.quit()
            sys.exit()

    mouseX, mouseY = pygame.mouse.get_pos()
    mouseX = max(mouseX, 100)
    mouseY = max(mouseY, 100)
    
    renderer.draw_color = (150, 150, 45, 255)
    renderer.clear()
    uiBlock.draw(Rect(100, 100, mouseX - 100, mouseY - 100))
    renderer.present()