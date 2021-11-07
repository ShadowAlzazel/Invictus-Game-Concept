#Started 11/5/2021 
#from . shipEquipment import *
#from . shipRole import Heavycruiser
from shipClasses.shipEquipment import *
from shipClasses.shipRole import Heavycruiser

"""--<->----------------------------HEAVYCRUISERS------------------------------<->--"""

#Apocalypse Class Heavycrusier
class ApocalypseClass(Heavycruiser):
    ammount = 0
    shipStats = {
        "FP": 350, "ACC": 33, "EVA": 30, "SPD": 25,
        "armor": 2.5, "luck": 10
    }
    
    shields = 10000
    hull = 10000

    def __init__(self, hullnumber, name):
        ApocalypseClass.ammount += 1
        super().__init__(hullnumber, name)
        vID = self.vesselID
        self.defenses['ShieldType'].append(HyperShieldGen(vID))
        self.defenses['ArmorType'].append(CarbonNanoThreadsArmor(vID))
        self.primaryBattery = [triple_M12_NeutronLauchers(vID, ''.join(['T', str(x)])) for x in range(1,6)]
        self.secondaryBattery = [triple_M7_TitanAutoCannons(vID, ''.join(['S', str(x)])) for x in range(1,4)] 
        self.broadsideBattery = []
        for x in range(1, 11):
            if x <= 8:
                self.broadsideBattery.append(double_M6_TitanAutoCannons(vID, ''.join(['B', str(x)])))
            elif x <= 10:
                self.broadsideBattery.append(double_A5_LaserLance(vID, ''.join(['B', str(x)])))
