#class for board display
from gameField.gameAssets import *

class spaceGameBoard:

    def __init__(self, someZone):
        self.gameCombatZone = someZone
        self.hexesLength = someZone.l
        self.hexesWidth = someZone.w
        self.displayBoard = []
        newRow = []
        for x in someZone.starSpaceHexes:  
            newRow.append(x)
            if len(newRow) == self.hexesLength:
                self.displayBoard.append(newRow)
                newRow = []
    

    def drawHexes(self, gameWindow):

        # e is for flipping the y coordinate
        e = self.hexesWidth
        for row in self.displayBoard:
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
