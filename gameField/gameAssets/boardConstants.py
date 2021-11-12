#game constants
import pygame

LENGTH = 1000
WIDTH = 750
CENTER_X = LENGTH // 2
CENTER_Y = WIDTH // 2

HEX_SIZE = 0

FPS = 60

SCREEN_RGB = [38, 38, 51]


GAME_ICON = pygame.image.load('gameField/gameAssets/shipIconP2.png')
HEX_Y_IMG = pygame.image.load('gameField/gameAssets/emptyHex.png')
HEX_ENTF_IMG = pygame.image.load('gameField/gameAssets/shipHereHex.png')