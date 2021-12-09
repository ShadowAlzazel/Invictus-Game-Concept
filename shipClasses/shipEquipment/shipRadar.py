#ship radar object for hexes
from functools import lru_cache

class hex_radar:

    def __init__(self, vessel_ID, radar_class):
        self.radar_class = int(radar_class)
        self.equipment_ID = '-'.join([vessel_ID, 'HXRDR', str(radar_class)])


    #ping nearby with radar
    def radar_pinger(self, ship_hex_place, pinged_hex):
        hexes_nearby, ring = self._hex_finder(1, ship_hex_place)
        hexes_nearby_ping, ringPing = self._hex_finder(1, pinged_hex) 
        enemy_pinged = False 
        for k, u in zip(hexes_nearby, hexes_nearby_ping):
            if not k.empty and k.entity.command[0:3] != ship_hex_place.entity.command[0:3]:
                enemy_pinged = True 
            if not u.empty and u.entity.command[0:3] != ship_hex_place.entity.command[0:3]:
                enemy_pinged = True
        return enemy_pinged


    #acquires a target and returns a range
    def radar_ballistics_finder(self, radar_range, ship_hex_place, target_hex):
        hexes_nearby, hex_rings = self._hex_finder(radar_range, ship_hex_place) 
        if target_hex.entity.command[0:3] != ship_hex_place.entity.command[0:3]:
            for i in range(1, radar_range + 1):
                if target_hex in hex_rings[i] and target_hex in hexes_nearby:
                    return i


    #track revealed targets
    def radar_tracker(self, radar_range, ship_hex_place):
        hexes_nearby, hex_rings = self._hex_finder(radar_range, ship_hex_place) 
        targets_hex_places = []
        for k in hexes_nearby:
            if not k.empty and k.entity.command[0:3] != ship_hex_place.entity.command[0:3]:
                if k.entity.detected or k.entity.revealed:
                    targets_hex_places.append(k)
        #returns a space_hex
        return targets_hex_places


    #detect targets in range and stealthed
    def radar_detecter(self, radar_range, ship_hex_place):
        hexes_nearby, hex_rings = self._hex_finder(radar_range, ship_hex_place) 
        target_hex_places = []
        for k in hexes_nearby:
            if not k.empty and k.entity.command[0:3] != ship_hex_place.entity.command[0:3]:
                u = self._detect_enemy_limiter(hex_rings, k, radar_range)
                if u:
                    target_hex_places.append(k)
        #returns a space_hex
        return target_hex_places


    #check if the stealth of the ship is within detection range
    def _detect_enemy_limiter(self, hex_ring, enemy_hex_place, detection_range):
        enemy_stealth = enemy_hex_place.entity.ship_stats['STH']
        enemy_detected_bool = any(enemy_hex_place in hex_ring[z] for z in range(1, (detection_range - enemy_stealth) + 1))
        return enemy_detected_bool


    #find hexes in rings
    @lru_cache(maxsize=2)
    def _hex_finder(self, requested_range, some_hex_space):
        assert requested_range != 0
        range_EFF = requested_range 
        if range_EFF > self.radar_class:
            range_EFF = self.radar_class
        origin_hex = some_hex_space
        hexes_nearby = []
        hex_rings = [[some_hex_space]]

        def hex_finder_recursor(range_EFF, prev_hex_ring, n=1): 
            new_hex_ring = []
            for z in prev_hex_ring:
                for y in z.neighbors:
                    if y not in new_hex_ring and y != origin_hex and y not in prev_hex_ring:
                        new_hex_ring.append(y)

            u_ring = []
            for k in new_hex_ring:
                if k not in hexes_nearby:
                    hexes_nearby.append(k)
                    u_ring.append(k)
            hex_rings.append(u_ring)

            if n != range_EFF:
                hex_finder_recursor(range_EFF, new_hex_ring, n + 1)

            return hexes_nearby, hex_rings
        return hex_finder_recursor(range_EFF, [origin_hex])