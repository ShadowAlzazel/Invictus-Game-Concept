#Started 11/5/2021 
#from . shipEquipment import *
#from . shipRole import Battlecruiser
from shipClasses.shipEquipment import *
from shipClasses.shipRole import Battlecruiser

"""--<->----------------------------BATTLECRUISERS------------------------------<->--"""

#Zenith Class Battlecruiser
class ZenithClass(Battlecruiser):
    ammount = 0
    shipStats = {       
        "FP": 493, "ACC": 47, "EVA": 37, "SPD": 31,
        "armor": 2.75, "luck": 10
    }

    shields = 27500
    hull = 11700

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        vID = self.vesselID
        self.defenses['ShieldType'].append(DarkEnergyShieldGen(vID))
        self.defenses['ArmorType'].append(MythrilAlloyArmor(vID))
        self.primaryBattery = []
        for x in range(1, 6):
            if x <= 3:
                self.primaryBattery.append(double_A17_HAT3ArcThrowers(vID, ''.join(['T', str(x)])))
            elif x <= 5:
                self.primaryBattery.append(triple_L18_DeuteriumLance(vID, ''.join(['T', str(x)])))
        self.secondaryBattery = []
        for x in range(1,6):
            if x <= 2:
                self.secondaryBattery.append(quadruple_M12_NeutronLauchers(vID, ''.join(['S', str(x)])))
            elif x <= 4:
                self.secondaryBattery.append(triple_A11_TeslaArcThrowers(vID, ''.join(['S', str(x)])))
            elif x <= 5: 
                 self.secondaryBattery.append(triple_L13_HadronLance(vID, ''.join(['S', str(x)])))
        self.broadsideBattery = []
        for x in range(1, 17):
            if x <= 8:
                self.broadsideBattery.append(double_M6_TitanAutoCannons(vID, ''.join(['B', str(x)])))
            elif x <= 16:
                self.broadsideBattery.append(double_A5_LaserLance(vID, ''.join(['B', str(x)])))

        ZenithClass.ammount += 1

#Eclipse Class Battlecruiser
class EclipseClass(Battlecruiser):
    ammount = 0
    shipStats = {       
        "FP": 517, "ACC": 45, "EVA": 35, "SPD": 29,
        "armor": 2.75, "luck": 10
    }

    shields = 25600
    hull = 13800

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)
        vID = self.vesselID
        self.defenses['ShieldType'].append(DarkEnergyShieldGen(vID))
        self.defenses['ArmorType'].append(MythrilAlloyArmor(vID))
        self.primaryBattery = []
        for x in range(1, 5):
            if x <= 2:
                self.primaryBattery.append(triple_L18_DeuteriumLance(vID, ''.join(['T', str(x)])))
            elif x <= 4:
                self.primaryBattery.append(double_M22_ThorGigaGuns(vID, ''.join(['T', str(x)])))
        self.secondaryBattery = [quadruple_M12_NeutronLauchers(vID, ''.join(['S', str(x)])) for x in range(1,5)]
        self.broadsideBattery = []
        for x in range(1, 17):
            if x <= 8:
                self.broadsideBattery.append(double_A5_LaserLance(vID, ''.join(['B', str(x)])))
            elif x <= 12:
                self.broadsideBattery.append(double_A5_WaveArcThrowers(vID, ''.join(['B', str(x)])))
            elif x <= 16:
                self.broadsideBattery.append(double_M6_TitanAutoCannons(vID, ''.join(['B', str(x)])))
        
        EclipseClass.ammount += 1

#Penumbra Class Battlecruiser
class PenumbraClass(Battlecruiser):
    ammount = 0
    shipStats = {       
        "FP": 505, "ACC": 45, "EVA": 35, "SPD": 30,
        "armor": 2.75, "luck": 10
    }

    shields = 23500
    hull = 14500

    def __init__(self, hullnumber, name):
        PenumbraClass.ammount += 1
        super().__init__(hullnumber, name)
        vID = self.vesselID
        self.defenses['ShieldType'].append(DarkEnergyShieldGen(vID))
        self.defenses['ArmorType'].append(MythrilAlloyArmor(vID))
        self.primaryBattery = [double_L18_DeuteriumLance(vID, ''.join(['T', str(x)])) for x in range(1,7)]
        self.secondaryBattery = [quadruple_M12_NeutronLauchers(vID, ''.join(['S', str(x)])) for x in range(1,3)]
        self.broadsideBattery = []
        for x in range(1, 17):
            if x <= 8:
                self.broadsideBattery.append(double_M6_TitanAutoCannons(vID, ''.join(['B', str(x)])))
            elif x <= 16:
                self.broadsideBattery.append(double_A5_LaserLance(vID, ''.join(['B', str(x)])))
