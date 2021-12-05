#a turn based combat game
from random import randint

class turnGame:
    #Query = {'No': ['No', 'no', 'N', 'n'], 'Yes': ['Yes', 'yes', 'Y', 'y'], 
    #        'Inspect': ['I', 'Inspect', 'i', 'inspect', 'ins'], 'Skip': ['Skip', 'skip', 'S', 's'],
    #        'Move': ['Move', 'move', 'm', 'M'], 'End': ['End', 'end', 'finish', 'Finish', 'E', 'e'],
    #        'Attack': ['Attack', 'attack', 'atk', 'Atk', 'a', 'A', 'ATK'], 'AutoAttack': ['AutAttack', 'autoattack', 'auto', 'aa', 'AA']
    #        }

    def __init__(self, map_hexes):
        self.opsSpace = map_hexes
        self.game_ships = map_hexes.game_entities['ship_entity']
        self.game_fleets = map_hexes.fleet_entities
        self.game_turn = 0
        self.selected_hex = None #usually a hex
        self.active_fleet = self.game_fleets[-1]
        self.active_fleet_index = len(self.game_fleets) - 1
        for f in self.game_fleets:
            self._update_ships(f)
            self._update_detections(f)     


    #fleet Actions
    def next_fleet_turn(self):
        self.selected_hex = None 
        q = self.active_fleet_index
        if q == len(self.game_fleets) - 1:
            self.game_turn += 1
            self.active_fleet_index = 0
            self.active_fleet = self.game_fleets[0]
        else:
            self.active_fleet_index += 1
            self.active_fleet = self.game_fleets[q + 1]
        self._update_ships(self.active_fleet)
        self._update_detections(self.active_fleet)


    #update ships in fleet turn
    def _update_ships(self, some_fleet):
        for s in some_fleet.fleet_ships:
            s.ship_moves = s.ship_stats['SPD']
            s.ship_attacks = 1
            s.ship_active = True
            s.reload_battery()
            s.recharge_defenses()


    #select shiphex
    def select_hex(self, some_hex):
        #check if there is a previously selected hex
        if self.selected_hex:
            #check if hexShip has any actions
            if self.selected_hex.entity.ship_moves == 0:
                #check if any targets available
                nearbyShipHexes = self.selected_hex.entity.track_targets()
                if not nearbyShipHexes:
                    self.selected_hex.entity.ship_active = False

            result = self._shipActions(some_hex)
            self._update_detections(self.active_fleet)
            if not result:
                self.selected_hex = None 
                self.select_hex(some_hex)

        aShip = some_hex.entity
        #can only select a ship
        if not some_hex.empty and self.active_fleet.fleetCommand[0:3] == aShip.command[0:3] and aShip.operational:
            self.selected_hex = some_hex
            return True
        return False 
        

    #all availabe ship actions
    def _shipActions(self, some_hex):
        result = False
        if not self.selected_hex.entity.ship_active:
            print("No possible actions left")
            return False

        #check if moves available
        if self.selected_hex.entity.ship_moves != 0:
            result = self._moveShipAction(some_hex)     
        else:
            print("No Movements available")   

        #if no movement triggered, check for attacks
        if not result:
            result = self._attackShipAction(some_hex)

        return result


    #detect ships for fleet
    def _update_detections(self, some_fleet):
        for s in self.game_ships:
            if s.command[0:3] != some_fleet.fleetCommand[0:3]:
                s.detected = False
            else: 
                s.detected = True 

        enemiesDetected = []
        for a in some_fleet.fleet_ships:
            if a.operational:
                for x in a.detect_targets():
                    enemiesDetected.append(x)

        for e in set(enemiesDetected):
            e.entity.detected = True


    #attack action; check for minimum  range, and guns in ranges
    def _attackShipAction(self, some_hex):
        aShip = self.selected_hex.entity
        if not aShip.guns_primed():
            aShip.ship_attacks = 0
            print("No guns loaded")
            return False

        #selected hex must be a target
        nearbyShipHexes = aShip.track_targets()
        if some_hex not in nearbyShipHexes:
            return False

        result = self._shipSalvoAction(aShip, some_hex.entity)
        return result


    #move ship on board
    def _moveShipAction(self, some_hex):
        result = False
        selectedShip = self.selected_hex.entity
        #check if selcted hex direction does not match orientation
        if some_hex.empty and (some_hex in self.selected_hex.neighbors) and (some_hex.directions[selectedShip.orientation] != self.selected_hex.hexCoord or selectedShip.ship_type == 'DD' or selectedShip.ship_type == 'CS'):
            if selectedShip.ship_type == 'BB' and self.opsSpace.starHexes[some_hex.directions[selectedShip.orientation]] in self.selected_hex.neighbors:
                return result

            if selectedShip.ship_moves != 0:
                result = self.opsSpace.moveClickEntity(selectedShip, some_hex)
                if result:
                    selectedShip.ship_moves -= 1
                    #check if hex controlled
                    if selectedShip.ship_moves != 0:
                        enemyControlled = selectedShip.ping_hex(some_hex)
                        if enemyControlled:
                            selectedShip.ship_moves -= 1

            else:
                print("No movements left!") 
        return result


    #fire all guns in range 
    def _shipSalvoAction(self, aShip, bShip):
        #check if guns are loaded
        gunToFire = aShip.guns_primed()
        broadSideE = 0
        for s in gunToFire:
            if s in aShip.armaments['broadside_battery']:
                if broadSideE % 2 == 1:
                    s.gun_load_time = 0
                    gunToFire.remove(s)
                broadSideE += 1

        #get the distance
        bDistance = aShip.range_finder(bShip)

        totalDamage = 0
        for g in gunToFire:
            if not bShip.operational:
                print("ship Destroyed!")
                return True
            salvoDamage = 0
            trueDamage = 0
            if g.gun_stats['RNG'] >= bDistance:
                #find FP distribution ammong batteries
                batPow = 0  
                if g in aShip.armaments['primary_battery']:
                    batPow = aShip.ship_stats['FP'] // len(aShip.armaments['primary_battery'])
                elif g in aShip.armaments['secondary_battery']:
                    batPow = aShip.ship_stats['FP'] // len(aShip.armaments['secondary_battery'])
                elif g in aShip.armaments['broadside_battery']:
                    batPow = aShip.ship_stats['FP'] // len(aShip.armaments['broadside_battery'])

                for a in range(0, g.gun_stats['QNT']):
                    if self.gunHitCalc(g.gun_stats['HIT'], aShip.ship_stats['ACC'], bShip.ship_stats['EVA']) is True:
                        salvoDamage += self.gunDamageCalc(g.gun_stats['ATK'], aShip.ship_stats['FP'], aShip.ship_stats['LCK'], bShip.ship_stats['LCK'], batPow)

                trueDamage = bShip.take_damage(salvoDamage, g.gun_stats['PEN'], g.gun_stats['DIS'])
                if not bShip.operational:
                    m = bShip.placeHex.hexCoord
                    self.game_ships.remove(bShip) 
                    self.opsSpace.hexesFull.remove(self.opsSpace.starHexes[m])
                    self.opsSpace.starHexes[m].entity = []
                    self.opsSpace.starHexes[m].empty = True
                    trueDamage = 0
                    #del bShip
                    return True

                if trueDamage > 0:
                    print(g.battery_ID, "Has Hit", bShip.name, "For", trueDamage, "Damage!")
                g.gun_load_time = 0
            totalDamage += trueDamage
            salvoDamage = 0
        print(aShip.vessel_ID, aShip.name, "Has done", totalDamage, "Total Damage to", bShip.vessel_ID, bShip.name)
        return True


    #hit calculator for a gun
    def gunHitCalc(self, aShipGunHit, aShipACC, bShipEVA):
        hitRate = (aShipACC - bShipEVA) + aShipGunHit
        randHit = randint(1, 100)
        gunHit = hitRate > randHit
        return gunHit


    #damage calculator for a gun
    def gunDamageCalc(self, aShipGunAtk, aShipFP, aShipLCK, bShipLCK, batDistro):
        critRate = aShipLCK - bShipLCK + 5
        damageMult = 1
        randCrit = randint(1, 100)
        if critRate > randCrit:
            damageMult = 1.25 + (aShipLCK / 100)
        damage = (aShipGunAtk + (aShipFP // batDistro) * damageMult)
        return damage