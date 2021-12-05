#space grid in hexes

#hex space
class space_hex:

    def __init__(self, hexNumber): 
        self.hex_coordinate_index = hexNumber
        self.entity = []
        self.neighbors = []
        self.directions = {'R': 0, 'L': -1, 'UR': 0, 'UL': 0, 'DR': -1, 'DL': -1}
        self.empty = True

    def add_space_entity(self, new_entity):
        if self.empty:
            new_entity.place_hex = self
            self.entity = new_entity
            self.empty = False
        else:
            print("Space Occupied")
            return 


#hex map
class base_hex_map:
    
    def __init__(self, length, width):
        n = 0
        self.map_length = length
        self.map_width = width
        self.space_hexes = []
        self.hexes_full = []
        self.fleet_entities = []
        self.game_entities = {'spaceObject': [], 'ship_entity': []}
        for n in range(length * width):
            self.space_hexes.append(space_hex(n))


    # add an entity to the zone and a space_hex
    def add_new_entity(self, some_space_hex, new_entity):
            some_space_hex.add_space_entity(new_entity) 
            self.hexes_full.append(some_space_hex)
            self.game_entities[new_entity.entity_type].append(new_entity)

    #click move
    def move_some_entity(self, movable_entity, selected_hex):
        old_hex_coordinate_index = movable_entity.place_hex.hex_coordinate_index
        new_hex_coordinate_index = selected_hex.hex_coordinate_index
        if not selected_hex.empty:
            print("Hex Occupied!")
            return False

        for key in self.space_hexes[old_hex_coordinate_index].directions:
            if self.space_hexes[old_hex_coordinate_index].directions[key] == new_hex_coordinate_index:
                movable_entity.orientation = key

        self.hexes_full.remove(self.space_hexes[old_hex_coordinate_index])
        self.hexes_full.append(self.space_hexes[new_hex_coordinate_index])
        self.space_hexes[new_hex_coordinate_index].add_space_entity(movable_entity)
        self.space_hexes[old_hex_coordinate_index].entity = []
        self.space_hexes[old_hex_coordinate_index].empty = True
        print("Moved From: Space Hex", old_hex_coordinate_index, end=' ')
        print("To: Space Hex", movable_entity.place_hex.hex_coordinate_index)
        return True