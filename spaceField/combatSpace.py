from . spaceHexes import *
from . spaceObjects import *
from random import randint

def createCombatSpace(length, width, density):
    newZone = zoneSpace(length, width)
    area = length * width
    rho = int(((density * 0.01) * area) // 1)
    rhoLib = []

    for x in range(0, rho):
        rhoLib.append(randint(0, area - 1))
        newZone.addCustomEntity(newZone.starSpaceHexes[rhoLib[x]], spaceObject(x))

    return newZone
