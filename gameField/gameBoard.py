#class for board display
import pygame
from pygame.transform import rotate
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
FIT_SPACE = pygame.transform.smoothscale(SPACE_BACKGROUND, (LENGTH, WIDTH))


class spaceGameBoard:

    def __init__(self, l, w, hexSize):
        self.hexesLength = l
        self.hexesWidth = w
        self.hexSize = hexSize
        #movement variables
        self.windowMoveX = 0
        self.windowMoveY = 0
        self.centerHex = -1
        self.bordersColumnsY = ((WIDTH - (self.hexSize * self.hexesWidth)) // 2) - self.windowMoveY
        self.bordersRowsX = ((LENGTH - (self.hexSize * self.hexesLength)) // 2) + self.windowMoveX
        #images
        self.EMPTY_HEX_IMG = EMPTY_HEX_IMG
        self.ASCS_SHIP_HEX_IMG = ASCS_SHIP_HEX_IMG
        self.XNFF_SHIP_HEX_IMG = XNFF_SHIP_HEX_IMG
        self.MOVE_OPTION_HEX_IMG = MOVE_OPTION_HEX_IMG
        self.SHIP_TARGET_HEX_IMG = SHIP_TARGET_HEX_IMG
        self.CLICK_HEX_IMG = CLICK_HEX_IMG
        self.scaleHexes(self.hexSize)

    #draw hexes on board
    def drawHexes(self, gameWindow, operationSpace, shipHex=[]):
        gameWindow.blit(FIT_SPACE, (0, 0))
        #check of shipClicked
        shipClicked = False
        if shipHex and not shipHex.empty:
            targets = []
            aShip = shipHex.entity
            if aShip.gunsReady():
                targets = aShip.findTargets()
            shipClicked = True

        if self.centerHex > -1:
            c = 0
            if (self.centerHex // self.hexesLength) % 2 != 0:
                c = 32
            self.windowMoveX = int((self.hexesLength / 2) - ((self.centerHex % self.hexesLength) + 1)) * self.hexSize + c
            self.windowMoveY = int(((self.centerHex // self.hexesLength)) - (self.hexesWidth / 2) + 0.5) * self.hexSize
            self.centerHex = -1

        #e is for flipping the y coordinate
        e = self.hexesWidth
        n = 0
        for hex in operationSpace.starSpaceHexes: 
            #indent every second row
            i = 0 
            if not e % 2 == 0:
                i = self.hexSize // 2
            #y coordinate, #x coordinate is a proportion of the screen
            y = (self.bordersColumnsY) + ((e - 1) * self.hexSize) + self.windowMoveY
            x = (self.bordersRowsX) + (n * self.hexSize) + i - (self.hexSize // 2) + self.windowMoveX
            #draw hex on grid
            gameWindow.blit(self.EMPTY_HEX_IMG, (x, y))

            if hex.empty:
                if shipClicked:
                    if hex in shipHex.neighbors and aShip.shipMovement != 0 and (hex.directions[aShip.orientation] != shipHex.coord['hexNum'] or aShip.shiptype == 'DD' or aShip.shiptype == 'CS'):
                        if not (aShip.shiptype == 'BB' and operationSpace.starSpaceHexes[hex.directions[aShip.orientation]] in shipHex.neighbors):
                            gameWindow.blit(self.MOVE_OPTION_HEX_IMG, (x, y))

            elif hex.entity.spaceEntity == 'shipObject':
                if hex.entity.command == 'ASCS':
                    self.orientationRotation(hex.entity)
                    gameWindow.blit(self.ASCS_SHIP_HEX_IMG, (x, y))
                elif hex.entity.command == 'XNFF':
                    self.orientationRotation(hex.entity)
                    gameWindow.blit(self.XNFF_SHIP_HEX_IMG, (x, y))

                if shipClicked:
                    if hex in targets:
                        gameWindow.blit(self.SHIP_TARGET_HEX_IMG, (x, y))
        
            if shipClicked:
                if hex.coord['hexNum'] == shipHex.coord['hexNum']:
                    gameWindow.blit(self.CLICK_HEX_IMG, (x, y))

            #iterate
            n += 1
            if n == self.hexesLength:
                e -= 1
                n = 0

    #get hexNums from coord mouse
    def getMouseHex(self, mousePos):
        i = 0
        a, b = mousePos
        aActive = False
        bActive = False 
        column, row = 0, 0

        if b in range(self.bordersColumnsY + self.windowMoveY, (self.hexSize * self.hexesWidth) + (self.bordersColumnsY) + self.windowMoveY):
            bActive = True
            #reverse y coords
            row = abs(((b - (self.bordersColumnsY + self.windowMoveY)) // self.hexSize) - self.hexesWidth) - 1
            #check even/odd rows
            if ((b - (self.bordersColumnsY + self.windowMoveY)) // self.hexSize) % 2 == 1:
                i = self.hexSize // 2  

        if a in range((self.bordersRowsX) - i + self.windowMoveX, ((self.hexSize * self.hexesLength) + (self.bordersRowsX) - i) + self.windowMoveX):
            aActive = True
            column = ((a - (self.bordersRowsX + self.windowMoveX)) + i) // self.hexSize

        if aActive and bActive:
            indexCoord = (row * self.hexesLength) + column
            return indexCoord
        else:
            print("No Hexes In this space")
            return -1

    #WIP zoom in
    def zoomInHex(self):
        self.hexSize += 16
        self.scaleHexes(self.hexSize)

    #WIP zoom out
    def zoomOutHex(self):
        self.hexSize -= 16
        self.scaleHexes(self.hexSize)

    #rotate an image based on ship orientation
    def orientationRotation(self, aShip):
        orients = {'R': -90.0, 'L': -270.0, 'UR': -30.0, 'UL': -330.0, 'DR': -150.0, 'DL': -210.0}
        if aShip.command == 'ASCS':
            self.ASCS_SHIP_HEX_IMG = self.rotateCenter(ASCS_SHIP_HEX_IMG, orients[aShip.orientation]) 
        elif aShip.command == 'XNFF':
            self.XNFF_SHIP_HEX_IMG = self.rotateCenter(XNFF_SHIP_HEX_IMG, orients[aShip.orientation])

    #rotate an image with pivot center
    def rotateCenter(self, aImage, anAngle):
        origRect = aImage.get_rect()
        rotImage = pygame.transform.rotate(aImage, anAngle)
        rotRect = origRect.copy()
        rotRect.center = rotImage.get_rect().center
        rotImage = rotImage.subsurface(rotRect).copy()
        return rotImage
        
    #scale the hexes
    def scaleHexes(self, hexSize):
        self.EMPTY_HEX_IMG = pygame.transform.smoothscale(EMPTY_HEX_IMG, (hexSize, hexSize))
        self.ASCS_SHIP_HEX_IMG = pygame.transform.smoothscale(ASCS_SHIP_HEX_IMG, (hexSize, hexSize))
        self.XNFF_SHIP_HEX_IMG = pygame.transform.smoothscale(XNFF_SHIP_HEX_IMG, (hexSize, hexSize))
        self.MOVE_OPTION_HEX_IMG = pygame.transform.smoothscale(MOVE_OPTION_HEX_IMG, (hexSize, hexSize))
        self.SHIP_TARGET_HEX_IMG = pygame.transform.smoothscale(SHIP_TARGET_HEX_IMG, (hexSize, hexSize))
        self.CLICK_HEX_IMG = pygame.transform.smoothscale(CLICK_HEX_IMG, (hexSize, hexSize))
        self.ASCS_SHIP_HEX_IMG.convert()
        self.EMPTY_HEX_IMG.convert()
        self.XNFF_SHIP_HEX_IMG.convert()
        self.MOVE_OPTION_HEX_IMG.convert()
        self.SHIP_TARGET_HEX_IMG.convert()
        self.CLICK_HEX_IMG.convert()