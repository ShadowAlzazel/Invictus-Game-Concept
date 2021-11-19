from shipClasses.shipEquipment import *
from shipClasses.shipRole import Strikecruiser

#strike cruisers

#----------------------------------Voltage Class Strikecruiser-----------------------------------
class VoltageClass(Strikecruiser):
    shipClass = 'VoltageClass'
    ammount = 0
    shipStats = {
        "FP": 287, "ACC": 39, "EVA": 41, "SPD": 6,
        "RDR": 5, "LCK": 10
    }
    
    shields = 12000
    hull = 8800

    def __init__(self, hullnumber, name):
        VoltageClass.ammount += 1
        super().__init__(hullnumber, name)
        vID = self.vesselID
        self.radar = shipHexRadar(vID, self.shipStats['RDR'])
        self.defenses['shieldType'].append(HyperShieldGen(vID))
        self.defenses['armorType'].append(OrichalcumAlloyArmor(vID))
        
        for x in range(1, 7):
            if x <= 2:
                self.armaments['primaryBattery'].append(double_F14_MatterErasers(vID, ''.join(['T', str(x)])))
            elif x <= 6:
                self.armaments['primaryBattery'].append(triple_A11_TeslaArcThrowers(vID, ''.join(['T', str(x)])))
        self.armaments['secondaryBattery'] = [triple_L9_UltravioletLasers(vID, ''.join(['S', str(x)])) for x in range(1,3)]
        for x in range(1, 9):
            if x <= 4:
                self.armaments['broadsideBattery'].append(double_M4_ShredderAutoGuns(vID, ''.join(['B', str(x)])))
            else:
                self.armaments['broadsideBattery'].append(double_L5_WaveLasers(vID, ''.join(['B', str(x)])))


#-------------------------------------Dynamo Class Strikecruiser----------------------------------------
class DynamoClass(Strikecruiser):
    shipClass = 'DynamoClass'
    ammount = 0
    shipStats = {
        "FP": 298, "ACC": 40, "EVA": 38, "SPD": 6,
        "RDR": 5, "LCK": 10
    }
    
    shields = 13000
    hull = 8200

    def __init__(self, hullnumber, name):
        DynamoClass.ammount += 1
        super().__init__(hullnumber, name)
        vID = self.vesselID
        self.radar = shipHexRadar(vID, self.shipStats['RDR'])
        self.defenses['shieldType'].append(HyperShieldGen(vID))
        self.defenses['armorType'].append(OrichalcumAlloyArmor(vID))
        for x in range(1, 7):
            if x <= 4:
                self.armaments['primaryBattery'].append(triple_L13_XRayLasers(vID, ''.join(['T', str(x)])))
            elif x <= 6:
                self.armaments['primaryBattery'].append(double_L13_XRayLasers(vID, ''.join(['T', str(x)])))
        self.armaments['secondaryBattery'] = [triple_L6_ParticleLance(vID, ''.join(['S', str(x)])) for x in range(1,5)]
        for x in range(1, 9):
            if x <= 4:
                self.armaments['broadsideBattery'].append(double_L5_WaveLasers(vID, ''.join(['B', str(x)])))
            else:
                self.armaments['broadsideBattery'].append(double_A5_ArcThrowers(vID, ''.join(['B', str(x)])))