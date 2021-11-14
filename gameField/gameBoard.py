#class for board display
import pygame
from gameField.gameAssets import *

GAME_ICON = pygame.image.load('gameField/gameAssets/shipIconP2.png')
EMPTY_HEX_IMG = pygame.image.load('gameField/gameAssets/emptyHex.png')
ASCS_SHIP_HEX_IMG = pygame.image.load('gameField/gameAssets/ASCSshipHex.png')
XNFF_SHIP_HEX_IMG = pygame.image.load('gameField/gameAssets/XNFFshipHex.png')
MOVE_OPTION_HEX_IMG = pygame.image.load('gameField/gameAssets/emptyHexMovable.png')
SHIP_TARGET_HEX_IMG = pygame.image.load('gameField/gameAssets/hexTarget.png')
CLICK_HEX_IMG = pygame.image.load('gameField/gameAssets/clickHex.png')
SPACE_BACKGROUND = pygame.image.load('gameField/gameAssets/spaceBackground1.png')

# Note:
# SPACE_BACKGROUND is a downloaded image from https://www.reddit.com/r/PixelArt/comments/f1wg26/space_background/
# thanks to astrellon3 

#----------------------------------------------------------------------
FIT_SPACE = pygame.transform.scale(SPACE_BACKGROUND, (LENGTH, WIDTH))


class spaceGameBoard:

    def __init__(self, l, w, hexSize):
        self.hexesLength = l
        self.hexesWidth = w
        self.hexSize = hexSize
        self.EMPTY_HEX_IMG = EMPTY_HEX_IMG
        self.ASCS_SHIP_HEX_IMG = ASCS_SHIP_HEX_IMG
        self.XNFF_SHIP_HEX_IMG = XNFF_SHIP_HEX_IMG
        self.MOVE_OPTION_HEX_IMG = MOVE_OPTION_HEX_IMG
        self.SHIP_TARGET_HEX_IMG = SHIP_TARGET_HEX_IMG
        self.CLICK_HEX_IMG = CLICK_HEX_IMG
        self.bordersColumnsY = (WIDTH - (self.hexSize * self.hexesWidth)) // 2
        self.bordersRowsX = (LENGTH - (self.hexSize * self.hexesLength)) // 2

    #draw hexes on board
    def drawHexes(self, gameWindow, operationSpace, shipHex=[]):
        gameWindow.blit(FIT_SPACE, (0, 0))
        shipClicked = False
        if shipHex and not shipHex.empty:
            targets = []
            aShip = shipHex.entity
            if aShip.gunsReady():
                targets = aShip.findTargets()
            shipClicked = True

        # e is for flipping the y coordinate
        e = self.hexesWidth
        n = 0
        for hex in operationSpace.starSpaceHexes: 
            #indent every second row
            i = 0 
            if not e % 2 == 0:
                i = self.hexSize // 2
            #y coordinate
            y = (self.bordersColumnsY) + ((e - 1) * self.hexSize)
            #x coordinate is a proportion of the screen
            x = (self.bordersRowsX) + (n * self.hexSize) + i - (self.hexSize // 2)
            if hex.empty:
                gameWindow.blit(self.EMPTY_HEX_IMG, (x, y))
                if shipClicked:
                    if hex in shipHex.neighbors and aShip.shipMovement != 0:
                        gameWindow.blit(self.MOVE_OPTION_HEX_IMG, (x, y))

            elif hex.entity.spaceEntity == 'shipObject':
                if hex.entity.command == 'ASCS':
                    gameWindow.blit(self.ASCS_SHIP_HEX_IMG, (x, y))
                elif hex.entity.command == 'XNFF':
                    gameWindow.blit(self.XNFF_SHIP_HEX_IMG, (x, y))

                if shipClicked:
                    if hex in targets:
                        gameWindow.blit(self.SHIP_TARGET_HEX_IMG, (x, y))
        
            if shipClicked:
                if hex.coord['hexNum'] == shipHex.coord['hexNum']:
                    gameWindow.blit(self.CLICK_HEX_IMG, (x, y))

            n += 1
            if n == self.hexesLength:
                e -= 1
                n = 0

    def zoomInHex(self):
        self.hexSize += 16
        self.scaleHexes(self.hexSize)

    def zoomOutHex(self):
        self.hexSize -= 16
        self.scaleHexes(self.hexSize)

    def getCoordMouse(self, mousePos):
        i = 0
        a, b = mousePos
        aActive = False
        bActive = False 
        column, row = 0, 0

        if b in range(self.bordersColumnsY, (self.hexSize * self.hexesWidth) + (self.bordersColumnsY)):
            bActive = True
            #reverse y coords
            row = abs(((b - self.bordersColumnsY) // self.hexSize) - self.hexesWidth) - 1

            #check even odd
            if ((b - self.bordersColumnsY) // self.hexSize) % 2 == 1:
                i = self.hexSize // 2  

        if a in range((self.bordersRowsX) - i, ((self.hexSize * self.hexesLength) + (self.bordersRowsX) - i)):
            aActive = True
            column = ((a - self.bordersRowsX) + i) // self.hexSize

        if aActive and bActive:
            indexCoord = (row * self.hexesLength) + column
            return indexCoord
        else:
            print("No Hexes In this space")
            return -1

    def scaleHexes(self, hexSize):
        self.EMPTY_HEX_IMG = pygame.transform.scale(EMPTY_HEX_IMG, (hexSize, hexSize))
        self.ASCS_SHIP_HEX_IMG = pygame.transform.scale(ASCS_SHIP_HEX_IMG, (hexSize, hexSize))
        self.XNFF_SHIP_HEX_IMG = pygame.transform.scale(XNFF_SHIP_HEX_IMG, (hexSize, hexSize))
        self.MOVE_OPTION_HEX_IMG = pygame.transform.scale(MOVE_OPTION_HEX_IMG, (hexSize, hexSize))
        self.SHIP_TARGET_HEX_IMG = pygame.transform.scale(SHIP_TARGET_HEX_IMG, (hexSize, hexSize))
        self.CLICK_HEX_IMG = pygame.transform.scale(CLICK_HEX_IMG, (hexSize, hexSize))
        self.ASCS_SHIP_HEX_IMG.convert()
        self.EMPTY_HEX_IMG.convert()
        self.XNFF_SHIP_HEX_IMG.convert()
        self.MOVE_OPTION_HEX_IMG.convert()
        self.SHIP_TARGET_HEX_IMG.convert()
        self.CLICK_HEX_IMG.convert()