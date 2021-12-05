#levels 
from gameField.spaceGame import turnGame
from shipCreater import *
from fleetManager import *
from fleetLogger import *
from starSpaces import *
from levelManager import *

class level():

    def __init__(self, levelPaths):
        game_levels = starLevelOpen()
        if levelPaths in game_levels[0]["levels"]:
            self.name = game_levels[0]["levels"][levelPaths]["Name"]
            self.level_hex_map = create_map_hexes(game_levels[0]["levels"][levelPaths]["Length"], game_levels[0]["levels"][levelPaths]["Width"], game_levels[0]["levels"][levelPaths]["RhoDensity"])
            self.fleet_spawn = game_levels[0]["levels"][levelPaths]["SpawnLocations"]
            self.level_fleets = []
            for i, x in enumerate(game_levels[0]["levels"][levelPaths]["Fleets"]):
                new_fleet_command, new_fleet_name = x[0], x[1]
                new_fleet = space_fleet(new_fleet_name, new_fleet_command)
                launch_fleet(new_fleet)
                new_fleet.spawn_fleet(self.level_hex_map, self.fleet_spawn[i])
                self.level_fleets.append(new_fleet)
            self.areaGame = turnGame(self.level_hex_map)


        else:
            print("Invalid Level")

    #def __init__(self, name, length, width, rho, fleets, locations):
    #    self.name = name
    #    self.level_hex_map =  create_map_hexes(length, width, rho)
    #    self.level_fleets = [x for x in fleets]
    #    self.fleet_spawn = locations 
    #    for i, x in enumerate(self.level_fleets):
    #        launch_fleet(x)
    #        x.spawn_fleet(self.level_hex_map, locations[i])
    #    self.areaGame = turnGame(self.level_hex_map)


#fleet1 = space_fleet(astraFleets[0]['ASC']['fleetNames'][1], 'ASC')
#fleet2 = space_fleet(astraFleets[0]['XNFF']['fleetNames'][0], 'XNFF')
#level1 = level(14, 10, 0 ,(fleet1, fleet2), [40, 104])

#uLvl = level("level_Test")
