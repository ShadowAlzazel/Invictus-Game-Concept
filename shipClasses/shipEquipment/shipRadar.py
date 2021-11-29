#ship radar object for hexes
class shipHexRadar:

    def __init__(self, vesselID, radarClass):
        self.radarClass = int(radarClass)
        self.equipID = '-'.join([vesselID, 'HXRDR', str(radarClass)])


    #ping nearby with radar
    def radarPing(self, shipPlaceHex, aPlaceHex):
        nearby, ring = self._findHexes(1, shipPlaceHex)
        nearbyPing, ringPing = self._findHexes(1, aPlaceHex) 
        enemyPing = False 
        for k, u in zip(nearby, nearbyPing):
            if not k.empty and k.entity.command[0:3] != shipPlaceHex.entity.command[0:3]:
                enemyPing = True 
            if not u.empty and u.entity.command[0:3] != shipPlaceHex.entity.command[0:3]:
                enemyPing = True
        return enemyPing


    #acquires a target and returns a range
    def radarAcquisition(self, radarRange, shipPlaceHex, targetHex):
        nearby, ring = self._findHexes(radarRange, shipPlaceHex) 

        #q = []
        #for j in ring:
        #    u = []
        #    for l in j:
        #        u.append(l.hexCoord)
        #    q.append(u)
        #print(q)

        if targetHex.entity.command[0:3] != shipPlaceHex.entity.command[0:3]:
            for z in range(1, radarRange + 1):
                if targetHex in ring[z] and targetHex in nearby:
                    return z


    #track revealed targets
    def radarTracking(self, radarRange, shipPlaceHex):
        nearby, ring = self._findHexes(radarRange, shipPlaceHex) 
        targetsSpace = []
        for k in nearby:
            if not k.empty and k.entity.command[0:3] != shipPlaceHex.entity.command[0:3]:
                if k.entity.detected or k.entity.revealed:
                    targetsSpace.append(k)
        #returns a starSpace
        return targetsSpace


    #detect targets in range and stealthed
    def radarDetection(self, radarRange, shipPlaceHex):
        nearby, ring = self._findHexes(radarRange, shipPlaceHex) 
        targetsSpace = []
        for k in nearby:
            if not k.empty and k.entity.command[0:3] != shipPlaceHex.entity.command[0:3]:
                u = self._detectionRange(ring, k, radarRange)
                if u:
                    targetsSpace.append(k)
        #returns a starSpace
        return targetsSpace


    def _detectionRange(self, radarRing, eShipHex, detectionRange):
        s = eShipHex.entity.shipStats['STH']
        for z in range(1, (detectionRange - s) + 1):
            if eShipHex in radarRing[z]:
                return True         
        return False


    #find hexes in rings
    def _findHexes(self, requestedRange, aHexSpace):
        assert requestedRange != 0
        effRange = requestedRange 
        if effRange > self.radarClass:
            effRange = self.radarClass
        originHex = aHexSpace
        hexesNearby = []
        nearbyRing = [[aHexSpace]]

        def hexesInRange(effRange, someHexRing, n=1): 
            prevHexRing = someHexRing
            newHexRing = []
            for z in prevHexRing:
                for y in z.neighbors:
                    if y not in newHexRing and y != originHex and y not in prevHexRing:
                        newHexRing.append(y)

            u = []
            for k in newHexRing:
                if not (k in hexesNearby):
                    hexesNearby.append(k)
                    u.append(k)
            nearbyRing.append(u)

            if n != effRange:
                hexesInRange(effRange, newHexRing, n + 1)

            return hexesNearby, nearbyRing
        return hexesInRange(effRange, [originHex])