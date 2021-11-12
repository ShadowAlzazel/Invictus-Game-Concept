#class for board display
from gameField.gameAssets import *

class spaceGameBoard:

    def __init__(self, l, w):
        self.hexesLength = l
        self.hexesWidth = w
        self.bordersColumnsY = (WIDTH - (HEX_SIZE * self.hexesWidth)) // 2
        self.bordersRowsX = (LENGTH - (HEX_SIZE * self.hexesLength)) // 2

    #draw hexes on board
    def drawHexes(self, gameWindow, operationSpace):
        gameWindow.fill(SCREEN_RGB)
        # e is for flipping the y coordinate
        e = self.hexesWidth
        n = 0
        for hex in operationSpace.starSpaceHexes: 
            #indent every second row
            i = 0 
            if not e % 2 == 0:
                i = 32
            #y coordinate
            y = (self.bordersColumnsY) + ((e - 1) * HEX_SIZE)
            #x coordinate is a proportion of the screen
            x = (self.bordersRowsX) + (n * HEX_SIZE) + i - (HEX_SIZE // 2)
            if hex.empty:
                gameWindow.blit(EMPTY_HEX_IMG, (x, y))
            elif hex.entity.spaceEntity == 'shipObject':
                if hex.entity.command == 'ASCS':
                    gameWindow.blit(SHIP_HERE_HEX_IMG, (x, y))
                elif hex.entity.command == 'XNFF':
                    gameWindow.blit(SHIP_ENEMY_HERE_HEX_IMG, (x, y))

            n += 1
            if n == self.hexesLength:
                e -= 1
                n = 0

    def drawShipActions(self, gameWindow, operationSpace, shipHex):
        gameWindow.fill(SCREEN_RGB)
        # e is for flipping the y coordinate
        e = self.hexesWidth
        n = 0
        targets = []
        aShip = shipHex.entity
        if aShip.gunsReady():
            targets = aShip.findTargets()

        for hex in operationSpace.starSpaceHexes: 
            #indent every second row
            i = 0 
            if not e % 2 == 0:
                i = 32
            #y coordinate
            y = (self.bordersColumnsY) + ((e - 1) * HEX_SIZE)
            #x coordinate is a proportion of the screen
            x = (self.bordersRowsX) + (n * HEX_SIZE) + i - (HEX_SIZE // 2)
            if hex.empty:
                gameWindow.blit(EMPTY_HEX_IMG, (x, y))
                if hex in shipHex.neighbors and aShip.shipMovement != 0:
                    gameWindow.blit(HEX_MOVABLE, (x, y))
            elif hex.entity.spaceEntity == 'shipObject':
                if hex.entity.command == 'ASCS':
                    gameWindow.blit(SHIP_HERE_HEX_IMG, (x, y))
                elif hex.entity.command == 'XNFF': #aShip.command
                    gameWindow.blit(SHIP_ENEMY_HERE_HEX_IMG, (x, y))

                if hex in targets:
                    gameWindow.blit(HEX_SHIP_TARGET, (x, y))
                        

            n += 1
            if n == self.hexesLength:
                e -= 1
                n = 0


    def getCoordMouse(self, mousePos):
        i = 0
        a, b = mousePos
        aActive = False
        bActive = False 
        column, row = 0, 0

        if b in range(self.bordersColumnsY, (HEX_SIZE * self.hexesWidth) + (self.bordersColumnsY)):
            bActive = True
            #reverse y coords
            row = abs(((b - self.bordersColumnsY) // HEX_SIZE) - self.hexesWidth) - 1

            #check even odd
            if ((b - self.bordersColumnsY) // HEX_SIZE) % 2 == 1:
                i = HEX_SIZE // 2  

        if a in range((self.bordersRowsX) - i, ((HEX_SIZE * self.hexesLength) + (self.bordersRowsX) - i)):
            aActive = True
            column = ((a - self.bordersRowsX) + i) // HEX_SIZE

        if aActive and bActive:
            indexCoord = (row * self.hexesLength) + column
            return indexCoord
        else:
            print("No Hexes In this space")
            return -1