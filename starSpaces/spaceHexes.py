#space grid in hexes

#hex space
class starSpace:

    def __init__(self, hexNumber): 
        self.hex_coordinate_index = hexNumber
        self.entity = []
        self.neighbors = []
        self.directions = {'R': 0, 'L': -1, 'UR': 0, 'UL': 0, 'DR': -1, 'DL': -1}
        self.empty = True

    def addEntity(self, newEntity):
        if self.empty:
            newEntity.placeHex = self
            self.entity = newEntity
            self.empty = False
        else:
            print("Space Occupied")
            return 


#operation Space/Zone
class zoneSpace:
    
    def __init__(self, length, width):
        n = 0
        self.l = length
        self.w = width
        self.starHexes = []
        self.hexes_full = []
        self.fleet_entities = []
        self.game_entities = {'spaceObject': [], 'ship_entity': []}
        for n in range(self.l * self.w):
            self.starHexes.append(starSpace(n))


    # add an entity to the zone and a starSpace
    def addCustomEntity(self, aStarSpace, newEntity):
            aStarSpace.addEntity(newEntity) 
            self.hexes_full.append(aStarSpace)
            self.game_entities[newEntity.entity_type].append(newEntity)

    #click move
    def move_some_entity(self, movable_entity, selected_hex):
        old_hex_coordinate_index = movable_entity.placeHex.hex_coordinate_index
        new_hex_coordinate_index = selected_hex.hex_coordinate_index
        if not selected_hex.empty:
            print("Hex Occupied!")
            return False

        for key in self.starHexes[old_hex_coordinate_index].directions:
            if self.starHexes[old_hex_coordinate_index].directions[key] == new_hex_coordinate_index:
                movable_entity.orientation = key

        self.hexes_full.remove(self.starHexes[old_hex_coordinate_index])
        self.hexes_full.append(self.starHexes[new_hex_coordinate_index])
        self.starHexes[new_hex_coordinate_index].addEntity(movable_entity)
        self.starHexes[old_hex_coordinate_index].entity = []
        self.starHexes[old_hex_coordinate_index].empty = True
        print("Moved From: Space Hex", old_hex_coordinate_index, end=' ')
        print("To: Space Hex", movable_entity.placeHex.hex_coordinate_index)
        return True