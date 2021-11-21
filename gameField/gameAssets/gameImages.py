import pygame
from . gameConstants import LENGTH, WIDTH

#----------------------------IMAGES-----------------------------------------

GAME_ICON = pygame.image.load('gameField/gameAssets/shipIconP2.png')

#normal hexes
EMPTY_HEX_IMG = pygame.image.load('gameField/gameAssets/emptyHex.png')
ASCS_SHIP_HEX_IMG = pygame.image.load('gameField/gameAssets/ASCSshipHex.png')
XNFF_SHIP_HEX_IMG = pygame.image.load('gameField/gameAssets/XNFFshipHex.png')
MOVE_OPTION_HEX_IMG = pygame.image.load('gameField/gameAssets/emptyHexMovable.png')
SHIP_TARGET_HEX_IMG = pygame.image.load('gameField/gameAssets/hexTarget.png')
CLICK_HEX_IMG = pygame.image.load('gameField/gameAssets/clickHex.png')

#Animated Hexes
ANI_HEX_1 = pygame.image.load('gameField/gameAssets/gridAni_1.png')
ANI_HEX_2 = pygame.image.load('gameField/gameAssets/gridAni_2.png')
ANI_HEX_3 = pygame.image.load('gameField/gameAssets/gridAni_3.png')
ANI_HEX_4 = pygame.image.load('gameField/gameAssets/gridAni_4.png')
ANI_HEX_5 = pygame.image.load('gameField/gameAssets/gridAni_5.png')
ANI_HEX_6 = pygame.image.load('gameField/gameAssets/gridAni_6.png')
ANI_HEX_7 = pygame.image.load('gameField/gameAssets/gridAni_7.png')

#Background
SPACE_BACKGROUND = pygame.image.load('gameField/gameAssets/spaceBackground1.png')
FIT_SPACE = pygame.transform.smoothscale(SPACE_BACKGROUND, (LENGTH, WIDTH))