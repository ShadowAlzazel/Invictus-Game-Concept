#LIGHTCRUISERS
from shipClasses.shipEquipment import *
from shipClasses.shipRole import Lightcruiser

#--------------------------------Midnight-Class-Light-Cruiser--------------------------------- 
class Midnight_Class(Lightcruiser):
    ship_class = 'Midnight-Class'
    ammount = 0 
    ship_type = 'CL'
    ship_stats = {
        "FP": 200, "ACC": 35, "EVA": 49, "SPD": 7,
        "RDR": 5, "LCK": 10, "STH": 2
    }
    
    shields = 7500
    hull = 7500

    def __init__(self, hullnumber, name, command, fleet_name):
        Midnight_Class.ammount += 1
        super().__init__(hullnumber, name, command, fleet_name)
        vID = self.vessel_ID
        self.radar = hex_radar(vID, self.ship_stats['RDR'])
        self.defenses['shield_gen'].append(LumioneShieldGen(vID))
        self.defenses['armor_type'].append(CarbonNanoThreadsArmor(vID))
        self.armaments['primary_battery'] = [triple_L6_ParticleLance(vID, ''.join(['T', str(x)])) for x in range(1, 6)]
        self.armaments['secondary_battery'] = [triple_M5_WraithAutoGuns(vID, ''.join(['S', str(x)])) for x in range(1, 3)] 
        self.armaments['secondary_battery'].append(VLS_35C_DevestationMissiles(vID, 'M1'))
        self.armaments['broadside_battery'] = [quad_BPoDS(vID, ''.join(['B', str(x)])) for x in range(1, 7)]