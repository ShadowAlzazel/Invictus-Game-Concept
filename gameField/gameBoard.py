#class for board display
from gameField.gameHex import spaceGameHex
from gameField.gameAssets import *

class spaceGameBoard:

    def __init__(self, someZone):
        self.gameCombatZone = someZone
        self.hexesLength = someZone.l
        self.hexesWidth = someZone.w
        self.displayBoard = []
        newRow = []
        for x in someZone.starSpaceHexes:  
            z = spaceGameHex(x)
            newRow.append(z)
            if len(newRow) == self.hexesLength:
                self.displayBoard.append(newRow)
                newRow = []
    

    def drawHexes(self, gameWindow):

        e = 0
        for row in self.displayBoard:
            i = 0
            y = ((WIDTH - (64 * self.hexesWidth)) // 2) + (e * 64)
            n = 0
            if not e % 2 == 0:
                i = 32

            for hex in row:
                x = ((LENGTH - (64 * self.hexesLength)) // 2) + (n * 64) + i
                if hex.gameHexSpace.empty:
                    gameWindow.blit(HEX_Y_IMG, (x, y))
                elif hex.gameHexSpace.entity.spaceEntity == 'shipObject':
                    gameWindow.blit(HEX_ENTF_IMG, (x, y))
                n += 1

            e += 1
