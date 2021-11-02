from shipGacha import *
from shipCombat import ACombatGame

gameShipLib = []

gachaShip(gameShipLib)
gachaShip(gameShipLib)


#gameShipLib[0].fullInspect()
g1 = ACombatGame(30, gameShipLib[0], gameShipLib[1])
print(g1.combatLib)
g1.testCombatGame()
#g1.timedCombatGame()

