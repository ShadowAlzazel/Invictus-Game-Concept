#class for board display
from gameField.gameAssets import *

class spaceGameBoard:

    def __init__(self, someZoneSpace):
        self.combatZoneSpace = someZoneSpace
        self.hexesLength = someZoneSpace.l
        self.hexesWidth = someZoneSpace.w


    def drawHexes(self, gameWindow):
        displayBoard = self.createDisplayBoard()

        # e is for flipping the y coordinate
        e = self.hexesWidth
        for row in displayBoard:
            i = 0  
            y = ((WIDTH - (64 * self.hexesWidth)) // 2) + ((e - 1) * 64)
            n = 0
            #indent every second row
            if not e % 2 == 0:
                i = 32

            for hex in row:
                #x coordinate is a proportion of the screen
                x = ((LENGTH - (64 * self.hexesLength)) // 2) + (n * 64) + i
                if hex.empty:
                    gameWindow.blit(HEX_Y_IMG, (x, y))
                elif hex.entity.spaceEntity == 'shipObject':
                    gameWindow.blit(HEX_ENTF_IMG, (x, y))
                n += 1

            e -= 1


    def createDisplayBoard(self):
        newRow = []
        displayBoard = []
        for x in self.combatZoneSpace.starSpaceHexes:  
            newRow.append(x)
            if len(newRow) == self.hexesLength:
                displayBoard.append(newRow)
                newRow = []
        return displayBoard


    def getMousePosEnt(self, position):
        displayBoard = self.createDisplayBoard()
        x, y = position
        i = 0
        e = ((y - ((WIDTH - (64 * self.hexesWidth)) // 2)) // 64)   #row
        if not e % 2 == 0:
            i = 32
        n = (x - (LENGTH - ((64 * self.hexesLength) // 2) + i)) // 64   #column
        
        print(displayBoard[e][n].coord['hexNum'])
        return displayBoard[e][n]


