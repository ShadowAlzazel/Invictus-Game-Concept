#class for board display
from gameField.gameHex import spaceGameHex
from gameField.gameAssets import *

class spaceGameBoard:

    def __init__(self, someZone):
        self.gameCombatZone = someZone
        self.displayBoard = []
        newRow = []
        for x in someZone.starSpaceHexes:  
            z =  spaceGameHex(x)
            newRow.append(z)
            if len(newRow) == self.gameCombatZone.l:
                self.displayBoard.append(newRow)
                newRow = []
    

    def drawHexes(self, gameWindow):

        e = 0
        for row in self.displayBoard:
            for hexes in row:
                gameWindow.blit(HEX_Y_IMG)
            e += 1
