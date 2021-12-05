import json
from random import randint

with open("fleetManager\starFleets.json", "r") as astraFleetsFile:
    astraFleets = json.load(astraFleetsFile)

#fleet which contains ship
class spaceFleet:
    preset = False

    def __init__(self, name, fleetCommand):
        self.name = name
        self.fleetCommand = fleetCommand   # usually 'ASC'
        self.fleet_logs = []
        self.fleet_ships = []
        self.flagShip = 0
        self.trackedShipsHexes = []
        #check if preset fleet
        if fleetCommand in astraFleets[0] and name in astraFleets[0][fleetCommand]['fleetNames']:
            self.preset = True
            self.fleet_logs = astraFleets[0][fleetCommand][name]
        

    def spawnFleet(self, hex_map, start=-1, formation=0):
        hex_map.fleet_entities.append(self)
        #cluster formation
        if formation == 0:
            k, n = 0, 1
            #if -1 random spawn
            if start == -1: 
                r = randint(0, (hex_map.l * hex_map.w) - 1)
                if hex_map.space_hexes[r].empty:
                    fleetSpawnLoc = hex_map.space_hexes[r]
                else:
                    print("Spawn Failed")
                    return 
            elif start > 0:
                fleetSpawnLoc = hex_map.space_hexes[start]

            #spawn the fleet in the base_hex_map
            hex_map.add_new_entity(fleetSpawnLoc, self.fleet_ships[k])
            spawning = True
            while spawning:
                for hex in self.fleet_ships[k].place_hex.neighbors:
                    if n == len(self.fleet_ships):
                        spawning = False
                    elif hex.empty:
                        hex_map.add_new_entity(hex, self.fleet_ships[n])
                        n += 1
                k += 1