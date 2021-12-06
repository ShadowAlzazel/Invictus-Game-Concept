import pygame
from . gameConstants import LENGTH, RES_X, RES_Y, WIDTH

#----------------------------IMAGES-----------------------------------------

GAME_ICON = pygame.image.load('gameField/gameAssets/shipIconP2.png')

#ship images
ASCS_SHIP_HEX_IMG = pygame.image.load('gameField/gameAssets/ASC_ship2_icon32.png')
XNFF_SHIP_HEX_IMG = pygame.image.load('gameField/gameAssets/XNF_ship2_icon32.png')

#Animated Hexes
GRID_HEX_ANI_BASE = pygame.image.load('gameField/gameAssets/hex_base_blue32.png')
GRID_HEX_ANI_EMPTY = pygame.image.load('gameField/gameAssets/hex_base_floati32.png')
GRID_HEX_ANI_ENEMY = pygame.image.load('gameField/gameAssets/hex_base_enemy32.png')
GRID_HEX_ANI_ALLY =  pygame.image.load('gameField/gameAssets/hex_base_ally32.png')
GRID_HEX_ANI_CLICK = pygame.image.load('gameField/gameAssets/hex_base_click32.png')
GRID_HEX_ANI_MOVE = pygame.image.load('gameField/gameAssets/hex_base_move32.png')
GRID_HEX_ANI_TARGET = pygame.image.load('gameField/gameAssets/hex_base_target32.png')

#Fonts
FONT_1A = pygame.image.load('gameField/gameAssets/font1div.png')
FONT_2A = pygame.image.load('gameField/gameAssets/font2div.png')

# Note:
# SPACE_BACKGROUND is a downloaded image from https://www.reddit.com/r/PixelArt/comments/f1wg26/space_background/
# thanks to astrellon3 
SPACE_BACKGROUND = pygame.image.load('gameField/gameAssets/spaceBackground1.png')
FIT_SPACE = pygame.transform.smoothscale(SPACE_BACKGROUND, (LENGTH, WIDTH))