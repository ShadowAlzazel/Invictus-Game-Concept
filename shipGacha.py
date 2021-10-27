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


#Get random name from json file
def ranShipName(r = True, n = 0):
    if r == True:
        x = randint(0, len(randomShipNames) - 1)
    else:
        x = n
    y = randint(0, len(randomShipNames[x]['names']) - 1)

    rName = randomShipNames[x]['names'][y]
    return rName

#Get random Class from json file
def ranShipClass():
    x = randint(0, len(currentShipClasses) - 1)
    y = randint(0, len(currentShipClasses[x]['currentClasses']) - 1)

    rClass = currentShipClasses[x]['currentClasses'][y]
    return rClass

#create a ship with random stats
def createGachaShip():
    h = randint(1, 10000)
    l = len(shipLib2)

    gachaClass = getClass(ranShipClass())
    gachaShip = gachaClass(h, ranShipName())
    shipLib2.append(gachaShip)

    shipLib2[l].shipStats['FP'] += (randint(-10, 15))
    shipLib2[l].shipStats['ACC'] += (randint(-2, 3))
    shipLib2[l].shipStats['EVA'] += (randint(-3, 4))
    shipLib2[l].shipStats['SPD'] += (randint(-2, 2))


#print(ranShipName())
#print(ranShipClass())
createGachaShip()
print(shipLib2[0].shipStats)