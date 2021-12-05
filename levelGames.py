#levels 
from gameField.spaceGame import turnGame
from shipCreater import *
from fleetManager import *
from fleetLogger import *
from starSpaces import *
from levelManager import *

class level():

    def __init__(self, levelPaths):
        starLevels = starLevelOpen()
        if levelPaths in starLevels[0]["levels"]:
            self.name = starLevels[0]["levels"][levelPaths]["Name"]
            self.engagementSpace = create_map_hexes(starLevels[0]["levels"][levelPaths]["Length"], starLevels[0]["levels"][levelPaths]["Width"], starLevels[0]["levels"][levelPaths]["RhoDensity"])
            self.fleetSpawns = starLevels[0]["levels"][levelPaths]["SpawnLocations"]
            self.levelFleets = []
            for i, x in enumerate(starLevels[0]["levels"][levelPaths]["Fleets"]):
                newFleetCom, newFleetName = x[0], x[1]
                newFleet = spaceFleet(newFleetName, newFleetCom)
                launch_fleet(newFleet)
                newFleet.spawnFleet(self.engagementSpace, self.fleetSpawns[i])
                self.levelFleets.append(newFleet)
            self.areaGame = turnGame(self.engagementSpace)


        else:
            print("Invalid Level")

    #def __init__(self, name, length, width, rho, fleets, locations):
    #    self.name = name
    #    self.engagementSpace =  create_map_hexes(length, width, rho)
    #    self.levelFleets = [x for x in fleets]
    #    self.fleetSpawns = locations 
    #    for i, x in enumerate(self.levelFleets):
    #        launch_fleet(x)
    #        x.spawnFleet(self.engagementSpace, locations[i])
    #    self.areaGame = turnGame(self.engagementSpace)


#fleet1 = spaceFleet(astraFleets[0]['ASC']['fleetNames'][1], 'ASC')
#fleet2 = spaceFleet(astraFleets[0]['XNFF']['fleetNames'][0], 'XNFF')
#level1 = level(14, 10, 0 ,(fleet1, fleet2), [40, 104])

#uLvl = level("level_Test")
