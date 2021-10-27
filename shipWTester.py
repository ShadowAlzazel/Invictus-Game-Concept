#Started 10/26/2021
import json
import sys
from random import randint, choices
from shipCombatNew import combatGame
from shipClasses import *

with open("warShips.json", "r") as warShipsFile:
    warShips = json.load(warShipsFile)

def getClass(strShipClass):
    return getattr(sys.modules[__name__], strShipClass)


def createShips(n = 1):
    global shipLib
    c = 0
    z = []

    while c < n:
        if len(shipLib) == len(warShips):
            print("Library Full!")
            return

        r = randint(0, len(warShips) - 1)
        for x in shipLib:
            if x.name == warShips[r]["name"]:
                z.append(r)

        if r not in z:     
            shipRClass = getClass(warShips[r]["shipClass"]) 
            hullNum = warShips[r]["hullnumber"]
            name = warShips[r]["name"]
            newShip = shipRClass(hullNum, name)
            shipLib.append(newShip)
            c += 1


def ranBattler():
    rList = choices(shipLib, k=2)
    combatGame(rList[0], rList[1])

shipLib = []

createShips(3)
for x in shipLib:
    x.inspect()

ranBattler()


"""
thismodule = sys.modules[__name__]
setattr(thismodule, shipID, shipRClass(hullNum, name))
"""


