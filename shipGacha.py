import json
import sys
from random import randint
from shipClasses import *

with open("sortedShipNames.json", "r") as sortedShipNamesFile:
    sortedShipNames = json.load(sortedShipNamesFile)

with open("currentShipClasses.json", "r") as currentShipClassesFile:
    currentShipClasses = json.load(currentShipClassesFile)

aSubCat = ['IJN', 'KMS', 'HMS', 'FFNF']
aTypes = ['BB','BC','CS','CA','DD']


def getClass(strShipClass):
    return getattr(sys.modules[__name__], strShipClass)


#Get random name from json file
def ranShipName():
    x = aSubCat[randint(0, len(aSubCat) - 1)]
    y = aTypes[randint(0, len(aTypes) - 1)]
    q = randint(0, len(sortedShipNames[0][x][y]) - 1)

    rName = sortedShipNames[0][x][y][q]
    return rName


#Get random Class from json file
def ranShipClass():
    x = aTypes[randint(0, len(aTypes) - 1)]
    q = randint(0, len(currentShipClasses[0][x]) - 1)

    rClass = currentShipClasses[0][x][q]
    return rClass


#random stats
def ranShipStats(aShip):
    aShip.shipStats['FP'] += (randint(-5, 5))
    aShip.shipStats['ACC'] += (randint(-2, 2))
    aShip.shipStats['EVA'] += (randint(-2, 2))
    aShip.shipStats['SPD'] += (randint(-2, 2))
    aShip.shipStats['luck'] += (randint(-1, 1))


#create a ship with random stats
def gachaShip(givenLib):
    rPenantNum = randint(1, 10000)
    l = len(givenLib)

    gachaClass = getClass(ranShipClass())
    aGachaShip = gachaClass(rPenantNum, ranShipName())
    givenLib.append(aGachaShip)
    ranShipStats(givenLib[l])


#Create a specific ship
def buildShip(givenLib, f ,g, rS = False):
    assert f in aSubCat
    assert g in aTypes 
    rHullnum = randint(1, 10000)
    h = randint(0, len(sortedShipNames[0][f][g]) - 1)
    l = len(givenLib)

    gachaClass = getClass(ranShipClass())
    buildShip = gachaClass(rHullnum, sortedShipNames[0][f][g][h])
    givenLib.append(buildShip)
    if rS == True:
        ranShipStats(givenLib[l])


def gachaOrder(aLib):
    x = input("Enter 'Gacha' for a Random Pull, Else enter 'Build':")
    if x == 'Gacha' or x == 'gacha':
        gachaShip(aLib)
    elif x == 'Build' or x == 'build':
        u = input("Enter an available Faction from:", aSubCat)
        v = input("Enter an availabe ship type from:", aTypes)
        r = input("Allow for random stats? Enter T or F:")   
        if r == 'True' or r == 'T':
            r = True
        else: 
            r = False  
        buildShip(aLib, u, v, r)
    else:
        print("Order failed. Try again.")
    
    aLib[-1].fullInspect()


ShipLib2 = []

buildShip(ShipLib2, 'IJN', 'CA')
#gachaOrder(ShipLib2)
#gachaShip(ShipLib2)
#ShipLib2[-1].fullInspect()
