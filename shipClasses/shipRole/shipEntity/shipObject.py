#Basic Ship Object
#"""-------------------------------SHIP-OBJECT-------------------------------------"""

class Ship:
    entity_type = 'ship_entity'
    ammount = 0
    ship_type = 'CIV'
    ship_stats = {
        "FP": 10, "ACC": 10, "EVA": 50, "SPD": 5,
        "RDR": 3, "LCK": 10, "STH": 1
    }

    def __init__(self, hullnumber, name, command, fleet_name):
        Ship.ammount += 1
        self.operational = True
        self.command = command
        self.fleet_name = fleet_name
        self.name = name
        self.hullnumber = hullnumber
        self.vessel_ID = ''.join([self.ship_type, '-', str(self.hullnumber)])
        self.place_hex = []  #space_hex object
        self.orientation = 'R'
        self.radar = []  #radar object
        self.armaments = {'primary_battery': [], 'secondary_battery': [], 'broadside_battery': []}
        self.defenses = {'shield_gen': [], 'armor_type': []}
        self.detected = True 
        self.revealed = False
        
        print("New Ship Launched", end=': ')
        print(self.command, '-', name, sep='', end=', ')

    #damage function that takes in a value 
    def take_damage(self, damage_amount, wep_PEN=0, wep_DIS=1):
        if self.shields > damage_amount and wep_DIS > 0:
            damage_to_shields = self.defenses['shield_gen'][0].take_shield_damage(damage_amount, wep_DIS)
            self.shields -= damage_to_shields
            return damage_to_shields
        elif self.hull > damage_amount:
            damage_to_hull = self.defenses['armor_type'][0].take_armor_damage(damage_amount, wep_PEN) - self.shields
            self.shields = 0
            self.hull -= damage_to_hull
            return damage_to_hull
        else: 
            self.hull = 0
            print(self.vessel_ID, self.command, self.name, "has been destryed!")
            self._destroy_self_ship()


    #destroy ship
    def _destroy_self_ship(self):
        self.operational = False


    #full self repair
    def reset_ship(self):
        self.hull = self.__class__.hull
        self.shields = self.__class__.shields
        print(self.name, "Reset!")


    #ping nearby hex to see if controlled
    def ping_hex(self, some_hex):
        p = self.radar.radar_pinger(self.place_hex, some_hex)
        return p


    #find targets with radar
    def detect_targets(self):
        targetsHexes = self.radar.radar_detecter(self.ship_stats['RDR'], self.place_hex)
        return targetsHexes


    #find tracked targets within ready gun range 
    def track_targets(self):
        battery_ranges = [0]
        guns_ready_in_range = self.guns_primed()
        if not guns_ready_in_range:
            return False

        for w in guns_ready_in_range:
            battery_ranges.append(w.gun_stats['RNG'])    
        targetsHexes = self.radar.radar_tracker(max(battery_ranges), self.place_hex)
        return targetsHexes


    #find ranges 
    def range_finder(self, target_ship):
        r = self.radar.radar_ballistics_finder(self.ship_stats['RDR'], self.place_hex, target_ship.place_hex)
        return r


    #chech all guns ready to fire
    def guns_primed(self):
        primed = []
        for b in self.armaments.values():
            for g in b:
                if g.gun_load_time == g.gun_stats['RLD']:
                    primed.append(g)
        return primed


    #reload all guns
    def reload_battery(self):
        for b in self.armaments.values():
            for g in b:
                g.reload_gun()


    #recharge shields and repair armor
    def recharge_defenses(self):
        regen_ammount = (self.__class__.shields * (self.defenses['shield_gen'][0].shield_regeneration / 100))
        if self.__class__.shields > self.shields + regen_ammount:
            self.shields += regen_ammount

        if self.defenses['armor_type'][0].armor_integrity < 100 - self.defenses['armor_type'][0].armor_repair:
            self.defenses['armor_type'][0].armor_integrity += self.defenses['armor_type'][0].armor_repair


    #inspection function to look at stats
    def full_inspect(self):
        print("--<->---------------------------------------------------------------------<->--")
        print("Name: ", end='')
        print(self.command,'-' , self.name, sep='')
        print("Vessel Identifier: ", end='')
        print(self.vessel_ID)
        print("Ship Stats:")
        print(self.ship_stats)
        print("Primary Armament:")
        for x in self.armaments['primary_battery']:
            print(x.gun_name, "in Turret", x.battery_ID)
        print("Ship Defenses:")
        print(self.defenses['armor_type'][0].armor_name)
        print(self.defenses['shield_gen'][0].shield_name)
        print("Shield Capcity at", "%.2f%%" % ((self.shields / self.__class__.shields) * 100.0), end=', ')
        print("with", self.shields // 1, "out of", self.__class__.shields, "remaining")
        print("Hull Integrity at", "%.2f%%" % ((self.hull / self.__class__.hull) * 100.0), end=', ')
        print("with", self.hull // 1, "out of", self.__class__.hull, "remaining")
        print("--<->---------------------------------------------------------------------<->--")
