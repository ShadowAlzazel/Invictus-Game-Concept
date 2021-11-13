#space grid in hexes

#hex space
class starSpace:
    def __init__(self, hexNumber): 
        self.coord = {'hexNum': hexNumber}
        self.entity = []
        self.neighbors = []
        self.empty = True

    def addEntity(self, newEntity):
        if self.empty:
            newEntity.placeSpace = self
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
        self.starSpaceHexes = []
        self.hexesFull = []
        self.fleetEntities = []
        self.spaceEntities = {'spaceObject': [], 'shipObject': []}
        for n in range(0, self.l * self.w):
            self.starSpaceHexes.append(starSpace(n))


    # add an entity to the zone and a starSpace
    def addCustomEntity(self, aStarSpace, newEntity):
            aStarSpace.addEntity(newEntity) 
            self.hexesFull.append(aStarSpace)
            self.spaceEntities[newEntity.spaceEntity].append(newEntity)

    #click move
    def moveClickEntity(self, movableEntity, clickHex):
        oldHexCoord = movableEntity.placeSpace.coord['hexNum']
        newHexCoord = clickHex.coord['hexNum']
        if not clickHex.empty:
            print("Hex Occupied!")
            return False

        self.hexesFull.remove(self.starSpaceHexes[oldHexCoord])
        self.hexesFull.append(self.starSpaceHexes[newHexCoord])
        self.starSpaceHexes[newHexCoord].addEntity(movableEntity)
        self.starSpaceHexes[oldHexCoord].entity = []
        self.starSpaceHexes[oldHexCoord].empty = True
        print("Moved From: Space Hex", oldHexCoord, end=' ')
        print("To: Space Hex", movableEntity.placeSpace.coord['hexNum'])
        return True
