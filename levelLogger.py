#levels 
from gameField.spaceGame import turn_combat_game
#from shipCreater import *
from fleetManager import *
from fleetLogger import *
from starSpaces import *
from levelManager import *

class level():

    def __init__(self, level_path):
        game_levels = starLevelOpen()
        if level_path in game_levels[0]["levels"]:
            self.name = game_levels[0]["levels"][level_path]["Name"]
            self.level_hex_map = create_map_hexes(game_levels[0]["levels"][level_path]["Length"], game_levels[0]["levels"][level_path]["Width"], game_levels[0]["levels"][level_path]["RhoDensity"])
            self.fleet_spawn = game_levels[0]["levels"][level_path]["SpawnLocations"]
            self.level_fleets = []

            for i, x in enumerate(game_levels[0]["levels"][level_path]["Fleets"]):
                new_fleet_command, new_fleet_name = x[0], x[1]
                new_fleet = space_fleet(new_fleet_name, new_fleet_command)
                launch_fleet(new_fleet)
                new_fleet.spawn_fleet(self.level_hex_map, self.fleet_spawn[i])
                self.level_fleets.append(new_fleet)
                
            self.map_game = turn_combat_game(self.level_hex_map)


        else:
            print("Invalid Level")

#uLvl = level("level_Test")
