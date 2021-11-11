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
        if fleetCommand in astraFleets[0]:
            if name in astraFleets[0][fleetCommand]['fleetNames']:
                self.presetFleet = True
                self.fleetLogs = astraFleets[0][fleetCommand][name]
        

    def spawnFleet(self, operationSpace, formation = 0):
        operationSpace.fleetEntities.append(self)

        if formation == 0:  #cluster
            k, n = 0, 1
            r = randint(0, (operationSpace.l * operationSpace.w) - 1)
            if operationSpace.starSpaceHexes[r].empty:
                fleetSpawnP = operationSpace.starSpaceHexes[r]
            else:
                print("Spawn Failed")
                return 

            operationSpace.addCustomEntity(fleetSpawnP, self.fleetShips[k])
            spawning = True
            while spawning:
                for hex in self.fleetShips[k].placeSpace.neighbors:
                    if n == len(self.fleetShips):
                        spawning = False
                    elif hex.empty:
                        operationSpace.addCustomEntity(hex, self.fleetShips[n])
                        n += 1
                k += 1


