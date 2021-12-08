#get class from available class
import sys
from shipClasses import *
from shipGacha.shipSorter import randName, randShipClass, randStats 
from random import randint

def getClass(strShipClass):
    return getattr(sys.modules[__name__], strShipClass)

#Create a random ship using gacha stats to a lib
def make_rand_ship(someLib, sCmd):
    someClass = getClass(randShipClass())
    newShip = someClass(randint(1, 10000), randName())
    newShip.command = sCmd
    randStats(newShip)
    someLib.append(newShip)

#create random ships
def create_rand_ships(someShipLib, sCmd, n):
    while n > 0:
        make_rand_ship(someShipLib, sCmd)
        n -= 1