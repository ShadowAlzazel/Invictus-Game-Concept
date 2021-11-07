#get class from available class
import sys
from shipClasses import *
from shipGacha.randomGacha import randName, randShipClass 
from random import randint

def getClass(strShipClass):
    return getattr(sys.modules[__name__], strShipClass)

#Create a random ship using gacha stats to a lib
def gachaRandShip(someLib):
    someClass = getClass(randShipClass())
    newShip = someClass(randint(1, 10000), randName())
    someLib.append(newShip)