import json
import sys
from random import randint
from shipClasses import *

shipLib2 = []

with open("randomShipNames.json", "r") as randomShipNamesFile:
    randomShipNames = json.load(randomShipNamesFile)

#>>> randomShipNames[0]
#{'type': 'IJN', 'names': ['Yamakaze', 'Shimikaze', 'Yukikaze', 'Kamikaze']}
#>>> randomShipNames[0]['names']
#['Yamakaze', 'Shimikaze', 'Yukikaze', 'Kamikaze']

#>>> randomShipNames[2]['type']
#'HMS'
#>>> randomShipNames[2]['names'][11]
#'Nelson'

with open("currentShipClasses.json", "r") as currentShipClassesFile:
    currentShipClasses = json.load(currentShipClassesFile)

def getClass(strShipClass):
    return getattr(sys.modules[__name__], strShipClass)

def ranShipName():
    x = randint(0, len(randomShipNames) - 1)
    y = randint(0, len(randomShipNames[x]['names']) - 1)

    rName = randomShipNames[x]['names'][y]
    return rName


def ranShipClass():
    x = randint(0, len(currentShipClasses) - 1)
    y = randint(0, len(currentShipClasses[x]['currentClasses']) - 1)

    rClass = currentShipClasses[x]['currentClasses'][y]
    return rClass


def createGachaShip():
    n = randint(1, 10000)
    gachaClass = getClass(ranShipClass())
    gachaShip = gachaClass(n, ranShipName())
    shipLib2.append(gachaShip)

#print(ranShipName())
#print(ranShipClass())
createGachaShip()