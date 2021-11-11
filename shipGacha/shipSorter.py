#randomizer functions
import json
from random import randint


#"""-------------------------------------RANDOM-CLASS--------------------------------------"""
with open("shipGacha\currentShipClasses.json", "r") as currentShipClassesFile:
    currentShipClasses = json.load(currentShipClassesFile)

currentTypes = ['BB', 'BC', 'CS', 'CA', 'CL', 'DD']  #current available ship types

#Get random ship Class from json file
def randShipClass():
    x = currentTypes[randint(0, len(currentTypes) - 1)]
    q = randint(0, len(currentShipClasses[0][x]) - 1)

    rClass = currentShipClasses[0][x][q]
    return rClass


#"""-------------------------------------RANDOM-NAME--------------------------------------"""
nameOrigins = ['IJN', 'KMS', 'HMS', 'FFNF', 'USS']   #name from a historical origin
nameTypes = ['CVA', 'BB', 'BC', 'CS', 'CA', 'CVL', 'CL', 'DD']   #name from ship type

with open("shipGacha\sortedShipNames.json", "r") as sortedShipNamesFile:
    sortedShipNames = json.load(sortedShipNamesFile)

#Get random name from json file
def randName():
    x = nameOrigins[randint(0, len(nameOrigins) - 1)]
    y = nameTypes[randint(0, len(nameTypes) - 1)]
    q = randint(0, len(sortedShipNames[0][x][y]) - 1)

    rName = sortedShipNames[0][x][y][q]
    return rName


#"""-------------------------------------RANDOM-STATS--------------------------------------"""
#Randomize stats slightly
def randStats(aShip):
    aShip.shipStats['FP'] += (randint(-20, 20))
    aShip.shipStats['ACC'] += (randint(-5, 5))
    aShip.shipStats['EVA'] += (randint(-5, 5))
    aShip.shipStats['SPD'] += (randint(-1, 1))
    aShip.shipStats['LCK'] += (randint(-2, 2))

