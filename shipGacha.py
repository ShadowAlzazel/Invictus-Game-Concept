import json
import sys
from random import randint
from shipClasses import *

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


#Get random name from json file
def ranShipName(r3 = True, v3 = 0):
    if r3 == True:
        x = randint(0, len(randomShipNames) - 1)
    else:
        x = v3
    y = randint(0, len(randomShipNames[x]['names']) - 1)

    rName = randomShipNames[x]['names'][y]
    return rName

#Get random Class from json file
def ranShipClass(r2 = True, v2 = 0):
    if r2 == True:
        x = randint(0, len(currentShipClasses) - 1)
    else: 
        x = v2
    y = randint(0, len(currentShipClasses[x]['currentClasses']) - 1)

    rClass = currentShipClasses[x]['currentClasses'][y]
    return rClass

#create a ship with random stats
def createGachaShip(nLib, r1 = True, v1 = 0):
    h = randint(1, 10000)
    l = len(nLib)

    gachaClass = getClass(ranShipClass(r1, v1))
    gachaShip = gachaClass(h, ranShipName())
    nLib.append(gachaShip)

    nLib[l].shipStats['FP'] += (randint(-10, 15))
    nLib[l].shipStats['ACC'] += (randint(-2, 3))
    nLib[l].shipStats['EVA'] += (randint(-2, 3))
    nLib[l].shipStats['SPD'] += (randint(-2, 2))
    nLib[l].shipStats['luck'] += (randint(-1, 1))


#print(ranShipName())
#print(ranShipClass())
#createGachaShip()
#print(shipLib2[0].shipStats)