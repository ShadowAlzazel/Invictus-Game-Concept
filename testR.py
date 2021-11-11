import createTestShips
from spaceField import *

gameShipLib = []
def createShips(someShipLib, n):
    while n > 0:
        createTestShips.gachaRandShip(someShipLib)
        n -= 1

createShips(gameShipLib, 3)
gameShipLib[0].fullInspect()

aoe = createCombatSpace(5, 5, 0)
aoe.addCustomEntity(aoe.starSpaceHexes[12], gameShipLib[0])
#print(gameShipLib[0].placeSpace.neighbors)



def findHexes(radarClass, aHexSpace):
    assert radarClass != 0
    originHex = aHexSpace
    hexesNearby = []
    originRing = [aHexSpace]

    def hexRange(radarClass, someHexRing, n = 0):
        """
        for x in someHexSpace.neighbors:
            if n != rdr:
                hexRange(rdr, x, n + 1)
            elif x not in hexesNearby and x != originHex:
                hexesNearby.append(x)
        """
        thisHexRing = someHexRing
        newHexRing  = []
        for z in thisHexRing:
            for y in z.neighbors:
                if y not in newHexRing and y != originHex and y not in someHexRing:
                    newHexRing.append(y)


        if n != radarClass:
            hexRange(radarClass, newHexRing, n + 1)

        for k in newHexRing:
            if k not in hexesNearby:
                hexesNearby.append(k)

        return hexesNearby

    return hexRange(radarClass, originRing)


xList = findHexes(2, gameShipLib[0].placeSpace) 

ods = []
for z in xList:
    ods.append(z.coord['hexNum']) 
print(ods)
print(len(ods))


"""
aoe = createCombatSpace(5, 5, 0)
q = 0
n2List = []
for x in aoe.starSpaceHexes[q].neighbors:
    for y in aoe.starSpaceHexes[x.coord['hexNum']].neighbors:
        if y not in n2List and y != aoe.starSpaceHexes[q]:
            #print(y.coord['hexNum'])
            n2List.append(y)

o = []
for a in n2List:
    o.append(a.coord['hexNum'])
print(o)
"""

"""
rangeList = []
for a in gameShipLib[0].placeSpace.neighbors:
    for b in a.neighbors:
        for c in b.neighbors:
            for d in c.neighbors:
                for e in d.neighbors:
                    if e not in rangeList and e != gameShipLib[0].placeSpace:
                        rangeList.append(e)

oList = []
for u in rangeList:
    oList.append(u.coord['hexNum'])
print(oList)
"""