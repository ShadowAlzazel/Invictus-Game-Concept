from shipClasses.shipEquipment import *
from shipClasses.shipRole import Heavycruiser

#Heavy cruisers

#--------------------------Apocalypse Class Heavycrusier------------------------------
class ApocalypseClass(Heavycruiser):
    shipClass = 'ApocalypseClass'
    ammount = 0
    ship_stats = {
        "FP": 393, "ACC": 32, "EVA": 29, "SPD": 5,
        "RDR": 5, "LCK": 10, "STH": 0
    }
    
    shields = 11000
    hull = 10500

    def __init__(self, hullnumber, name, command, fleet_name):
        ApocalypseClass.ammount += 1
        super().__init__(hullnumber, name, command, fleet_name)
        vID = self.vessel_ID
        self.radar = hex_radar(vID, self.ship_stats['RDR'])
        self.defenses['shield_gen'].append(GigaShieldGen(vID))
        self.defenses['armor_type'].append(LivingDurasteelArmor(vID))
        self.armaments['primary_battery'] = [triple_M12_GaussCannons(vID, ''.join(['T', str(x)])) for x in range(1,6)]
        self.armaments['secondary_battery'] = [triple_P6_PlasmaPhasers(vID, ''.join(['S', str(x)])) for x in range(1,4)] 
        for x in range(1, 11):
            if x <= 8:
                self.armaments['broadside_battery'].append(double_M6_TitanAutoCannons(vID, ''.join(['B', str(x)])))
            elif x <= 10:
                self.armaments['broadside_battery'].append(double_P6_PlasmaPhasers(vID, ''.join(['B', str(x)])))


#--------------------------Apocalypse Class Heavycrusier------------------------------
class HarbingerClass(Heavycruiser):
    shipClass = 'HarbingerClass'
    ammount = 0
    ship_stats = {
        "FP": 377, "ACC": 34, "EVA": 30, "SPD": 5,
        "RDR": 5, "LCK": 10, "STH": 0
    }
    
    shields = 11300
    hull = 10000

    def __init__(self, hullnumber, name, command, fleet_name):
        HarbingerClass.ammount += 1
        super().__init__(hullnumber, name, command, fleet_name)
        vID = self.vessel_ID
        self.radar = hex_radar(vID, self.ship_stats['RDR'])
        self.defenses['shield_gen'].append(GigaShieldGen(vID))
        self.defenses['armor_type'].append(LivingDurasteelArmor(vID))
        self.armaments['primary_battery'] = [triple_A12_ProtonColliders(vID, ''.join(['T', str(x)])) for x in range(1,6)]
        self.armaments['secondary_battery'] = [triple_P6_PlasmaPhasers(vID, ''.join(['S', str(x)])) for x in range(1,4)] 
        for x in range(1, 11):
            if x <= 8:
                self.armaments['broadside_battery'].append(double_M6_TitanAutoCannons(vID, ''.join(['B', str(x)])))
            elif x <= 10:
                self.armaments['broadside_battery'].append(double_P6_PlasmaPhasers(vID, ''.join(['B', str(x)])))