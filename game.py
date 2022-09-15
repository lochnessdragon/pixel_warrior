import sys, os
import pygame
from pygame.locals import *
from Player import *
from CustomCursor import *
from Camera import *
from Tileset import *
from Tilemap import *
import LevelGenerator

pygame.init()

FPS = 60
clock = pygame.time.Clock()
assets_dir = os.path.dirname(__file__) + "/assets/"

# set up surface
window = pygame.display.set_mode((600, 400), RESIZABLE, vsync = True)
back_buffer = pygame.surface.Surface((window.get_width() / 2, window.get_height() / 2))

# light blue background
BG = (118, 59, 54)
window.fill(BG)
pygame.display.set_caption("Pixel Warrior")
pygame.mouse.set_visible(False)
custom_cursor = CustomCursor(assets_dir + "ui/cursor.png")

# load fonts
debug_font = pygame.freetype.Font(assets_dir + "ui/fonts/Kenney Pixel.ttf", size=20)
draw_debug_ui = False

# game objects
player = Player(assets_dir)

# list of all tile ids that are solid
solid_tiles = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 22, 29, 30, 31, 54, 55, 56]
environment_tileset = Tileset(assets_dir + "tilemaps/tilemap_environment.png", 16, 16)
map = LevelGenerator.generate_blank_map(32, 32, environment_tileset, solid_tiles)
camera = FollowCamera(player, back_buffer, pygame.Rect(0, 0, 512, 512))

# game loop
while True:
        frameTime = clock.tick(FPS)

        # tick
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == WINDOWRESIZED or event.type == WINDOWSIZECHANGED:
                # resize smaller buffer
                back_buffer = pygame.Surface((event.x // 2, event.y // 2))
                camera.resize(back_buffer.get_width(), back_buffer.get_height())
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_x:
                    draw_debug_ui = not draw_debug_ui


        player.update(frameTime, map)
        camera.update(frameTime)
        custom_cursor.update()

        # render
        back_buffer.fill(BG)
        # render layers
        # background
        map.draw(back_buffer, camera)

        # foreground

        # players/sprites
        player.draw(back_buffer, camera)

        pygame.transform.scale(back_buffer, (window.get_width(), window.get_height()), window)

        # draw ui
        if draw_debug_ui:
            debug_font.render_to(window, (0, 0), "Frame time: " + str(frameTime) + " ms", fgcolor = (255, 255, 255))
            debug_font.render_to(window, (0, 10), "Camera: (" + str(camera.pos.x) + ", " + str(camera.pos.y) + ")", fgcolor = (255, 255, 255))

        # draw cursor last
        custom_cursor.draw(window)

        # display
        pygame.display.update()
