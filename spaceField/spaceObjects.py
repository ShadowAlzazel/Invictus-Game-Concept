#innanimate objects

class spaceObject():
    spaceEntity = 'spaceObject'
    ammount = 0

    def __init__(self, objectNum):
        spaceObject.ammount += 1
        self.objectNumber = objectNum
        self.name = ''.join(["objects", str(objectNum)])
        self.placeSpace = []
        
