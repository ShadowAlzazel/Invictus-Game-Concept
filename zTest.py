from shipGacha import *
from shipTimedCombat import ACombatGame
import time 

gameShipLib = []

createGachaShip(gameShipLib, False, 0)
createGachaShip(gameShipLib, False, 0)


#gameShipLib[0].fullInspect()
g1 = ACombatGame(30, gameShipLib[0], gameShipLib[1])
print(g1.combatLib)
g1.timedCombatGame()