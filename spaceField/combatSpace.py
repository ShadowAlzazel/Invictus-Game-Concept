from spaceField.spaceHexes import *
from spaceField.spaceObjects import *
from random import randint

def createCombatSpace(length, width, density):
    newZone = zoneSpace(length, width)
    area = length * width
    rho = int(((density * 0.01) * area) // 1)
    rhoLib = []

    #get neighbors function
    def getNeighbors(starSpaceHex):
        hexCoord = starSpaceHex.coord['hexNum']
        neighbors = []
        hexMoves = {'Right': 1, 
                    'Left': -1, 
                    'UpRight': (((hexCoord // length) % 2) + length),
                    'UpLeft': ((((hexCoord // length) % 2) + length) - 1),
                    'DownRight': (((hexCoord // length) % 2) - length),
                    'DownLeft': ((((-(hexCoord // length) % 2)) - length) - 1)
                    }

        #check for right hex border
        if not (hexCoord + 1) % length == 0:
            j = newZone.starSpaceHexes[hexCoord + hexMoves['Right']]
            starSpaceHex.directions['R'] = j.coord['hexNum']
            neighbors.append(j)


        #check for left hex borders
        if not hexCoord % length == 0:
            j = newZone.starSpaceHexes[hexCoord + hexMoves['Left']]
            starSpaceHex.directions['L'] = j.coord['hexNum']
            neighbors.append(j)

        #check for up-right hex borders
        if not (hexCoord >= length * (width - 1)) and not ((hexCoord // length) % 2 == 1 and (hexCoord + 1) % length == 0):
            j = newZone.starSpaceHexes[hexCoord + hexMoves['UpRight']]
            starSpaceHex.directions['UR'] = j.coord['hexNum']
            neighbors.append(j)
        
        #check for up-left hex borders
        if not (hexCoord) >= length * (width - 1) and not((hexCoord // length) % 2 == 0 and hexCoord % length == 0):
            j = newZone.starSpaceHexes[hexCoord + hexMoves['UpLeft']]
            starSpaceHex.directions['UL'] = j.coord['hexNum']
            neighbors.append(j)

        #check for down-right hex borders
        if not (hexCoord) // length == 0 and not ((hexCoord // length) % 2 == 1 and (hexCoord + 1) % length == 0):
            j = newZone.starSpaceHexes[hexCoord + hexMoves['DownRight']]
            starSpaceHex.directions['DR'] = j.coord['hexNum']
            neighbors.append(j)

        #check for down-left hex borders
        if not (hexCoord) // length == 0 and not ((hexCoord // length) % 2 == 0 and hexCoord % length == 0):
            j = newZone.starSpaceHexes[hexCoord + hexMoves['DownLeft']]
            starSpaceHex.directions['DL'] = j.coord['hexNum']
            neighbors.append(j)

        return neighbors

    #add random objects
    for x in range(0, rho):
        rhoLib.append(randint(0, area - 1))
        newZone.addCustomEntity(newZone.starSpaceHexes[rhoLib[x]], spaceObject(x))

    #make neighbors for starSpaceHexes
    for z in newZone.starSpaceHexes:
        z.neighbors = getNeighbors(z)

    return newZone