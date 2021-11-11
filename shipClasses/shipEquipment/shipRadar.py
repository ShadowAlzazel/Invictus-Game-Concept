#finds the hexes in range

class shipHexRadar:

    def __init__(self, vesselID, radarClass):
        self.radarClass = int(radarClass)
        self.equipID = '-'.join([vesselID, 'HXRDR', str(radarClass)])


    def findGunTargets(self, gunRange, shipPlaceSpace, targetShip):
        nearby = self.findHexes(gunRange, shipPlaceSpace) 
        targets = []
        for k in nearby:
            if k.empty == False and k.entity.command != shipPlaceSpace.entity.command and k.entity == targetShip:
              targets.append(k)

        #returns a starSpace
        return targets


    def findRadarTargets(self, radarRange, shipPlaceSpace):
        nearby = self.findHexes(radarRange, shipPlaceSpace) 
        targets = []
        for k in nearby:
            if k.empty == False and k.entity.command != shipPlaceSpace.entity.command:
              targets.append(k)

        #returns a starSpace
        return targets
    

    def findHexes(self, requestedRange, aHexSpace):
        assert requestedRange != 0
        effRange = requestedRange 
        if effRange > self.radarClass:
            effRange = self.radarClass
        originHex = aHexSpace
        hexesNearby = []
        originRing = [aHexSpace]

        def hexesInRange(effRange, someHexRing, n = 1): #n = 1
            thisHexRing = someHexRing
            newHexRing  = []
            for z in thisHexRing:
                for y in z.neighbors:
                    if y not in newHexRing and y != originHex and y not in someHexRing:
                        newHexRing.append(y)

            if n != effRange:
                hexesInRange(effRange, newHexRing, n + 1)

            for k in newHexRing:
                if k not in hexesNearby:
                    hexesNearby.append(k)

            return hexesNearby
        return hexesInRange(effRange, originRing)


