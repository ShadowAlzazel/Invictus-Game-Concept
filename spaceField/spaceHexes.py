#space grid in hexes
from spaceField.spaceBoard import makeGameBoard, showShipVision

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

    def showMap(self):
        makeGameBoard(self)

    def showMapShip(self, aShip):
        showShipVision(self, aShip)

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



    #check if the move is valid
    def moveEntity(self, movableEntity, direction):
        uR = ['UR', 'ur', 'uR']
        uL = ['UL', 'ul', 'uL']
        dR = ['DR', 'dr', 'dR']
        dL = ['DL', 'dl', 'dL']
        tR = ['TR', 'tr', 'tR', 'R', 'r']
        tL = ['tL', 'tl', 'tL', 'L', 'l']
        curHexCoord = movableEntity.placeSpace.coord['hexNum']
        result = False

        if direction in tR:
            if (curHexCoord + 1) % self.l == 0:
                print("Cannot move Right! At right border!")
            else:
                result = self.moveLocation(movableEntity, 'Right')

        elif direction in tL:
            if (curHexCoord) % self.l == 0:
                print("Cannot move Left! At left border!")
            else:
                result = self.moveLocation(movableEntity, 'Left')

        elif direction in uR:
            if (curHexCoord) >= self.l * (self.w - 1):
                print("Cannot move Up-Right! At top border!")
            elif (curHexCoord // self.l) % 2 == 1 and (curHexCoord + 1) % self.l == 0:
                print("Cannot move Up-Right! Even Rank Border Hex!")
            else:
                result = self.moveLocation(movableEntity, 'UpRight')

        elif direction in uL:
            if (curHexCoord) >= self.l * (self.w - 1):
                print("Cannot move Up-Left! At top border!")   
            elif (curHexCoord // self.l) % 2 == 0 and curHexCoord % self.l == 0:
                print("Cannot move Up-Left! Odd Rank Border Hex!")  
            else:
                result = self.moveLocation(movableEntity, 'UpLeft') 

        elif direction in dR:
            if (curHexCoord) // self.l == 0:
                print("Cannot move Down! At bottom border!")
            elif (curHexCoord // self.l) % 2 == 1 and (curHexCoord + 1) % self.l == 0:
                print("Cannot move Down-Right! Even Rank Border Hex!")
            else:
                result = self.moveLocation(movableEntity, 'DownRight')

        elif direction in dL: 
            if (curHexCoord) // self.l == 0:
                print("Cannot move Down! At bottom border!")
            elif (curHexCoord // self.l) % 2 == 0 and curHexCoord % self.l == 0:
                print("Cannot move Down-Left! Odd Rank Border Hex")
            else: 
                result = self.moveLocation(movableEntity, 'DownLeft')
                 
        else:
            result = False 
            print("Directions Unknown")

        return result

    #move the entity to the corresponding location and change list
    def moveLocation(self, movingEntity, vector):
        oldHexCoord = movingEntity.placeSpace.coord['hexNum']
        hexMoves = {'Right': 1, 
                    'Left': -1, 
                    'UpRight': (((oldHexCoord // self.l) % 2) + self.l),
                    'UpLeft': ((((oldHexCoord // self.l) % 2) + self.l) - 1),
                    'DownRight': (((oldHexCoord // self.l) % 2) - self.l),
                    'DownLeft': ((((-(oldHexCoord // self.l) % 2)) - self.l) - 1)
                    }
        if not self.starSpaceHexes[oldHexCoord + hexMoves[vector]].empty:
            print("Space Occupied!")
            return False

        self.hexesFull.remove(self.starSpaceHexes[oldHexCoord])
        self.hexesFull.append(self.starSpaceHexes[oldHexCoord + hexMoves[vector]])
        self.starSpaceHexes[oldHexCoord + hexMoves[vector]].addEntity(movingEntity)
        self.starSpaceHexes[oldHexCoord].entity = []
        self.starSpaceHexes[oldHexCoord].empty = True
        print("Moved From: Space Hex", oldHexCoord, end=' ')
        print("To: Space Hex", movingEntity.placeSpace.coord['hexNum'])
        return True
