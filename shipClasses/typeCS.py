from shipClasses.shipEquipment import *
from shipClasses.shipRole import Strikecruiser

#strike cruisers

#----------------------------------Voltage Class Strikecruiser-----------------------------------
class Voltage_Class(Strikecruiser):
    ship_class = 'Voltage-Class'
    ammount = 0
    ship_stats = {
        "FP": 287, "ACC": 39, "EVA": 41, "SPD": 6,
        "RDR": 5, "LCK": 10, "STH": 1
    }
    
    shields = 12000
    hull = 8800

    def __init__(self, hullnumber, name, command, fleet_name):
        Voltage_Class.ammount += 1
        super().__init__(hullnumber, name, command, fleet_name)
        vID = self.vessel_ID
        self.radar = hex_radar(vID, self.ship_stats['RDR'])
        self.defenses['shield_gen'].append(HyperiumShieldGen(vID))
        self.defenses['armor_type'].append(MythrilAlloyArmor(vID))
        
        for x in range(1, 7):
            if x <= 2:
                self.armaments['primary_battery'].append(double_F14_MatterErasers(vID, ''.join(['T', str(x)])))
            elif x <= 6:
                self.armaments['primary_battery'].append(triple_A11_TeslaArcThrowers(vID, ''.join(['T', str(x)])))
        self.armaments['secondary_battery'] = [triple_L9_UltravioletLasers(vID, ''.join(['S', str(x)])) for x in range(1,3)]
        for x in range(1, 9):
            if x <= 4:
                self.armaments['broadside_battery'].append(double_M4_ShredderAutoGuns(vID, ''.join(['B', str(x)])))
            else:
                self.armaments['broadside_battery'].append(double_L5_WaveLasers(vID, ''.join(['B', str(x)])))


#-------------------------------------Dynamo Class Strikecruiser----------------------------------------
class Dynamo_Class(Strikecruiser):
    ship_class = 'Dynamo-Class'
    ammount = 0
    ship_stats = {
        "FP": 298, "ACC": 40, "EVA": 38, "SPD": 6,
        "RDR": 5, "LCK": 10, "STH": 1
    }
    
    shields = 13000
    hull = 8200

    def __init__(self, hullnumber, name, command, fleet_name):
        Dynamo_Class.ammount += 1
        super().__init__(hullnumber, name, command, fleet_name)
        vID = self.vessel_ID
        self.radar = hex_radar(vID, self.ship_stats['RDR'])
        self.defenses['shield_gen'].append(HyperiumShieldGen(vID))
        self.defenses['armor_type'].append(MythrilAlloyArmor(vID))
        for x in range(1, 7):
            if x <= 4:
                self.armaments['primary_battery'].append(triple_L13_XRayLasers(vID, ''.join(['T', str(x)])))
            elif x <= 6:
                self.armaments['primary_battery'].append(double_L13_XRayLasers(vID, ''.join(['T', str(x)])))
        self.armaments['secondary_battery'] = [triple_L6_ParticleLance(vID, ''.join(['S', str(x)])) for x in range(1,5)]
        for x in range(1, 9):
            if x <= 4:
                self.armaments['broadside_battery'].append(double_L5_WaveLasers(vID, ''.join(['B', str(x)])))
            else:
                self.armaments['broadside_battery'].append(double_A5_ArcThrowers(vID, ''.join(['B', str(x)])))


#-------------------------------------Dynamo Class Strikecruiser----------------------------------------
class Hero_Class(Strikecruiser):
    ship_class = 'Hero-Class'
    ammount = 0
    ship_stats = {
        "FP": 333, "ACC": 40, "EVA": 38, "SPD": 6,
        "RDR": 5, "LCK": 10, "STH": 1
    } 
    
    shields = 12400
    hull = 8700

    def __init__(self, hullnumber, name, command, fleet_name):
        Hero_Class.ammount += 1
        super().__init__(hullnumber, name, command, fleet_name)
        vID = self.vessel_ID
        self.radar = hex_radar(vID, self.ship_stats['RDR'])
        self.defenses['shield_gen'].append(HyperiumShieldGen(vID))
        self.defenses['armor_type'].append(MythrilAlloyArmor(vID))
        for x in range(1, 7):
            if x <= 4:
                self.armaments['primary_battery'].append(triple_L13_XRayLasers(vID, ''.join(['T', str(x)])))
            elif x <= 6:
                self.armaments['primary_battery'].append(double_L13_XRayLasers(vID, ''.join(['T', str(x)])))
        self.armaments['secondary_battery'] = [triple_L6_ParticleLance(vID, ''.join(['S', str(x)])) for x in range(1,5)]
        for x in range(1, 9):
            if x <= 4:
                self.armaments['broadside_battery'].append(double_L5_WaveLasers(vID, ''.join(['B', str(x)])))
            else:
                self.armaments['broadside_battery'].append(double_A5_ArcThrowers(vID, ''.join(['B', str(x)])))