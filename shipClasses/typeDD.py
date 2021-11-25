from shipClasses.shipEquipment import *
from shipClasses.shipRole import Destroyer

#Destroyers

#-----------------------------Johnston Class destroyer-------------------------------
class JohnstonClass(Destroyer):
    shipClass = 'JohnstonClass'
    ammount = 0
    shipStats = {
        "FP": 67, "ACC": 35, "EVA": 66, "SPD": 8,
        "RDR": 5, "LCK": 10, "STH": 2
    }
    
    shields = 3350
    hull = 2600

    def __init__(self, hullnumber, name):
        JohnstonClass.ammount += 1
        super().__init__(hullnumber, name)
        vID = self.vesselID
        self.radar = shipHexRadar(vID, self.shipStats['RDR'])
        self.defenses['shieldType'].append(LumioneShieldGen(vID))
        self.defenses['armorType'].append(TitaniumArmor(vID))
        for x in range(1,7):
            if x <= 4:
                self.armaments['primaryBattery'].append(double_M6_TitanAutoCannons(vID, ''.join(['T', str(x)])))
            else:
                self.armaments['primaryBattery'].append(double_M4_ShredderAutoGuns(vID, ''.join(['T', str(x)])))
        self.armaments['secondaryBattery'] = [VLS_35C_DevestationMissiles(vID, 'M1'), VLS_21C_AnnihilationMissiles(vID, 'M2')]
                

#------------------------------------Shimakaze class destroyer---------------------------------------
class ShimakazeClass(Destroyer):
    shipClass = 'ShimakazeClass'
    ammount = 0
    shipStats = {
        "FP": 47, "ACC": 35, "EVA": 68, "SPD": 8,
        "RDR": 5, "LCK": 10, "STH": 2
    }

    shields = 3600
    hull = 2300

    def __init__(self, hullnumber, name):
        ShimakazeClass.ammount += 1
        super().__init__(hullnumber, name)
        vID = self.vesselID
        self.radar = shipHexRadar(vID, self.shipStats['RDR'])
        self.defenses['shieldType'].append(LumioneShieldGen(vID))
        self.defenses['armorType'].append(TitaniumArmor(vID))
        for x in range(1,7):
            if x <= 2:
                self.armaments['primaryBattery'].append(triple_L5_WaveLasers(vID, ''.join(['T', str(x)])))
            else:
                self.armaments['primaryBattery'].append(double_M4_ShredderAutoGuns(vID, ''.join(['T', str(x)])))
        self.armaments['secondaryBattery'] = [FLP5_DevestationTorpedoes(vID, 'M1'), VLS_21C_AnnihilationMissiles(vID, 'M2')]
        