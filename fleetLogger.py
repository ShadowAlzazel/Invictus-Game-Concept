import sys
from shipClasses import *

#creates a ships from fleet log
def fleetLaunch(aFleet):

    def getSomeClass(nameOfShipClass):
        return getattr(sys.modules[__name__], nameOfShipClass)

    if aFleet.presetFleet:
        n = 0
        for aShips in aFleet.fleetLogs['shipNames']:
            aClass = getSomeClass(aFleet.fleetLogs['shipClasses'][n])
            newShip = aClass(aFleet.fleetLogs['shipHullnumber'][n], aShips)
            newShip.command = ''.join([aFleet.fleetCommand, 'S'])
            aFleet.fleetShips.append(newShip)
            n += 1

