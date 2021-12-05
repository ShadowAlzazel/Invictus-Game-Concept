import json
from random import randint

with open("fleetManager\starFleets.json", "r") as astraFleetsFile:
    astraFleets = json.load(astraFleetsFile)

#fleet which contains ship
class spaceFleet:
    presetFleet = False

    def __init__(self, name, fleetCommand):
        self.name = name
        self.fleetCommand = fleetCommand   # usually 'ASC'
        self.fleetLogs = []
        self.fleetShips = []
        self.flagShip = 0
        self.trackedShipsHexes = []
        #check if preset fleet
        if fleetCommand in astraFleets[0] and name in astraFleets[0][fleetCommand]['fleetNames']:
            self.presetFleet = True
            self.fleetLogs = astraFleets[0][fleetCommand][name]
        

    def spawnFleet(self, operationSpace, start=-1, formation=0):
        operationSpace.fleetEntities.append(self)
        #cluster formation
        if formation == 0:
            k, n = 0, 1
            #if -1 random spawn
            if start == -1: 
                r = randint(0, (operationSpace.l * operationSpace.w) - 1)
                if operationSpace.starHexes[r].empty:
                    fleetSpawnLoc = operationSpace.starHexes[r]
                else:
                    print("Spawn Failed")
                    return 
            elif start > 0:
                fleetSpawnLoc = operationSpace.starHexes[start]

            #spawn the fleet in the zoneSpace
            operationSpace.addCustomEntity(fleetSpawnLoc, self.fleetShips[k])
            spawning = True
            while spawning:
                for hex in self.fleetShips[k].placeHex.neighbors:
                    if n == len(self.fleetShips):
                        spawning = False
                    elif hex.empty:
                        operationSpace.addCustomEntity(hex, self.fleetShips[n])
                        n += 1
                k += 1