#Started 11/5/2021
#from . shipEquipment import *
#from . shipRole import Lightcruiser
from shipClasses.shipEquipment import *
from shipClasses.shipRole import Lightcruiser

"""--<->----------------------------LIGHTCRUISERS------------------------------<->--"""

#Midnight Class Light Cruiser 
class MidnightClass(Lightcruiser):
    ammount = 0 
    shiptype = 'CL'
    shipStats = {
        "FP": 200, "ACC": 35, "EVA": 45, "SPD": 35,
        "armor": 2, "luck": 10
    }
    
    shields = 7500
    hull = 7500

    def __init__(self, hullnumber, name):
        MidnightClass.ammount += 1
        super().__init__(hullnumber, name)
        vID = self.vesselID
        self.defenses['ShieldType'].append(HyperShieldGen(vID))
        self.defenses['ArmorType'].append(TitaniumArmor(vID))
        self.primaryBattery = [triple_A6_LaserLance(vID, ''.join(['T', str(x)])) for x in range(1, 5)]
        self.secondaryBattery = [double_M4_ShredderAutoGuns(vID, ''.join(['S', str(x)])) for x in range(1, 3)] 
        self.broadsideBattery = [quad_BPoDS(vID, ''.join(['S', str(x)])) for x in range(1, 5)]

