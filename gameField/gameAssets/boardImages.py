#images
import pygame

from gameField.gameAssets.boardConstants import LENGTH, WIDTH

SCREEN_RGB = [38, 38, 51]


GAME_ICON = pygame.image.load('gameField/gameAssets/shipIconP2.png')
EMPTY_HEX_IMG = pygame.image.load('gameField/gameAssets/emptyHex.png')
SHIP_HERE_HEX_IMG = pygame.image.load('gameField/gameAssets/shipHereHex.png')
ENEMY_SHIP_HERE_HEX_IMG = pygame.image.load('gameField/gameAssets/shipEnemyHereHex.png')
MOVE_OPTION_HEX_IMG = pygame.image.load('gameField/gameAssets/emptyHexMovable.png')
SHIP_TARGET_HEX_IMG = pygame.image.load('gameField/gameAssets/hexTarget.png')
CLICK_HEX_IMG = pygame.image.load('gameField/gameAssets/clickHex.png')
SPACE_BACKGROUND =  pygame.transform.scale(pygame.image.load('gameField/gameAssets/spaceBackground1.png'), (LENGTH, WIDTH))

# Note:
# SPACE_BACKGROUND is a downloaded image from https://www.reddit.com/r/PixelArt/comments/f1wg26/space_background/
# thanks to astrellon3 