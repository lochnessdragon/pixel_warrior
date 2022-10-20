import sys, os
import pygame
from pygame.locals import *
import pygame._sdl2.video
from Player import *
from CustomCursor import *
from Camera import *
from Spriteset import *
from Tilemap import *
import LevelGenerator
from AnimationStateMachine import *
from NPatchDrawing import *

pygame.init()

# define constants
FPS = 60
WHITE = (255, 255, 255)
BG = (118, 59, 54, 255)

clock = pygame.time.Clock()
assets_dir = os.path.dirname(__file__) + "/assets/"

# set up surface
window = pygame._sdl2.video.Window("Pixel Warrior", (640, 480))
window.resizable = True
renderer = pygame._sdl2.video.Renderer(window, accelerated = 1, vsync = True)

# light blue background
custom_cursor = CustomCursor(renderer, assets_dir + "ui/cursor.png")

# load fonts
debug_font = pygame.freetype.Font(assets_dir + "ui/fonts/Kenney Pixel.ttf", size=20)
draw_debug_ui = False

# game objects
wizard_spritesheet = Spriteset(renderer, assets_dir + "spritesheets/wizard.png", 16, 16)
idle_anim = PlayerIdleAnimation([0, 1], 1000)
walk_anim = PlayerWalkAnimation(list(range(2, 7)), 150)

idle_anim.walk_anim = walk_anim
walk_anim.idle_anim = idle_anim

player = Player(wizard_spritesheet, idle_anim, 20)

# create ui elements
testWin = NPatchWindow(renderer, assets_dir + "ui/window_npatch.png", 3)

# list of all tile ids that are solid
solid_tiles = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 22, 29, 30, 31, 54, 55, 56]
environment_tileset = Spriteset(renderer, assets_dir + "tilemaps/tilemap_environment.png", 16, 16)
map = LevelGenerator.generate_blank_map(32, 32, environment_tileset, solid_tiles)
camera = FollowCamera(player, window, pygame.Rect(0, 0, 512, 512))

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
                camera.resize(window.size[0], window.size[1])
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    window.destroy()
                    pygame.quit()
                    sys.exit()
                if event.key == K_x:
                    draw_debug_ui = not draw_debug_ui


        player.update(frameTime, map)
        camera.update(frameTime)
        custom_cursor.update()

        # render
        renderer.draw_color = BG
        renderer.clear()
        
        # render layers
        # background
        map.draw(camera)

        # foreground

        # players/sprites
        player.draw(camera)
        testWin.draw(pygame.Rect(100, 100, 200, 100))

        # draw ui
        if draw_debug_ui:
            debug_font.render_to(None, (0, 0), "Frame time: " + str(frameTime) + " ms", fgcolor = WHITE)
            debug_font.render_to(None, (0, 10), "Camera: (" + str(camera.pos.x) + ", " + str(camera.pos.y) + ")", fgcolor = WHITE)
            debug_font.render_to(None, (0, 20), f"Player Vel: {player.velocity}", fgcolor = WHITE)

        # draw cursor last
        custom_cursor.draw()

        # display
        renderer.present()
