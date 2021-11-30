from shipClasses.shipEquipment import *
from shipClasses.shipRole import Heavycruiser

#Heavy cruisers

#--------------------------Apocalypse Class Heavycrusier------------------------------
class ApocalypseClass(Heavycruiser):
    shipClass = 'ApocalypseClass'
    ammount = 0
    shipStats = {
        "FP": 393, "ACC": 32, "EVA": 29, "SPD": 5,
        "RDR": 5, "LCK": 10, "STH": 0
    }
    
    shields = 10000
    hull = 10000

    def __init__(self, hullnumber, name):
        ApocalypseClass.ammount += 1
        super().__init__(hullnumber, name)
        vID = self.vesselID
        self.radar = shipHexRadar(vID, self.shipStats['RDR'])
        self.defenses['shieldType'].append(HyperShieldGen(vID))
        self.defenses['armorType'].append(CarbonNanoThreadsArmor(vID))
        self.armaments['primaryBattery'] = [triple_M12_GaussCannons(vID, ''.join(['T', str(x)])) for x in range(1,6)]
        self.armaments['secondaryBattery'] = [triple_M7_TitanAutoCannons(vID, ''.join(['S', str(x)])) for x in range(1,4)] 
        for x in range(1, 11):
            if x <= 8:
                self.armaments['broadsideBattery'].append(double_M6_TitanAutoCannons(vID, ''.join(['B', str(x)])))
            elif x <= 10:
                self.armaments['broadsideBattery'].append(double_P6_PlasmaPhasers(vID, ''.join(['B', str(x)])))


#--------------------------Apocalypse Class Heavycrusier------------------------------
class HarbingerClass(Heavycruiser):
    shipClass = 'HarbingerClass'
    ammount = 0
    shipStats = {
        "FP": 375, "ACC": 34, "EVA": 30, "SPD": 5,
        "RDR": 5, "LCK": 10, "STH": 0
    }
    
    shields = 10000
    hull = 10000

    def __init__(self, hullnumber, name):
        HarbingerClass.ammount += 1
        super().__init__(hullnumber, name)
        vID = self.vesselID
        self.radar = shipHexRadar(vID, self.shipStats['RDR'])
        self.defenses['shieldType'].append(HyperShieldGen(vID))
        self.defenses['armorType'].append(CarbonNanoThreadsArmor(vID))
        self.armaments['primaryBattery'] = [triple_A12_ProtonColliders(vID, ''.join(['T', str(x)])) for x in range(1,6)]
        self.armaments['secondaryBattery'] = [triple_P6_PlasmaPhasers(vID, ''.join(['S', str(x)])) for x in range(1,4)] 
        for x in range(1, 11):
            if x <= 8:
                self.armaments['broadsideBattery'].append(double_M6_TitanAutoCannons(vID, ''.join(['B', str(x)])))
            elif x <= 10:
                self.armaments['broadsideBattery'].append(double_P6_PlasmaPhasers(vID, ''.join(['B', str(x)])))