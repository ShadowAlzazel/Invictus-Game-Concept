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
        
        for x in range(1, 5):
            if x <= 2:
                self.armaments['primaryBattery'].append(triple_L13_HadronLance(vID, ''.join(['T', str(x)])))
            elif x <= 4:
                self.armaments['primaryBattery'].append(triple_A11_TeslaArcThrowers(vID, ''.join(['T', str(x)])))
        self.armaments['secondaryBattery'] = [triple_M7_TitanAutoCannons(vID, ''.join(['S', str(x)])) for x in range(1,3)]
        for x in range(1, 9):
            if x <= 4:
                self.armaments['broadsideBattery'].append(double_M4_ShredderAutoCannons(vID, ''.join(['B', str(x)])))
            elif x <= 8:
                self.armaments['broadsideBattery'].append(double_L6_ParticleLance(vID, ''.join(['B', str(x)])))


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
        for x in range(1, 5):
            if x <= 2:
                self.armaments['primaryBattery'].append(triple_M12_GaussCannons(vID, ''.join(['T', str(x)])))
            elif x <= 4:
                self.armaments['primaryBattery'].append(triple_A11_TeslaArcThrowers(vID, ''.join(['T', str(x)])))
        self.armaments['secondaryBattery'] = [triple_L6_ParticleLance(vID, ''.join(['S', str(x)])) for x in range(1,3)]
        for x in range(1, 9):
            if x <= 4:
                self.armaments['broadsideBattery'].append(double_M4_ShredderAutoCannons(vID, ''.join(['B', str(x)])))
            elif x <= 8:
                self.armaments['broadsideBattery'].append(double_A5_ArcThrowers(vID, ''.join(['B', str(x)])))