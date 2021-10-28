#Started 10/26/2021
import json
import sys
from random import choice
from shipClasses import *

shipLib = []

with open("warShips.json", "r") as warShipsFile:
    warShips = json.load(warShipsFile)
#>>> warShips[0]
#{'name': 'Hood', 'shipClass': 'HoodClass', 'shipType': 'BB', 'hullnumber': 18, 'shipID': 'BB18'}
#>>> warShips[1]['name']
#'Prince of Wales'

def getClass(strShipClass):
    return getattr(sys.modules[__name__], strShipClass)


#launch Ship using json file
def launchShip(jShip):
    jClass = getClass(jShip["shipClass"])
    newShip = jClass(jShip["hullnumber"], jShip["name"])
    shipLib.append(newShip)


#create multiple ships
def createShips(n = 1):
    c = 0
    while c < n:
        randomShip = choice(warShips)
        u = 0
        if len(shipLib) == 0:
            launchShip(randomShip)
            randomShip = choice(warShips)
            c += 1
        
        for x in shipLib:
            if x.name != randomShip['name'] and u == (len(shipLib) - 1):
                launchShip(randomShip)
                c += 1
            else:
                u += 1 

                
createShips(3)
for x in shipLib:
    x.fullInspect()


"""
thismodule = sys.modules[__name__]
setattr(thismodule, shipID, shipRClass(hullNum, name))
"""