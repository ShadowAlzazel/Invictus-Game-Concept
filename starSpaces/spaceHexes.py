#space grid in hexes

#hex space
class starSpace:

    def __init__(self, hexNumber): 
        self.hexCoord = hexNumber
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
        self.hexesFull = []
        self.fleetEntities = []
        self.spaceEntities = {'spaceObject': [], 'ship_entity': []}
        for n in range(self.l * self.w):
            self.starHexes.append(starSpace(n))


    # add an entity to the zone and a starSpace
    def addCustomEntity(self, aStarSpace, newEntity):
            aStarSpace.addEntity(newEntity) 
            self.hexesFull.append(aStarSpace)
            self.spaceEntities[newEntity.entity_type].append(newEntity)

    #click move
    def moveClickEntity(self, movableEntity, clickHex):
        oldHexCoord = movableEntity.placeHex.hexCoord
        newHexCoord = clickHex.hexCoord
        if not clickHex.empty:
            print("Hex Occupied!")
            return False

        for key in self.starHexes[oldHexCoord].directions:
            if self.starHexes[oldHexCoord].directions[key] == newHexCoord:
                movableEntity.orientation = key

        self.hexesFull.remove(self.starHexes[oldHexCoord])
        self.hexesFull.append(self.starHexes[newHexCoord])
        self.starHexes[newHexCoord].addEntity(movableEntity)
        self.starHexes[oldHexCoord].entity = []
        self.starHexes[oldHexCoord].empty = True
        print("Moved From: Space Hex", oldHexCoord, end=' ')
        print("To: Space Hex", movableEntity.placeHex.hexCoord)
        return True