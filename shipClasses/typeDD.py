from shipClasses.shipEquipment import *
from shipClasses.shipRole import Destroyer

#Destroyers

#-----------------------------Johnston Class destroyer-------------------------------
class JohnstonClass(Destroyer):
    shipClass = 'JohnstonClass'
    ammount = 0
    ship_stats = {
        "FP": 67, "ACC": 35, "EVA": 66, "SPD": 8,
        "RDR": 5, "LCK": 10, "STH": 3
    }
    
    shields = 3350
    hull = 2600

    def __init__(self, hullnumber, name):
        JohnstonClass.ammount += 1
        super().__init__(hullnumber, name)
        vID = self.vesse_ID
        self.radar = hex_radar(vID, self.ship_stats['RDR'])
        self.defenses['shield_gen'].append(AdvancedShieldGen(vID))
        self.defenses['armor_type'].append(TitaniumArmor(vID))
        for x in range(1,7):
            if x <= 4:
                self.armaments['primary_battery'].append(double_M6_TitanAutoCannons(vID, ''.join(['T', str(x)])))
            else:
                self.armaments['primary_battery'].append(double_M4_ShredderAutoGuns(vID, ''.join(['T', str(x)])))
        self.armaments['secondary_battery'] = [VLS_35C_DevestationMissiles(vID, 'M1'), VLS_21C_AnnihilationMissiles(vID, 'M2')]
                

#------------------------------------Shimakaze class destroyer---------------------------------------
class ShimakazeClass(Destroyer):
    shipClass = 'ShimakazeClass'
    ammount = 0
    ship_stats = {
        "FP": 47, "ACC": 35, "EVA": 68, "SPD": 8,
        "RDR": 5, "LCK": 10, "STH": 3
    }

    shields = 3600
    hull = 2300

    def __init__(self, hullnumber, name):
        ShimakazeClass.ammount += 1
        super().__init__(hullnumber, name)
        vID = self.vesse_ID
        self.radar = hex_radar(vID, self.ship_stats['RDR'])
        self.defenses['shield_gen'].append(AdvancedShieldGen(vID))
        self.defenses['armor_type'].append(TitaniumArmor(vID))
        for x in range(1,7):
            if x <= 2:
                self.armaments['primary_battery'].append(triple_L5_WaveLasers(vID, ''.join(['T', str(x)])))
            else:
                self.armaments['primary_battery'].append(double_M4_ShredderAutoGuns(vID, ''.join(['T', str(x)])))
        self.armaments['secondary_battery'] = [FLP5_DevestationTorpedoes(vID, 'M1'), VLS_21C_AnnihilationMissiles(vID, 'M2')]
        