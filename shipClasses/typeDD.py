#Started 11/5/2021 
#from . shipEquipment import *
#from . shipRole import Destroyer
from shipClasses.shipEquipment import *
from shipClasses.shipRole import Destroyer

"""--<->--------------------------DESTROYERS---------------------------<->--"""

#Johnston Class destroyer
class JohnstonClass(Destroyer):
    ammount = 0
    shipStats = {
        "FP": 67, "ACC": 48, "EVA": 66, "SPD": 55,
        "armor": 1, "luck": 10
    }
    
    def __init__(self, hullnumber, name):
        JohnstonClass.ammount += 1
        super().__init__(hullnumber, name)
        vID = self.vesselID
        self.defenses['ShieldType'].append(LumioneShieldGen(vID))
        self.defenses['ArmorType'].append(TitaniumArmor(vID))
        self.primaryBattery = [double_M6_TitanAutoCannons(vID, 'T1'), double_M4_ShredderAutoGuns(vID, 'T2')]
        self.secondaryBattery = []
        self.broadsideBattery = []

#Shimakaze class destroyer
class ShimakazeClass(Destroyer):
    ammount = 0
    shipStats = {
        "FP": 47, "ACC": 58, "EVA": 68, "SPD": 61,
        "armor": 1, "luck": 10
    }

    def __init__(self, hullnumber, name):
        ShimakazeClass.ammount += 1
        super().__init__(hullnumber, name)
        vID = self.vesselID
        self.defenses['ShieldType'].append(LumioneShieldGen(vID))
        self.defenses['ArmorType'].append(TitaniumArmor(vID))
        self.primaryBattery = [double_M6_TitanAutoCannons(vID, 'T1'), double_M4_ShredderAutoGuns(vID, 'T2')]
        self.secondaryBattery = []
        self.broadsideBattery = []
