import testShip
from spaceField import *
from shipCombat import ACombatGame

gameShipLib = []
def createShips(someShipLib, n):
    while n > 0:
        testShip.gachaRandShip(someShipLib)
        n -= 1

createShips(gameShipLib, 3)
gameShipLib[0].fullInspect()

aoe = createCombatSpace(10, 10, 10)
print(aoe.spaceHexesFull)

aGame = ACombatGame(30, gameShipLib[0], gameShipLib[1])
aGame.testCombatGame()
#aGame.timedCombatGame()

#aoe.addCustomEntity(aoe.starSpaceHexes[5], gameShipLib[0])
#aoe.addCustomEntity(aoe.starSpaceHexes[6], gameShipLib[1])
#print(aoe.spaceEntities['spaceObject'][0].name, "At Hex", aoe.spaceEntities['spaceObject'][0].placeSpace.coord['hexNum'])
#print(aoe.spaceEntities['spaceObject'][1].name, "At Hex", aoe.spaceEntities['spaceObject'][1].placeSpace.coord['hexNum'])
#aoe.moveEntity(gameShipLib[0], 'UL')