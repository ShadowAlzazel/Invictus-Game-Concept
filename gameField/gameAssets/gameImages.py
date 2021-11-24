import pygame
from . gameConstants import LENGTH, WIDTH

#----------------------------IMAGES-----------------------------------------

GAME_ICON = pygame.image.load('gameField/gameAssets/shipIconP2.png')

#normal hexes
EMPTY_HEX_IMG = pygame.image.load('gameField/gameAssets/emptyHex.png')
ASCS_SHIP_HEX_IMG = pygame.image.load('gameField/gameAssets/ASCSshipHex.png')
XNFF_SHIP_HEX_IMG = pygame.image.load('gameField/gameAssets/XNFFshipHex.png')

#Animated Hexes
GRID_HEX_BASE_0 = pygame.image.load('gameField/gameAssets/hexTemp6.png')
GRID_HEX_ANI_B0 = pygame.image.load('gameField/gameAssets/hexTemp5.png')
GRID_HEX_ANI_BASE = pygame.image.load('gameField/gameAssets/hexBase2.png')
GRID_HEX_ANI_EMPTY = pygame.image.load('gameField/gameAssets/hexEmpty3.png')
GRID_HEX_ANI_ENEMY = pygame.image.load('gameField/gameAssets/hexEnemy.png')
GRID_HEX_ANI_ALLY =  pygame.image.load('gameField/gameAssets/hexAlly.png')
GRID_HEX_ANI_CLICK = pygame.image.load('gameField/gameAssets/hexClick.png')
GRID_HEX_ANI_MOVE = pygame.image.load('gameField/gameAssets/hexMove.png')
GRID_HEX_ANI_TARGET = pygame.image.load('gameField/gameAssets/hexTarget.png')

#Fonts
FONT_1A = pygame.image.load('gameField/gameAssets/font1div.png')
FONT_2A = pygame.image.load('gameField/gameAssets/font2div.png')

# Note:
# SPACE_BACKGROUND is a downloaded image from https://www.reddit.com/r/PixelArt/comments/f1wg26/space_background/
# thanks to astrellon3 
SPACE_BACKGROUND = pygame.image.load('gameField/gameAssets/spaceBackground1.png')
FIT_SPACE = pygame.transform.smoothscale(SPACE_BACKGROUND, (LENGTH, WIDTH))