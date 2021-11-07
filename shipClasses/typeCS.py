#Started 11/5/2021 
#from . shipEquipment import *
#from . shipRole import Strikecruiser
from shipClasses.shipEquipment import *
from shipClasses.shipRole import Strikecruiser

"""--<->----------------------------STRIKECRUISERS------------------------------<->--"""

#Voltage Class Strikecruiser
class VoltageClass(Strikecruiser):
    ammount = 0
    shipStats = {
        "FP": 287, "ACC": 39, "EVA": 41, "SPD": 34,
        "armor": 2.5, "luck": 10
    }
    
    shields = 12000
    hull = 8800

    def __init__(self, hullnumber, name):
        VoltageClass.ammount += 1
        super().__init__(hullnumber, name)
        vID = self.vesselID
        self.defenses['ShieldType'].append(HyperShieldGen(vID))
        self.defenses['ArmorType'].append(OrichalcumAlloyArmor(vID))
        self.primaryBattery = []
        for x in range(1, 5):
            if x <= 2:
                self.primaryBattery.append(triple_L13_HadronLance(vID, ''.join(['T', str(x)])))
            elif x <= 4:
                self.primaryBattery.append(triple_A11_TeslaArcThrowers(vID, ''.join(['T', str(x)])))
        self.secondaryBattery = [triple_M7_TitanAutoCannons(vID, ''.join(['S', str(x)])) for x in range(1,3)]
        self.broadsideBattery = []
        for x in range(1, 9):
            if x <= 4:
                self.broadsideBattery.append(double_M4_ShredderAutoGuns(vID, ''.join(['B', str(x)])))
            elif x <= 8:
                self.broadsideBattery.append(double_A5_LaserLance(vID, ''.join(['B', str(x)])))


#Dynamo Class Strikecruiser
class DynamoClass(Strikecruiser):
    ammount = 0
    shipStats = {
        "FP": 298, "ACC": 40, "EVA": 38, "SPD": 32,
        "armor": 2.5, "luck": 10
    }
    
    shields = 13000
    hull = 8200

    def __init__(self, hullnumber, name):
        DynamoClass.ammount += 1
        super().__init__(hullnumber, name)
        vID = self.vesselID
        self.defenses['ShieldType'].append(HyperShieldGen(vID))
        self.defenses['ArmorType'].append(OrichalcumAlloyArmor(vID))
        self.primaryBattery = []
        for x in range(1, 5):
            if x <= 2:
                self.primaryBattery.append(triple_M12_NeutronLauchers(vID, ''.join(['T', str(x)])))
            elif x <= 4:
                self.primaryBattery.append(triple_A11_TeslaArcThrowers(vID, ''.join(['T', str(x)])))
        self.secondaryBattery = [triple_A6_LaserLance(vID, ''.join(['S', str(x)])) for x in range(1,3)]
        self.broadsideBattery = []
        for x in range(1, 9):
            if x <= 4:
                self.broadsideBattery.append(double_M4_ShredderAutoGuns(vID, ''.join(['B', str(x)])))
            elif x <= 8:
                self.broadsideBattery.append(double_A5_WaveArcThrowers(vID, ''.join(['B', str(x)])))