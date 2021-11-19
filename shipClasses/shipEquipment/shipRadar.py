#finds the hexes in range

class shipHexRadar:

    def __init__(self, vesselID, radarClass):
        self.radarClass = int(radarClass)
        self.equipID = '-'.join([vesselID, 'HXRDR', str(radarClass)])


    def findGunTargets(self, gunRange, shipplaceHex, targetShip):
        nearby = self._findHexes(gunRange, shipplaceHex) 
        targets = []
        for k in nearby:
            if k.empty == False and k.entity.command != shipplaceHex.entity.command and k.entity == targetShip:
              targets.append(k)

        #returns a starSpace
        return targets


    def findRadarTargets(self, radarRange, shipplaceHex):
        nearby = self._findHexes(radarRange, shipplaceHex) 
        targets = []
        for k in nearby:
            if k.empty == False and k.entity.command != shipplaceHex.entity.command:
              targets.append(k)

        #returns a starSpace
        return targets
    

    def _findHexes(self, requestedRange, aHexSpace):
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