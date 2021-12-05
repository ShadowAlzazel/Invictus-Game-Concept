#a turn based combat game
from random import randint

class turnGame:
    #Query = {'No': ['No', 'no', 'N', 'n'], 'Yes': ['Yes', 'yes', 'Y', 'y'], 
    #        'Inspect': ['I', 'Inspect', 'i', 'inspect', 'ins'], 'Skip': ['Skip', 'skip', 'S', 's'],
    #        'Move': ['Move', 'move', 'm', 'M'], 'End': ['End', 'end', 'finish', 'Finish', 'E', 'e'],
    #        'Attack': ['Attack', 'attack', 'atk', 'Atk', 'a', 'A', 'ATK'], 'AutoAttack': ['AutAttack', 'autoattack', 'auto', 'aa', 'AA']
    #        }

    def __init__(self, hex_map):
        self.opsSpace = hex_map
        self.game_ships = hex_map.game_entities['ship_entity']
        self.game_fleets = hex_map.fleet_entities
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
                nearby_enemy_hexes = self.selected_hex.entity.track_targets()
                if not nearby_enemy_hexes:
                    self.selected_hex.entity.ship_active = False

            result = self._game_ship_actions(some_hex)
            self._update_detections(self.active_fleet)
            if not result:
                self.selected_hex = None 
                self.select_hex(some_hex)

        some_ship = some_hex.entity
        #can only select a ship
        if not some_hex.empty and self.active_fleet.fleetCommand[0:3] == some_ship.command[0:3] and some_ship.operational:
            self.selected_hex = some_hex
            return True
        return False 
        

    #all availabe ship actions
    def _game_ship_actions(self, some_hex):
        result = False
        if not self.selected_hex.entity.ship_active:
            print("No possible actions left")
            return False

        #check if moves available
        if self.selected_hex.entity.ship_moves != 0:
            result = self._game_ship_move_action(some_hex)     
        else:
            print("No Movements available")   

        #if no movement triggered, check for attacks
        if not result:
            result = self._game_ship_attack_action(some_hex)

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
    def _game_ship_attack_action(self, some_hex):
        some_ship = self.selected_hex.entity
        if not some_ship.guns_primed():
            some_ship.ship_attacks = 0
            print("No guns loaded")
            return False

        #selected hex must be a target
        nearby_enemy_hexes = some_ship.track_targets()
        if some_hex not in nearby_enemy_hexes:
            return False

        result = self._game_ship_salvo_action(some_ship, some_hex.entity)
        return result


    #move ship on board
    def _game_ship_move_action(self, some_hex):
        result = False
        selected_ship = self.selected_hex.entity
        #check if selcted hex direction does not match orientation
        if some_hex.empty and (some_hex in self.selected_hex.neighbors) and (some_hex.directions[selected_ship.orientation] != self.selected_hex.hex_coordinate_index or selected_ship.ship_type == 'DD' or selected_ship.ship_type == 'CS'):
            if selected_ship.ship_type == 'BB' and self.opsSpace.starHexes[some_hex.directions[selected_ship.orientation]] in self.selected_hex.neighbors:
                return result

            if selected_ship.ship_moves != 0:
                result = self.opsSpace.move_some_entity(selected_ship, some_hex)
                if result:
                    selected_ship.ship_moves -= 1
                    #check if hex controlled
                    if selected_ship.ship_moves != 0:
                        enemy_tracking = selected_ship.ping_hex(some_hex)
                        if enemy_tracking:
                            selected_ship.ship_moves -= 1

            else:
                print("No movements left!") 
        return result


    #fire all guns in range 
    def _game_ship_salvo_action(self, some_ship, enemy_ship):
        #check if guns are loaded
        guns_to_fire = some_ship.guns_primed()
        half_broadside = 0
        for j in guns_to_fire:
            if j in some_ship.armaments['broadside_battery']:
                if half_broadside % 2 == 1:
                    j.gun_load_time = 0
                    guns_to_fire.remove(j)
                half_broadside += 1

        #get the distance
        ballistic_distance = some_ship.range_finder(enemy_ship)

        total_damage = 0
        for g in guns_to_fire:
            if not enemy_ship.operational:
                print("ship Destroyed!")
                return True
            salvo_damage = 0
            true_damage = 0
            if g.gun_stats['RNG'] >= ballistic_distance:
                #find FP distribution ammong batteries
                batPow = 0  
                if g in some_ship.armaments['primary_battery']:
                    batPow = some_ship.ship_stats['FP'] // len(some_ship.armaments['primary_battery'])
                elif g in some_ship.armaments['secondary_battery']:
                    batPow = some_ship.ship_stats['FP'] // len(some_ship.armaments['secondary_battery'])
                elif g in some_ship.armaments['broadside_battery']:
                    batPow = some_ship.ship_stats['FP'] // len(some_ship.armaments['broadside_battery'])

                for a in range(0, g.gun_stats['QNT']):
                    if self._gun_hit_calculator(g.gun_stats['HIT'], some_ship.ship_stats['ACC'], enemy_ship.ship_stats['EVA']) is True:
                        salvo_damage += self._gun_damage_calculator(g.gun_stats['ATK'], some_ship.ship_stats['FP'], some_ship.ship_stats['LCK'], enemy_ship.ship_stats['LCK'], batPow)

                true_damage = enemy_ship.take_damage(salvo_damage, g.gun_stats['PEN'], g.gun_stats['DIS'])
                if not enemy_ship.operational:
                    m = enemy_ship.placeHex.hex_coordinate_index
                    self.game_ships.remove(enemy_ship) 
                    self.opsSpace.hexes_full.remove(self.opsSpace.starHexes[m])
                    self.opsSpace.starHexes[m].entity = []
                    self.opsSpace.starHexes[m].empty = True
                    true_damage = 0
                    #del enemy_ship
                    return True

                if true_damage > 0:
                    print(g.battery_ID, "Has Hit", enemy_ship.name, "For", true_damage, "Damage!")
                g.gun_load_time = 0
            total_damage += true_damage
            salvo_damage = 0
        print(some_ship.vessel_ID, some_ship.name, "Has done", total_damage, "Total Damage to", enemy_ship.vessel_ID, enemy_ship.name)
        return True


    #hit calculator for a gun
    def _gun_hit_calculator(self, some_gun_HIT, some_ship_ACC, enemy_ship_EVA):
        hit_rate = (some_ship_ACC - enemy_ship_EVA) + some_gun_HIT
        random_hit_value = randint(1, 100)
        gun_hit_bool = hit_rate > random_hit_value
        return gun_hit_bool


    #damage calculator for a gun
    def _gun_damage_calculator(self, some_gun_ATK, some_ship_FP, some_ship_LCK, enemy_ship_LCK, battery_distribution):
        crit_rate = some_ship_LCK - enemy_ship_LCK + 5
        damage_multiplier = 1
        random_crit_value = randint(1, 100)
        if crit_rate > random_crit_value:
            damage_multiplier = 1.25 + (some_ship_LCK / 100)
        damage = (some_gun_ATK + (some_ship_FP // battery_distribution) * damage_multiplier)
        return damage