#ship radar object for hexes
class hex_radar:

    def __init__(self, vessel_ID, radar_LIM):
        self.radar_LIM = int(radar_LIM)
        self.equipment_ID = '-'.join([vessel_ID, 'HXRDR', str(radar_LIM)])


    #ping nearby with radar
    def radarPing(self, ship_hex_place, pinged_hex):
        nearby, ring = self._hex_finder(1, ship_hex_place)
        nearbyPing, ringPing = self._hex_finder(1, pinged_hex) 
        enemyPing = False 
        for k, u in zip(nearby, nearbyPing):
            if not k.empty and k.entity.command[0:3] != ship_hex_place.entity.command[0:3]:
                enemyPing = True 
            if not u.empty and u.entity.command[0:3] != ship_hex_place.entity.command[0:3]:
                enemyPing = True
        return enemyPing


    #acquires a target and returns a range
    def radarAcquisition(self, radarRange, ship_hex_place, targetHex):
        nearby, ring = self._hex_finder(radarRange, ship_hex_place) 

        #q = []
        #for j in ring:
        #    u = []
        #    for l in j:
        #        u.append(l.hexCoord)
        #    q.append(u)
        #print(q)

        if targetHex.entity.command[0:3] != ship_hex_place.entity.command[0:3]:
            for z in range(1, radarRange + 1):
                if targetHex in ring[z] and targetHex in nearby:
                    return z


    #track revealed targets
    def radarTracking(self, radarRange, ship_hex_place):
        nearby, ring = self._hex_finder(radarRange, ship_hex_place) 
        targetsSpace = []
        for k in nearby:
            if not k.empty and k.entity.command[0:3] != ship_hex_place.entity.command[0:3]:
                if k.entity.detected or k.entity.revealed:
                    targetsSpace.append(k)
        #returns a starSpace
        return targetsSpace


    #detect targets in range and stealthed
    def radarDetection(self, radarRange, ship_hex_place):
        nearby, ring = self._hex_finder(radarRange, ship_hex_place) 
        targetsSpace = []
        for k in nearby:
            if not k.empty and k.entity.command[0:3] != ship_hex_place.entity.command[0:3]:
                u = self._detectionRange(ring, k, radarRange)
                if u:
                    targetsSpace.append(k)
        #returns a starSpace
        return targetsSpace


    #check if the stealth of the ship is within detection range
    def _detectionRange(self, radarRing, eShipHex, detectionRange):
        shipStealth = eShipHex.entity.ship_stats['STH']
        enemyDetected = any(eShipHex in radarRing[z] for z in range(1, (detectionRange - shipStealth) + 1))
        return enemyDetected


    #find hexes in rings
    def _hex_finder(self, requestedRange, aHexSpace):
        assert requestedRange != 0
        effRange = requestedRange 
        if effRange > self.radar_LIM:
            effRange = self.radar_LIM
        originHex = aHexSpace
        hexesNearby = []
        nearbyRing = [[aHexSpace]]

        def hex_finder_recursor(effRange, someHexRing, n=1): 
            prevHexRing = someHexRing
            newHexRing = []
            for z in prevHexRing:
                for y in z.neighbors:
                    if y not in newHexRing and y != originHex and y not in prevHexRing:
                        newHexRing.append(y)

            u = []
            for k in newHexRing:
                if k not in hexesNearby:
                    hexesNearby.append(k)
                    u.append(k)
            nearbyRing.append(u)

            if n != effRange:
                hex_finder_recursor(effRange, newHexRing, n + 1)

            return hexesNearby, nearbyRing
        return hex_finder_recursor(effRange, [originHex])