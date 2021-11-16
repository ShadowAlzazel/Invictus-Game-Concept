from shipClasses.shipEquipment import *
from shipClasses.shipRole import Destroyer

#Destroyers

#-----------------------------Johnston Class destroyer-------------------------------
class JohnstonClass(Destroyer):
    shipClass = 'JohnstonClass'
    ammount = 0
    shipStats = {
        "FP": 67, "ACC": 48, "EVA": 66, "SPD": 9,
        "RDR": 5, "LCK": 10
    }
    
    def __init__(self, hullnumber, name):
        JohnstonClass.ammount += 1
        super().__init__(hullnumber, name)
        vID = self.vesselID
        self.radar = shipHexRadar(vID, self.shipStats['RDR'])
        self.defenses['shieldType'].append(LumioneShieldGen(vID))
        self.defenses['armorType'].append(TitaniumArmor(vID))
        self.armaments['primaryBattery'] = [double_M6_TitanAutoCannons(vID, 'T1'), double_M4_ShredderAutoGuns(vID, 'T2')]
        
        

#------------------------------------Shimakaze class destroyer---------------------------------------
class ShimakazeClass(Destroyer):
    shipClass = 'ShimakazeClass'
    ammount = 0
    shipStats = {
        "FP": 47, "ACC": 58, "EVA": 68, "SPD": 9,
        "RDR": 5, "LCK": 10
    }

    def __init__(self, hullnumber, name):
        ShimakazeClass.ammount += 1
        super().__init__(hullnumber, name)
        vID = self.vesselID
        self.radar = shipHexRadar(vID, self.shipStats['RDR'])
        self.defenses['shieldType'].append(LumioneShieldGen(vID))
        self.defenses['armorType'].append(TitaniumArmor(vID))
        self.armaments['primaryBattery'] = [double_M6_TitanAutoCannons(vID, 'T1'), double_M4_ShredderAutoGuns(vID, 'T2')]
        
        
