from starSpaces.spaceHexes import *
from starSpaces.spaceObjects import *
from random import randint

def create_map_hexes(length, width, density):
    newZone = zoneSpace(length, width)
    area = length * width
    rho = int(((density * 0.01) * area) // 1)
    rhoLib = []

    #get neighbors function
    def getNeighbors(starSpaceHex):
        hex_coordinate_index = starSpaceHex.hex_coordinate_index
        neighbors = []
        hex_moves = {'Right': 1, 
                    'Left': -1, 
                    'UpRight': (((hex_coordinate_index // length) % 2) + length),
                    'UpLeft': ((((hex_coordinate_index // length) % 2) + length) - 1),
                    'DownRight': (((hex_coordinate_index // length) % 2) - length),
                    'DownLeft': ((((-(hex_coordinate_index // length) % 2)) - length) - 1)
                    }

        #check for right hex border
        if not (hex_coordinate_index + 1) % length == 0:
            j = newZone.starHexes[hex_coordinate_index + hex_moves['Right']]
            starSpaceHex.directions['R'] = j.hex_coordinate_index
            neighbors.append(j)

        #check for left hex borders
        if not hex_coordinate_index % length == 0:
            j = newZone.starHexes[hex_coordinate_index + hex_moves['Left']]
            starSpaceHex.directions['L'] = j.hex_coordinate_index
            neighbors.append(j)

        #check for up-right hex borders
        if not (hex_coordinate_index >= length * (width - 1)) and not ((hex_coordinate_index // length) % 2 == 1 and (hex_coordinate_index + 1) % length == 0):
            j = newZone.starHexes[hex_coordinate_index + hex_moves['UpRight']]
            starSpaceHex.directions['UR'] = j.hex_coordinate_index
            neighbors.append(j)
        
        #check for up-left hex borders
        if not (hex_coordinate_index) >= length * (width - 1) and not ((hex_coordinate_index // length) % 2 == 0 and hex_coordinate_index % length == 0):
            j = newZone.starHexes[hex_coordinate_index + hex_moves['UpLeft']]
            starSpaceHex.directions['UL'] = j.hex_coordinate_index
            neighbors.append(j)

        #check for down-right hex borders
        if not (hex_coordinate_index) // length == 0 and not ((hex_coordinate_index // length) % 2 == 1 and (hex_coordinate_index + 1) % length == 0):
            j = newZone.starHexes[hex_coordinate_index + hex_moves['DownRight']]
            starSpaceHex.directions['DR'] = j.hex_coordinate_index
            neighbors.append(j)

        #check for down-left hex borders
        if not (hex_coordinate_index) // length == 0 and not ((hex_coordinate_index // length) % 2 == 0 and hex_coordinate_index % length == 0):
            j = newZone.starHexes[hex_coordinate_index + hex_moves['DownLeft']]
            starSpaceHex.directions['DL'] = j.hex_coordinate_index
            neighbors.append(j)

        return neighbors

    #add random objects
    for x in range(0, rho):
        rhoLib.append(randint(0, area - 1))
        newZone.addCustomEntity(newZone.starHexes[rhoLib[x]], spaceObject(x))

    #make neighbors for starHexes
    for z in newZone.starHexes:
        z.neighbors = getNeighbors(z)

    return newZone