#class for board display
#import pygame
from gameField.gameAssets import *
from multiprocessing.dummy import Pool as ThreadPool
#from multiprocessing import Pool 
from itertools import repeat

#----------------------------------------------------------------------

class spaceWindow:

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
        self.ROT_ASCS_SHIP_HEX_IMG = ASCS_SHIP_HEX_IMG
        self.XNFF_SHIP_HEX_IMG = XNFF_SHIP_HEX_IMG
        self.ROT_XNFF_SHIP_HEX_IMG = XNFF_SHIP_HEX_IMG
        #selections
        self.selectedHexNum = -1
        self.selectedHex = []
        self.shipClicked = False 
        self.targetedHexes = []
        self.currentFleetCom = 'NNNN'

        #animations
        self.baseHex = GRID_HEX_ANI_BASE
        self.baseHex.convert()
        self.templateHexes = {'aniHexB': GRID_HEX_ANI_EMPTY, 'aniHexEnemy': GRID_HEX_ANI_ENEMY, 'aniHexClick': GRID_HEX_ANI_CLICK, 
                            'aniHexMove': GRID_HEX_ANI_MOVE, 'aniHexTarget': GRID_HEX_ANI_TARGET, 'aniHexAlly': GRID_HEX_ANI_ALLY}
        for val in self.templateHexes.values():
            val.convert()
        self.animatedHexes = {'gridHex': self.templateHexes['aniHexB'], 'enemyHex': self.templateHexes['aniHexEnemy'], 
                            'clickHex': self.templateHexes['aniHexClick'], 'moveHex': self.templateHexes['aniHexMove'], 
                            'targetHex': self.templateHexes['aniHexTarget'], 'allyHex': self.templateHexes['aniHexAlly']}
        self.counterA = 0
        self.counterC = 0
        #scale
        self.scaleHexes(self.hexSize)

    #draw hexes on board
    def drawHexes(self, gameWindow, operationSpace, currentFleet, shipHex=[]):
        gameWindow.blit(FIT_SPACE, (0, 0))

        if self.centerHex > -1:
            c = 0
            if (self.centerHex // self.hexesLength) % 2 != 0:
                c = self.hexSize / 2
            self.windowMoveX = int((self.hexesLength / 2) - ((self.centerHex % self.hexesLength) + 1)) * self.hexSize + c
            self.windowMoveY = int(((self.centerHex // self.hexesLength)) - (self.hexesWidth / 2) + 0.5) * self.hexSize
            self.centerHex = -1
        """
        self.targetedHexes,  self.shipClicked = [], False
        if self.selectedHexNum > -1:
            self.selectedHex = operationSpace.starHexes[self.selectedHexNum]
            if not self.selectedHex.empty: 
                aShip = self.selectedHex.entity
                self.shipClicked = True
                if aShip.gunsReady():
                    self.targetedHexes = aShip.trackTargets()
                

        self.opsSpace = operationSpace

        dPool = ThreadPool(2)
        hexResults = dPool.map(self._drawAHex, operationSpace.starHexes)
        filteredResults = list(filter(None, hexResults))
        hexImgs, positions = [], []
        for u in filteredResults:
            hexImgs.append(u[0])
            positions.append(u[1])
        print(hexImgs[0], positions[0])


        dPool.map(gameWindow.blit, hexImgs, positions)
        #s = 1
        #s[1][1]

        dPool.close()
        dPool.join()

        """
        #check of shipClicked
        shipClicked = False
        if shipHex and not shipHex.empty:
            targets = []
            aShip = shipHex.entity
            if aShip.gunsReady():
                targets = aShip.trackTargets()
            shipClicked = True

        
        #e is for flipping the y coordinate
        e = self.hexesWidth
        n = 0
        for hex in operationSpace.starHexes: 
            #indent every second row
            i = 0 
            if not e % 2 == self.hexesWidth % 2:
                i = self.hexSize // 2
            #y coordinate, #x coordinate is a proportion of the screen
            y = (self.bordersColumnsY) + ((e - 1) * self.hexSize) + self.windowMoveY
            x = (self.bordersRowsX) + (n * self.hexSize) + i - (self.hexSize // 2) + self.windowMoveX
            #draw hex on grid
            if x < LENGTH + self.hexSize and y < WIDTH + self.hexSize and x > -self.hexSize and y > -self.hexSize:
                gameWindow.blit(self.animatedHexes['gridHex'], (x, y))

                #check if empty for move
                if hex.empty:
                    if shipClicked:
                        if hex in shipHex.neighbors and aShip.shipMovement != 0 and (hex.directions[aShip.orientation] != shipHex.hexCoord or aShip.shiptype == 'DD' or aShip.shiptype == 'CS'):
                            if not (aShip.shiptype == 'BB' and operationSpace.starHexes[hex.directions[aShip.orientation]] in shipHex.neighbors):
                                gameWindow.blit(self.animatedHexes['moveHex'], (x, y))

                #check if ship
                elif hex.entity.spaceEntity == 'shipObject':
                    if currentFleet[0:3] != hex.entity.command[0:3] and hex.entity.detected:
                        gameWindow.blit(self.animatedHexes['enemyHex'], (x, y))
                    elif currentFleet[0:3] == hex.entity.command[0:3]:
                        gameWindow.blit(self.animatedHexes['allyHex'], (x, y))

                    if hex.entity.command == 'ASCS' and hex.entity.detected:
                        self.orientationRotation(hex.entity)
                        gameWindow.blit(self.ROT_ASCS_SHIP_HEX_IMG, (x, y))
                    elif hex.entity.command == 'XNFFS' and hex.entity.detected:
                        self.orientationRotation(hex.entity)
                        gameWindow.blit(self.ROT_XNFF_SHIP_HEX_IMG, (x, y))

                    #check if target in range
                    if shipClicked:
                        if hex in targets:
                            gameWindow.blit(self.animatedHexes['targetHex'], (x, y))
            
                #clicked
                if shipClicked:
                    if hex.hexCoord == shipHex.hexCoord:
                        gameWindow.blit(self.animatedHexes['clickHex'], (x, y))

            #iterate
            n += 1
            if n == self.hexesLength:
                e -= 1
                n = 0
        
        #self.opsSpace = []

    """
    def drawAHex(self, windowHex):
        coord = windowHex[1].hexCoord
        rowHeight = self.hexesWidth - (coord // self.hexesLength) 
        indent = 0
        if not rowHeight % 2 == self.hexesWidth % 2:
            indent = self.hexSize // 2

        y = (self.bordersColumnsY) + (rowHeight * self.hexSize) + self.windowMoveY
        x = (self.bordersRowsX) + ((coord % self.hexesLength) * self.hexSize) + indent - (self.hexSize // 2) + self.windowMoveX
        if x < LENGTH + self.hexSize and y < WIDTH + self.hexSize and x > -self.hexSize and y > -self.hexSize:
            windowHex[0].blit(self.animatedHexes['gridHex'], (x, y))
        #print((x, y))
    """
    #WIP
    def _getHexImg(self, aHex, hexImg):
        
        if aHex.empty: 
            if self.shipClicked:
                aShip = self.selectedHex.entity
                if aHex in self.selectedHex.neighbors and aShip.shipMovement != 0 and (aHex.directions[aShip.orientation] != self.selectedHex.hexCoord or aShip.shiptype == 'DD' or aShip.shiptype == 'CS'):
                    if not (aShip.shiptype == 'BB' and self.opsSpace.starHexes[hex.directions[aShip.orientation]] in self.selectedHex.neighbors):
                        hexImg.blit(self.animatedHexes['moveHex'], (0,0))

                #check if ship
        elif aHex.entity.spaceEntity == 'shipObject':
            if self.currentFleetCom[0:3] != aHex.entity.command[0:3] and aHex.entity.detected:
                hexImg.blit(self.animatedHexes['enemyHex'], (0,0))
            elif self.currentFleetCom[0:3] == aHex.entity.command[0:3]:
                hexImg.blit(self.animatedHexes['allyHex'], (0,0))

            if aHex.entity.command[0:3] == 'ASC' and aHex.entity.detected:
                self.orientationRotation(aHex.entity)
                hexImg.blit(self.ROT_ASCS_SHIP_HEX_IMG, (0,0))
            elif aHex.entity.command[0:3] == 'XNF' and aHex.entity.detected:
                self.orientationRotation(aHex.entity)
                hexImg.blit(self.ROT_XNFF_SHIP_HEX_IMG, (0,0))
                
            #check if target in range
            if self.shipClicked:
                if aHex in self.targetedHexes:
                    hexImg.blit(self.animatedHexes['targetHex'], (0,0))
    
        #clicked
        if self.shipClicked:
            if aHex.hexCoord == self.selectedHex.hexCoord:
                hexImg.blit(self.animatedHexes['clickHex'], (0,0))
        
        
        return

    #WIP
    def _drawAHex(self, aHex):
        coord = aHex.hexCoord
        rowHeight = self.hexesWidth - (coord // self.hexesLength) - 1
        indent = 0
        if rowHeight % 2 == self.hexesWidth % 2:
            indent = self.hexSize // 2

        y = (self.bordersColumnsY) + (rowHeight * self.hexSize) + self.windowMoveY
        x = (self.bordersRowsX) + ((coord % self.hexesLength) * self.hexSize) + indent - (self.hexSize // 2) + self.windowMoveX
        if x < LENGTH + self.hexSize and y < WIDTH + self.hexSize and x > -self.hexSize and y > -self.hexSize:
            hexImg = self.animatedHexes['gridHex']
            self._getHexImg(aHex, hexImg)
            #hexImg = self.animatedHexes['gridHex']
            return [hexImg, (x, y)]


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
            if ((b - (self.bordersColumnsY + self.windowMoveY)) // self.hexSize) % 2 == (self.hexesWidth + 1) % 2:
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
        self.scaleHexes(self.hexSize)
        if aShip.command == 'ASCS':
            self.ROT_ASCS_SHIP_HEX_IMG = self.rotateCenter(self.ASCS_SHIP_HEX_IMG, orients[aShip.orientation]) 
        elif aShip.command == 'XNFFS':
            self.ROT_XNFF_SHIP_HEX_IMG = self.rotateCenter(self.XNFF_SHIP_HEX_IMG, orients[aShip.orientation])

    #rotate an image with pivot center
    def rotateCenter(self, aImage, anAngle):
        origRect = aImage.get_rect()
        rotImage = pygame.transform.rotate(aImage, anAngle)
        rotRect = origRect.copy()
        rotRect.center = rotImage.get_rect().center
        rotImage = rotImage.subsurface(rotRect).copy()
        return rotImage

    def aniHexes(self):
        x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 10, 9 ,8, 7, 6, 5, 4, 3, 2, 1, 0]
        w = self.counterA 
        
        for temps, ani in zip(self.templateHexes.values(), self.animatedHexes.keys()):
            baseImg = self.baseHex.copy()
            newAniImg = temps.copy()
            baseImg.blit(newAniImg, (0, x[w]))
            aniImg = pygame.transform.scale(baseImg, (self.hexSize, self.hexSize))
            self.animatedHexes[ani] = aniImg
        
        if self.counterA == 23:
            self.counterA = 0
        else:
            self.counterA += 1
       
    #scale the hexes
    def scaleHexes(self, hexSize):
        self.ASCS_SHIP_HEX_IMG.convert()
        self.EMPTY_HEX_IMG.convert()
        self.XNFF_SHIP_HEX_IMG.convert()
        self.EMPTY_HEX_IMG = pygame.transform.smoothscale(EMPTY_HEX_IMG, (hexSize, hexSize))
        self.ASCS_SHIP_HEX_IMG = pygame.transform.smoothscale(ASCS_SHIP_HEX_IMG, (hexSize, hexSize))
        self.XNFF_SHIP_HEX_IMG = pygame.transform.smoothscale(XNFF_SHIP_HEX_IMG, (hexSize, hexSize))
