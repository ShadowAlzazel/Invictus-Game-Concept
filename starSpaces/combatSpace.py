from starSpaces.spaceHexes import *
from starSpaces.spaceObjects import *
from random import randint

def create_map_hexes(length, width, density):
    new_hex_map = base_hex_map(length, width)
    area = length * width
    rho = int(((density * 0.01) * area) // 1)
    rho_objects = []

    #get neighbors function
    def get_neighbors(some_space_hex):
        hex_coordinate_index = some_space_hex.hex_coordinate_index
        neighbors = []
        hex_moves = {'Right': 1, 
                    'Left': -1, 
                    'UpRight': (((hex_coordinate_index // length) % 2) + length),
                    'UpLeft': ((((hex_coordinate_index // length) % 2) + length) - 1),
                    'DownRight': (((hex_coordinate_index // length) % 2) - length),
                    'DownLeft': ((((-(hex_coordinate_index // length) % 2)) - length) - 1)
                    }

        #check for right hex border
        if not (hex_coordinate_index + 1) % length == 0:
            j = new_hex_map.space_hexes[hex_coordinate_index + hex_moves['Right']]
            some_space_hex.directions['R'] = j.hex_coordinate_index
            neighbors.append(j)

        #check for left hex borders
        if not hex_coordinate_index % length == 0:
            j = new_hex_map.space_hexes[hex_coordinate_index + hex_moves['Left']]
            some_space_hex.directions['L'] = j.hex_coordinate_index
            neighbors.append(j)

        #check for up-right hex borders
        if not (hex_coordinate_index >= length * (width - 1)) and not ((hex_coordinate_index // length) % 2 == 1 and (hex_coordinate_index + 1) % length == 0):
            j = new_hex_map.space_hexes[hex_coordinate_index + hex_moves['UpRight']]
            some_space_hex.directions['UR'] = j.hex_coordinate_index
            neighbors.append(j)
        
        #check for up-left hex borders
        if not (hex_coordinate_index) >= length * (width - 1) and not ((hex_coordinate_index // length) % 2 == 0 and hex_coordinate_index % length == 0):
            j = new_hex_map.space_hexes[hex_coordinate_index + hex_moves['UpLeft']]
            some_space_hex.directions['UL'] = j.hex_coordinate_index
            neighbors.append(j)

        #check for down-right hex borders
        if not (hex_coordinate_index) // length == 0 and not ((hex_coordinate_index // length) % 2 == 1 and (hex_coordinate_index + 1) % length == 0):
            j = new_hex_map.space_hexes[hex_coordinate_index + hex_moves['DownRight']]
            some_space_hex.directions['DR'] = j.hex_coordinate_index
            neighbors.append(j)

        #check for down-left hex borders
        if not (hex_coordinate_index) // length == 0 and not ((hex_coordinate_index // length) % 2 == 0 and hex_coordinate_index % length == 0):
            j = new_hex_map.space_hexes[hex_coordinate_index + hex_moves['DownLeft']]
            some_space_hex.directions['DL'] = j.hex_coordinate_index
            neighbors.append(j)

        return neighbors

    #add random objects
    for x in range(0, rho):
        rho_objects.append(randint(0, area - 1))
        new_hex_map.add_new_entity(new_hex_map.space_hexes[rho_objects[x]], spaceObject(x))

    #make neighbors for space_hexes
    for z in new_hex_map.space_hexes:
        z.neighbors = get_neighbors(z)

    return new_hex_map