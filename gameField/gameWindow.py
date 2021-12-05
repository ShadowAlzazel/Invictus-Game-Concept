#class for game display
from gameField.gameAssets import *
from multiprocessing.dummy import Pool as ThreadPool
#from multiprocessing import Pool 

#----------------------------------------------------------------------

class spaceWindow:

    def __init__(self, opsSpace, gameWindow, hexSize):
        self.hexesLength = opsSpace.l
        self.hexesWidth = opsSpace.w
        self.opsSpace = opsSpace
        self.hexSize = hexSize
        self.gameScreen = gameWindow
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
    def drawHexes(self, currentFleetCom, shipHex=[]):
        self.selectedHex = shipHex
        self.currentFleetCom = currentFleetCom
        self.gameScreen.blit(FIT_SPACE, (0, 0))

        if self.centerHex > -1:
            c = 0
            if (self.centerHex // self.hexesLength) % 2 != 0:
                c = self.hexSize / 2
            self.windowMoveX = int((self.hexesLength / 2) - ((self.centerHex % self.hexesLength) + 1)) * self.hexSize + c
            self.windowMoveY = int(((self.centerHex // self.hexesLength)) - (self.hexesWidth / 2) + 0.5) * self.hexSize
            self.centerHex = -1
            
        #check of shipClicked
        self.shipClicked = False
        if shipHex and not shipHex.empty:
            self.targetedHexes = []
            aShip = shipHex.entity
            if aShip.guns_primed():
                self.targetedHexes = aShip.track_targets()
            self.shipClicked = True

        dPool = ThreadPool(2)
        dPool.map(self._drawHex, self.opsSpace.starHexes)
        dPool.close()


    def _drawHex(self, aHex):
        coord = aHex.hexCoord
        rowHeight = self.hexesWidth - (coord // self.hexesLength) - 1
        indent = 0
        if rowHeight % 2 == self.hexesWidth % 2:
            indent = self.hexSize // 2

        y = (self.bordersColumnsY) + (rowHeight * self.hexSize) + self.windowMoveY
        x = (self.bordersRowsX) + ((coord % self.hexesLength) * self.hexSize) + indent - (self.hexSize // 2) + self.windowMoveX
        if x < LENGTH + self.hexSize and y < WIDTH + self.hexSize and x > -self.hexSize and y > -self.hexSize:
            self.gameScreen.blit(self.animatedHexes['gridHex'], (x, y))
            #check if empty for move
            if aHex.empty:
                if self.shipClicked:
                    aShip = self.selectedHex.entity
                    if aHex in self.selectedHex.neighbors and aShip.shipMovement != 0 and (aHex.directions[aShip.orientation] != self.selectedHex.hexCoord or aShip.ship_type == 'DD' or aShip.ship_type == 'CS'):
                        if not (aShip.ship_type == 'BB' and self.opsSpace.starHexes[aHex.directions[aShip.orientation]] in self.selectedHex.neighbors):
                            self.gameScreen.blit(self.animatedHexes['moveHex'], (x, y))

            #check if ship
            elif aHex.entity.entity_type == 'ship_entity':
                if self.currentFleetCom[0:3] != aHex.entity.command[0:3] and aHex.entity.detected:
                    self.gameScreen.blit(self.animatedHexes['enemyHex'], (x, y))
                elif self.currentFleetCom[0:3] == aHex.entity.command[0:3]:
                    self.gameScreen.blit(self.animatedHexes['allyHex'], (x, y))

                if aHex.entity.command == 'ASCS' and aHex.entity.detected:
                    self.orientationRotation(aHex.entity)
                    self.gameScreen.blit(self.ROT_ASCS_SHIP_HEX_IMG, (x, y))
                elif aHex.entity.command == 'XNFFS' and aHex.entity.detected:
                    self.orientationRotation(aHex.entity)
                    self.gameScreen.blit(self.ROT_XNFF_SHIP_HEX_IMG, (x, y))

                #check if target in range
                if self.shipClicked:
                    if aHex in self.targetedHexes:
                        self.gameScreen.blit(self.animatedHexes['targetHex'], (x, y))
        
                #clicked
                if self.shipClicked:
                    if aHex.hexCoord == self.selectedHex.hexCoord:
                        self.gameScreen.blit(self.animatedHexes['clickHex'], (x, y))
        

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
