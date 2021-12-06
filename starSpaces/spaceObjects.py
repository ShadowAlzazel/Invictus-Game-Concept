#innanimate objects

class spaceObject():
    entity_type = 'spaceObject'
    ammount = 0

    def __init__(self, objectNum):
        spaceObject.ammount += 1
        self.objectNumber = objectNum
        self.name = ''.join(["objects", str(objectNum)])
        self.place_hex = []
